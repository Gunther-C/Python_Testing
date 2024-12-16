import pytest
from flask import url_for
from tests.mocks import VALID_CLUB_NAME, CLUBS_LIST_CONTROL


class TestShowClubs:
    """
        Test : endpoint show_clubs
    """
    def test_show_clubs(self, client, mock_clubs):
        """
        Test show_clubs endpoint success.
        :param client:
        :param mock_clubs:
        :return: none
        """
        rv = client.get(url_for('show_clubs'))
        assert rv.status_code == 200
        assert b"Clubs and Points" in rv.data

    def test_show_invalid_club(self, client, mock_invalid_clubs):
        """
        Test redirect on invalid clubs.
        :param client:
        :param mock_invalid_clubs:
        :return: none
        """
        rv = client.get(url_for('show_clubs'))
        assert rv.status_code == 302
        assert rv.headers['Location'].endswith('/')

    def test_clubs_points_display(self, client, mock_clubs):
        """
        Test correct display of club names and points.
        :param client:
        :param mock_clubs:
        :return: none
        """
        rv = client.get(url_for('show_clubs'))
        assert rv.status_code == 200
        assert f"{VALID_CLUB_NAME}".encode() in rv.data
        assert f"{CLUBS_LIST_CONTROL['name']}".encode() in rv.data
        assert f"{CLUBS_LIST_CONTROL['points']}".encode() in rv.data
