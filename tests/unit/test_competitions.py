import pytest
from flask import url_for
from tests.mocks import MOCK_BDD_COMPETITIONS
from tests.mocks import VALID_CLUB_EMAIL, VALID_CLUB_NAME
from tests.mocks import VALID_COMPETITION_NAME, INVALID_COMPETITION_NAME


class TestCompetitions:
    """
        Test : competitions bdd / json
    """
    def test_show_competitions(self, client, mock_clubs, mock_competitions):
        rv = client.post(url_for('show_summary'), data={"email": VALID_CLUB_EMAIL})
        assert rv.status_code == 200

        assert len(mock_competitions) == len(MOCK_BDD_COMPETITIONS)
        for competition in mock_competitions:
            assert f"{competition['name']}".encode() in rv.data

    def test_book_invalid_competitions(self, client, mock_clubs, mock_competitions):
        rv = client.get(url_for('book', competition=INVALID_COMPETITION_NAME, club=VALID_CLUB_NAME))
        assert rv.status_code == 200

        assert len(mock_competitions) == len(MOCK_BDD_COMPETITIONS)
        for competition in mock_competitions:
            assert f"{competition['name']}".encode() in rv.data

    def test_purchase_competitions(self, client, mock_clubs, mock_competitions):
        rv = client.post(url_for('purchase_places'),
                         data={
                            "club": VALID_CLUB_NAME,
                            "competition": VALID_COMPETITION_NAME,
                            "places": "1"
                        })
        assert rv.status_code == 200
        assert len(mock_competitions) == len(MOCK_BDD_COMPETITIONS)
        for competition in mock_competitions:
            assert f"{competition['name']}".encode() in rv.data

    def test_purchase_invalid_competitions(self, client, mock_clubs, mock_competitions):
        rv = client.post(url_for('purchase_places'),
                         data={
                             "club": VALID_CLUB_NAME,
                             "competition": INVALID_COMPETITION_NAME,
                             "places": "1"
                         })
        assert rv.status_code == 200
        assert len(mock_competitions) == len(MOCK_BDD_COMPETITIONS)
        for competition in mock_competitions:
            assert f"{competition['name']}".encode() in rv.data
