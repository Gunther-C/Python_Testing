import pytest
from flask import url_for
from tests.mocks import VALID_CLUB_EMAIL, VALID_CLUB_NAME, INVALID_CLUB_NAME
from tests.mocks import VALID_COMPETITION_NAME


class TestIntegrationBook:

    def test_book_valid(self, client, mock_clubs, mock_competitions):
        """
        Test that booking a valid competition is handled correctly.
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return: none
        """
        _rv = client.post(url_for('show_summary'), data={'email': VALID_CLUB_EMAIL})
        assert _rv.status_code == 200
        rv = client.get(url_for('book', competition=VALID_COMPETITION_NAME, club=VALID_CLUB_NAME))
        assert rv.status_code == 200

    def test_book_invalid(self, client,  mock_clubs, mock_competitions):
        """
        Test booking a competition with an invalid club redirects to the index page with an error message.
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return: none
        """
        _rv = client.post(url_for('show_summary'), data={'email': VALID_CLUB_EMAIL})
        assert _rv.status_code == 200
        rv = client.get(url_for('book', competition=VALID_COMPETITION_NAME, club=INVALID_CLUB_NAME))
        assert rv.status_code == 302
        assert rv.headers['Location'].endswith('/')

        rv = client.get(rv.location)
        assert rv.status_code == 200
        assert b"No club found with the provided name." in rv.data



