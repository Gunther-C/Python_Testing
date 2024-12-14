import pytest
from flask import get_flashed_messages, url_for
from tests.mocks import VALID_CLUB_NAME, VALID_CLUB_EMAIL, INVALID_CLUB_EMAIL


class TestShowSummary:
    """
        Test : endpoint show_summary
    """
    def test_index(self, client):
        """
        Test that the index page loads correctly
        :param client:
        :return: none
        """
        rv = client.get(url_for('index'))
        assert rv.status_code == 200
        assert "GUDLFT Registration".encode() in rv.data

    def test_show_summary(self, client, mock_clubs, mock_competitions):
        """
        Test that the summary page displays the correct information
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return: none
        """
        rv = client.post(url_for('show_summary'), data={'email': VALID_CLUB_EMAIL})
        assert rv.status_code == 200
        assert f"{VALID_CLUB_NAME}".encode() in rv.data

    def test_unknown_email(self, client, mock_clubs, mock_competitions):
        """
        Test that an unknown email redirects to the index page and displays an error message
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return: none
        """
        rv = client.post(url_for('show_summary'), data={"email": INVALID_CLUB_EMAIL})
        assert rv.status_code == 302
        assert rv.headers['Location'].endswith('/')

        rv = client.get(rv.location)
        assert rv.status_code == 200
        assert b"No club found with the provided email." in rv.data

