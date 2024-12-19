import pytest
from flask import get_flashed_messages, url_for
from tests.mocks import BDD_CLUBS, BDD_COMPETITIONS
from tests.mocks import INVALID_CLUB_EMAIL, VALID_CLUB_EMAIL, INVALID_CLUB_NAME, VALID_CLUB_NAME
from tests.mocks import INVALID_COMPETITION_NAME, VALID_COMPETITION_NAME
from server import find_entity


class TestFindEntity:
    """
        Test : fonction find_entity
        Test : message 'flask'
    """

    def test_valid_club_email(self):
        """
        Test finding a club with a valid email.
        :return: none
        """
        club = find_entity(BDD_CLUBS, VALID_CLUB_EMAIL, 'club', 'email')
        assert club is not None

    def test_invalid_club_email(self, request_context):
        """
        Test the error message after an invalid email.
        :param request_context:
        :return: none
        """
        club = find_entity(BDD_CLUBS, INVALID_CLUB_EMAIL, 'club', 'email')
        assert club is None
        message = get_flashed_messages()
        assert "No club found with the provided email." in message

    def test_valid_club_name(self):
        """
        Test finding a club with a valid name.
        :return: none
        """
        club = find_entity(BDD_CLUBS, VALID_CLUB_NAME, 'club', 'name')
        assert club is not None

    def test_invalid_club_name(self, request_context):
        """
        Test the error message after an invalid club name.
        :return: none
        """
        club = find_entity(BDD_CLUBS, INVALID_CLUB_NAME, 'club', 'name')
        assert club is None
        message = get_flashed_messages()
        assert "No club found with the provided name." in message

    def test_valid_competition_name(self):
        """
        Test finding a competition with a valid name.
        :return: none
        """
        competition = find_entity(BDD_COMPETITIONS, VALID_COMPETITION_NAME, 'competition', 'name')
        assert competition is not None

    def test_invalid_competition_name(self, request_context):
        """
        Test the error message after an invalid competition name.
        :return: none
        """
        competition = find_entity(BDD_COMPETITIONS, INVALID_COMPETITION_NAME, 'competition', 'name')
        assert competition is None
        message = get_flashed_messages()
        assert "No competition found with the provided name." in message
