import pytest
from flask import get_flashed_messages, url_for
from tests.mocks import BDD_CLUBS, BDD_COMPETITIONS
from tests.mocks import VALID_CLUB_NAME, INVALID_CLUB_NAME, VALID_CLUB_EMAIL, INVALID_CLUB_EMAIL
from tests.mocks import LIST_CONTROL_NAME, LIST_CONTROL_POINT
from tests.mocks import VALID_COMPETITION_NAME, INVALID_COMPETITION_NAME


class TestIntegration:

    def test_full_flow_show_clubs_invalid(self, client, mock_invalid_clubs):
        """
        Test redirect on invalid clubs.
        :param client:
        :param mock_invalid_clubs:
        :return: none
        """
        index = client.get(url_for('index'))
        assert index.status_code == 200
        assert "GUDLFT Registration".encode() in index.data

        clubs = client.get(url_for('show_clubs'))
        assert clubs.status_code == 302
        assert clubs.headers['Location'].endswith('/')

        _index = client.get(clubs.location)
        assert _index.status_code == 200
        message = get_flashed_messages()
        assert f"No registered club." in message
        assert b"No registered club." in _index.data

    def test_full_flow_show_clubs(self, client, mock_clubs):
        """
        Test that the summary page displays the correct information
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return: none
        """
        index = client.get(url_for('index'))
        assert index.status_code == 200
        assert "GUDLFT Registration".encode() in index.data

        clubs = client.get(url_for('show_clubs'))
        assert clubs.status_code == 200
        assert b"Clubs and Points" in clubs.data
        assert f"{LIST_CONTROL_NAME}".encode() in clubs.data
        assert f"{LIST_CONTROL_POINT}".encode() in clubs.data

    def test_full_flow(self, client, mock_full_flow):
        """
        Test that simulates the complete user flow from the index page
         to booking and validating a competition registration.
        :param client:
        :param mock_full_flow:
        :return: none
        """
        club = mock_full_flow[0]
        competition = mock_full_flow[1]

        index = client.get(url_for('index'))
        assert index.status_code == 200
        assert "GUDLFT Registration".encode() in index.data

        homepage = client.post(url_for('show_summary'), data={"email": INVALID_CLUB_EMAIL})
        assert homepage.status_code == 302
        assert homepage.headers['Location'].endswith('/')

        _index = client.get(homepage.location)
        assert _index.status_code == 200
        assert b"No club found with the provided email." in _index.data

        _homepage = client.post(url_for('show_summary'), data={'email': club['email']})
        assert _homepage.status_code == 200
        assert f"{club['name']}".encode() in _homepage.data

        book = client.get(url_for('book', competition=competition['name'], club=INVALID_CLUB_NAME))
        assert book.status_code == 302
        assert book.headers['Location'].endswith('/')

        _index = client.get(book.location)
        assert _index.status_code == 200
        assert b"No club found with the provided name." in _index.data

        _book = client.get(url_for('book', competition=competition['name'], club=club['name']))
        assert _book.status_code == 200
        assert f"{club['name']}".encode() in _book.data
        assert f"{competition['name']}".encode() in _book.data

        purchase = client.post(url_for('purchase_places'),
                               data={
                                   "club": INVALID_CLUB_NAME,
                                   "competition": competition['name'],
                                   "places": "1"
                               })
        assert purchase.status_code == 302
        assert purchase.headers['Location'].endswith('/')

        _index = client.get(purchase.location)
        assert _index.status_code == 200
        assert b"No club found with the provided name." in _index.data

        _purchase = client.post(url_for('purchase_places'),
                               data={
                                   "club": club['name'],
                                   "competition": competition['name'],
                                   "places": "1"
                               })
        assert _purchase.status_code == 200
        assert f"{club['name']}".encode() in _purchase.data
        assert int(club['points']) == 0
        assert int(competition['numberOfPlaces']) == 0
        assert b"Great - booking complete! You have booked place(s)." in _purchase.data

        logout = client.get(url_for('logout'))
        assert logout.status_code == 302
        assert logout.headers['Location'].endswith('/')

        _index = client.get(logout.location)
        assert _index.status_code == 200
        assert b"GUDLFT Registration" in _index.data
