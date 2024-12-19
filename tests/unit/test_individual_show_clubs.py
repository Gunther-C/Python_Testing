import pytest
from flask import url_for
from tests.mocks import LIST_CONTROL_NAME, LIST_CONTROL_POINT


class TestIndividualShowClubs:
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
        clubs = client.get(url_for('show_clubs'))
        assert clubs.status_code == 200
        assert b"Clubs and Points" in clubs.data

    def test_show_invalid_club(self, client, mock_invalid_clubs):
        """
        Test redirect on invalid clubs.
        :param client:
        :param mock_invalid_clubs:
        :return: none
        """
        clubs = client.get(url_for('show_clubs'))
        assert clubs.status_code == 302
        assert clubs.headers['Location'].endswith('/')

    def test_clubs_points_display(self, client, mock_clubs):
        """
        Test correct display of club names and points.
        :param client:
        :param mock_clubs:
        :return: none
        """
        clubs = client.get(url_for('show_clubs'))
        assert clubs.status_code == 200
        assert f"{LIST_CONTROL_NAME}".encode() in clubs.data
        assert f"{LIST_CONTROL_POINT}".encode() in clubs.data
