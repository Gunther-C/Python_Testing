import pytest
from flask import get_flashed_messages, url_for
from tests.mocks import VALID_CLUB_NAME, INVALID_CLUB_NAME
from tests.mocks import VALID_COMPETITION_NAME, INVALID_COMPETITION_NAME, INVALID_COMPETITION_DATE


class TestIndividualBook:
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
        book = client.get(url_for('book', competition=VALID_COMPETITION_NAME, club=VALID_CLUB_NAME))
        assert book.status_code == 200
        assert f"{VALID_CLUB_NAME}".encode() in book.data
        assert f"{VALID_COMPETITION_NAME}".encode() in book.data

    def test_book_invalid_club(self, client, mock_clubs, mock_competitions):
        """
        Club Error Redirection Test
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return : none
        """
        book = client.get(url_for('book', competition=VALID_COMPETITION_NAME, club=INVALID_CLUB_NAME))
        assert book.status_code == 302
        assert book.headers['Location'].endswith('/')

    def test_book_invalid_competition(self, client, mock_clubs, mock_competitions):
        """
        Competition Error Redirection Test
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return : none
        """
        book = client.get(url_for('book', competition=INVALID_COMPETITION_NAME, club=VALID_CLUB_NAME))
        assert book.status_code == 200
        assert b"No competition found with the provided name." in book.data

    def test_book_invalid_date(self, client, mock_clubs, mock_competitions):
        """
        Test that booking a competition with an invalid date (past competition) displays an error message
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return: none
        """
        book = client.get(url_for('book', competition=INVALID_COMPETITION_DATE, club=VALID_CLUB_NAME))
        assert book.status_code == 200
        message = get_flashed_messages()
        assert f"This competition {INVALID_COMPETITION_DATE} has already taken place." in message
        assert f"This competition {INVALID_COMPETITION_DATE} has already taken place.".encode() in book.data
