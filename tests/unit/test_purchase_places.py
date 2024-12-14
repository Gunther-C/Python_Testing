
import pytest
from flask import url_for
from tests.mocks import VALID_CLUB_NAME, INVALID_CLUB_NAME
from tests.mocks import VALID_COMPETITION_NAME, INVALID_COMPETITION_NAME


class TestPurchasePlace:
    """
        Test : endpoint purchase_places
    """
    def test_purchase_valid(self, client, mock_update_points):
        """
        Successful validation test of a booking with points update
        :param client:
        :param mocks_purchase_update:
        :return: none
        """
        club = mock_update_points[0]
        competition = mock_update_points[1]
        rv = client.post(url_for('purchase_places'),
                         data={
                             "club": club['name'],
                             "competition": competition['name'],
                             "places": "1"
                         })
        assert rv.status_code == 200
        assert int(club['points']) == 0
        assert f"{club['name']}".encode() in rv.data
        assert b"Great - booking complete! You have booked place(s)." in rv.data

    def test_purchase_invalid_club(self, client, mock_clubs, mock_competitions):
        """
        Club Error Redirection Test
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return: none
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

    def test_purchase_invalid_competition(self, client, mock_clubs, mock_competitions):
        """
        Competition Error Redirection Test
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return: none
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

    def test_purchase_point_limit(self, client, mock_insufficient_points):
        """
        Test the club cannot spend more points than it has
        :param client:
        :param mock_insufficient_points:
        :return: none
        """
        club = mock_insufficient_points[0]
        competition = mock_insufficient_points[1]
        rv = client.post(url_for('purchase_places'),
                         data={
                            "club": club['name'],
                            "competition": competition['name'],
                            "places": str(int(club['points']) + 1)
                        })
        assert rv.status_code == 200
        assert f"{club['name']}".encode() in rv.data
        assert f"{competition['name']}".encode() in rv.data
        assert b"Not enough points available." in rv.data
