import pytest
from flask import get_flashed_messages, url_for
from tests.mocks import VALID_CLUB_NAME, VALID_CLUB_EMAIL, INVALID_CLUB_EMAIL


class TestFunctionalLogout:
    """
        Test : endpoint logout
    """
    def test_functional_logout(self, client):
        """
        Test the logout functionality
        :param client:
        :return: none
        """
        logout = client.get(url_for('logout'))
        assert logout.status_code == 302
        assert logout.headers['Location'].endswith('/')
