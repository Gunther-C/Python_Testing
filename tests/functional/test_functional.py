import pytest
from flask import get_flashed_messages, url_for
from tests.mocks import BDD_CLUBS, BDD_COMPETITIONS
from tests.mocks import VALID_CLUB_NAME, VALID_CLUB_EMAIL, INVALID_CLUB_EMAIL
from tests.mocks import VALID_COMPETITION_NAME, INVALID_COMPETITION_DATE, COMPETITION_ONE_POINT
from server import app, find_entity


class TestFunctional:

    def test_authentication_invalid(self, client):
        """
        Test that an unknown email redirects to the index page and displays an error message
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return: none
        """
        club = find_entity(BDD_CLUBS, INVALID_CLUB_EMAIL, 'club', 'email')
        assert club is None
        message = get_flashed_messages()
        assert "No club found with the provided email." in message

        homepage = client.post(url_for('show_summary'), data={"email": INVALID_CLUB_EMAIL})
        assert homepage.status_code == 302
        assert homepage.headers['Location'].endswith('/')

        index = client.get(homepage.location)
        assert index.status_code == 200
        assert b"No club found with the provided email." in index.data

    def test_book_invalid_date(self, client):
        """
        Test that booking a competition with an invalid date (past competition) displays an error message
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return: none
        """
        club = find_entity(BDD_CLUBS, VALID_CLUB_NAME, 'club', 'name')
        assert club is not None
        app.clubs = [club]

        competition = find_entity(BDD_COMPETITIONS, INVALID_COMPETITION_DATE, 'competition', 'name')
        assert competition is not None
        app.competitions = [competition]

        homepage = client.post(url_for('show_summary'), data={'email': club['email']})
        assert homepage.status_code == 200

        book = client.get(url_for('book', competition=competition['name'], club=club['name']))
        assert book.status_code == 200

        message = get_flashed_messages()
        message_text = f"This competition {competition['name']} has already taken place."
        assert message_text in message
        assert message_text.encode() in book.data

    def test_purchase_point_limit(self, client):
        """
        Test that booking a competition with an invalid date (past competition) displays an error message
        :param client:
        :param mock_clubs:
        :param mock_competitions:
        :return: none
        """
        club = find_entity(BDD_CLUBS, VALID_CLUB_NAME, 'club', 'name')
        assert club is not None
        app.clubs = [club]

        competition = find_entity(BDD_COMPETITIONS, VALID_COMPETITION_NAME, 'competition', 'name')
        assert competition is not None
        app.competitions = [competition]

        homepage = client.post(url_for('show_summary'), data={'email': club['email']})
        assert homepage.status_code == 200

        purchase = client.post(url_for('purchase_places'),
                               data={
                                    "club": club['name'],
                                    "competition": competition['name'],
                                    "places": str(int(club['points']) + 1)
                               })
        assert purchase.status_code == 200
        assert f"{club['name']}".encode() in purchase.data
        assert f"{competition['name']}".encode() in purchase.data
        assert b"Not enough points available." in purchase.data

    def test_purchase_places_limit(self, client, mock_places_limit):
        """
        Test that attempting to purchase more than 12 places displays an error message.
        :param client:
        :param mock_places_limit:
        :return: none
        """
        club = find_entity(BDD_CLUBS, VALID_CLUB_NAME, 'club', 'name')
        assert club is not None
        app.clubs = [club]

        competition = find_entity(BDD_COMPETITIONS, VALID_COMPETITION_NAME, 'competition', 'name')
        assert competition is not None
        app.competitions = [competition]

        purchase = client.post(url_for('purchase_places'),
                               data={
                                   "club": club['name'],
                                   "competition": competition['name'],
                                   "places": "14"
                               })
        assert purchase.status_code == 200
        assert f"{club['name']}".encode() in purchase.data
        assert f"{competition['name']}".encode() in purchase.data
        assert b"Booking limit of 12 places exceeded." in purchase.data

    def test_purchase_insufficient_spots(self, client):
        """
        Test booking more places than available.
        :param client:
        :param mock_competition_places_limit:
        :return: none
        """
        club = find_entity(BDD_CLUBS, VALID_CLUB_NAME, 'club', 'name')
        assert club is not None
        app.clubs = [club]

        competition = find_entity(BDD_COMPETITIONS, COMPETITION_ONE_POINT, 'competition', 'name')
        assert competition is not None
        app.competitions = [competition]

        purchase = client.post(url_for('purchase_places'),
                               data={
                                   "club": club['name'],
                                   "competition": competition['name'],
                                   "places": "2"
                               })
        assert purchase.status_code == 200
        assert f"{club['name']}".encode() in purchase.data
        assert f"{competition['name']}".encode() in purchase.data
        assert f"Booking limit of {competition['numberOfPlaces']} places.".encode() in purchase.data

    def test_show_clubs_empty(self, client, mock_invalid_clubs):
        """
        Test redirect on invalid clubs.
        :param client:
        :param mock_invalid_clubs:
        :return: none
        """
        clubs = client.get(url_for('show_clubs'))
        assert clubs.status_code == 302
        assert clubs.headers['Location'].endswith('/')

        index = client.get(clubs.location)
        assert index.status_code == 200
        message = get_flashed_messages()
        assert f"No registered club." in message
        assert b"No registered club." in index.data
