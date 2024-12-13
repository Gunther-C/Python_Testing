
import pytest
from flask import url_for
from tests.mocks import VALID_CLUB_NAME, INVALID_CLUB_NAME
from tests.mocks import VALID_COMPETITION_NAME, INVALID_COMPETITION_NAME


class TestPurchasePlace:
    """
        Test : endpoint purchase_places
    """
    def test_purchase_valid(self, client, mocks_clubs_competitions, competitions_places18, club_point1):
        """
        :param client:
        :param mocks_clubs_competitions:
        :param competitions_places18:
        :param club_point1:
        :return: Successful validation test of a booking with points update
        """
        rv = client.post(url_for('purchase_places'),
                         data={
                             "club": club_point1['name'],
                             "competition": competitions_places18['name'],
                             "places": "1"
                         })
        assert rv.status_code == 200
        assert int(club_point1['points']) == 0
        assert f"{club_point1['name']}".encode() in rv.data
        assert b"Great - booking complete! You have booked place(s)." in rv.data

    def test_purchase_invalid_club(self, client, mocks_clubs_competitions):
        """
        :param client:
        :param mocks_clubs_competitions:
        :return: Club Error Redirection Test
        """
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

    def test_purchase_invalid_competition(self, client, mocks_clubs_competitions):
        """
        :param client:
        :param mocks_clubs_competitions:
        :return: Competition Error Redirection Test
        """
        rv = client.post(url_for('purchase_places'),
                         data={
                             "club": VALID_CLUB_NAME,
                             "competition": INVALID_COMPETITION_NAME,
                             "places": "1"
                         })
        assert rv.status_code == 200
        assert f"{VALID_CLUB_NAME}".encode() in rv.data
        assert b"No competition found with the provided name." in rv.data

    def test_purchase_point_limit(self, client, mocks_clubs_competitions, competitions_places18, club_point1):
        """
        :param client:
        :param mocks_clubs_competitions:
        :param competitions_places18:
        :param club_point1:
        :return: Test the club cannot spend more points than it has
        """
        rv = client.post(url_for('purchase_places'),
                         data={
                            "club": club_point1['name'],
                            "competition": competitions_places18['name'],
                            "places": str(int(club_point1['points']) + 1)
                        })
        assert rv.status_code == 200
        assert f"{club_point1['name']}".encode() in rv.data
        assert f"{competitions_places18['name']}".encode() in rv.data
        assert b"Not enough points available." in rv.data
