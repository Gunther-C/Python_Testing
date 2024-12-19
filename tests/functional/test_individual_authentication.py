import pytest
from flask import get_flashed_messages, url_for
from tests.mocks import VALID_CLUB_NAME, VALID_CLUB_EMAIL, INVALID_CLUB_EMAIL


class TestFunctionalAuthentication:
    """
        Test : endpoint show_summary
    """
    def test_functional_index(self, client):
        """
        Test that the index page loads correctly
        :param client:
        :return: none
        """
        index = client.get(url_for('index'))
        assert index.status_code == 200
        assert "GUDLFT Registration".encode() in index.data

    def test_functional_authentication_valid(self, client, mock_clubs, mock_competitions):
        """
        Test that the summary page displays the correct information
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return: none
        """
        homepage = client.post(url_for('show_summary'), data={'email': VALID_CLUB_EMAIL})
        assert homepage.status_code == 200
        assert f"{VALID_CLUB_NAME}".encode() in homepage.data

    def test_functional_authentication_invalid(self, client, mock_clubs, mock_competitions):
        """
        Test that an unknown email redirects to the index page and displays an error message
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return: none
        """
        homepage = client.post(url_for('show_summary'), data={"email": INVALID_CLUB_EMAIL})
        assert homepage.status_code == 302
        assert homepage.headers['Location'].endswith('/')


