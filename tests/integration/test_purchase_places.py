import pytest
from flask import url_for
from tests.mocks import VALID_CLUB_NAME, VALID_CLUB_EMAIL, INVALID_CLUB_NAME
from tests.mocks import VALID_COMPETITION_NAME, INVALID_COMPETITION_NAME


class TestPurchasePlace:
    """
        Test : endpoint purchase_places
    """
    def test_purchase_valid(self, client, mock_clubs, mock_competitions):
        """
        Test that a valid purchase of places is successful.
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return: none
        """
        _rv = client.post(url_for('show_summary'), data={'email': VALID_CLUB_EMAIL})
        assert _rv.status_code == 200
        rv = client.get(url_for('book', competition=VALID_COMPETITION_NAME, club=VALID_CLUB_NAME))
        assert rv.status_code == 200
        rv = client.post(url_for('purchase_places'),
                         data={
                             "club": VALID_CLUB_NAME,
                             "competition": VALID_COMPETITION_NAME,
                             "places": "1"
                         })
        assert rv.status_code == 200

    def test_purchase_invalid(self, client, mock_clubs, mock_competitions):
        """
        Test that an invalid purchase of places redirects to the home page with an error message.
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return: none
        """
        _rv = client.post(url_for('show_summary'), data={'email': VALID_CLUB_EMAIL})
        assert _rv.status_code == 200
        rv = client.get(url_for('book', competition=VALID_COMPETITION_NAME, club=VALID_CLUB_NAME))
        assert rv.status_code == 200
        rv = client.post(url_for('purchase_places'),
                         data={
                             "club": INVALID_CLUB_NAME,
                             "competition": VALID_COMPETITION_NAME,
                             "places": "1"
                         })
        assert rv.status_code == 302
        assert rv.headers['Location'].endswith('/')

        rv = client.get(rv.location)
        assert rv.status_code == 200
        assert b"No club found with the provided name." in rv.data



