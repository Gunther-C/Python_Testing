import pytest
from flask import url_for
from tests.mocks import VALID_CLUB_NAME, INVALID_CLUB_NAME
from tests.mocks import VALID_COMPETITION_NAME, INVALID_COMPETITION_NAME


class TestBook:
    """
        Test : endpoint book
    """
    def test_book_valid(self, client, mock_clubs, mock_competitions):
        """
        Test that booking a competition is handled correctly.
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return : none
        """
        rv = client.get(url_for('book', competition=VALID_COMPETITION_NAME, club=VALID_CLUB_NAME))
        assert rv.status_code == 200
        assert f"{VALID_CLUB_NAME}".encode() in rv.data
        assert f"{VALID_COMPETITION_NAME}".encode() in rv.data

    def test_book_invalid_club(self, client, mock_clubs, mock_competitions):
        """
        Club Error Redirection Test
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return : none
        """
        rv = client.get(url_for('book', competition=VALID_COMPETITION_NAME, club=INVALID_CLUB_NAME))
        assert rv.status_code == 302
        assert rv.location == url_for('index')

        rv = client.get(rv.location)
        assert rv.status_code == 200
        assert b"No club found with the provided name." in rv.data

    def test_book_invalid_competition(self, client, mock_clubs, mock_competitions):
        """
        Competition Error Redirection Test
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return : none
        """
        rv = client.get(url_for('book', competition=INVALID_COMPETITION_NAME, club=VALID_CLUB_NAME))
        assert rv.status_code == 200
        assert b"No competition found with the provided name." in rv.data
