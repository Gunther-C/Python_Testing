import pytest
from flask import url_for


class TestIndividualLogout:
    """
        Test : endpoint logout
    """
    def test_individual_logout(self, client):
        """
        Test the logout functionality
        :param client:
        :return: none
        """
        logout = client.get(url_for('logout'))
        assert logout.status_code == 302
        assert logout.headers['Location'].endswith('/')
