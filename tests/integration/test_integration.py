import pytest
from flask import url_for
from tests.mocks import VALID_CLUB_NAME, INVALID_CLUB_NAME, VALID_CLUB_EMAIL, INVALID_CLUB_EMAIL


class TestIntegration:

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

        homepage = client.post(url_for('show_summary'), data={"email": INVALID_CLUB_EMAIL})
        assert homepage.status_code == 302
        assert homepage.headers['Location'].endswith('/')

        _index = client.get(homepage.location)
        assert _index.status_code == 200

        _homepage = client.post(url_for('show_summary'), data={'email': club['email']})
        assert _homepage.status_code == 200

        book = client.get(url_for('book', competition=competition['name'], club=INVALID_CLUB_NAME))
        assert book.status_code == 302
        assert book.headers['Location'].endswith('/')

        _index = client.get(book.location)
        assert _index.status_code == 200

        _book = client.get(url_for('book', competition=competition['name'], club=club['name']))
        assert _book.status_code == 200

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

        _purchase = client.post(url_for('purchase_places'),
                                data={
                                    "club": club['name'],
                                    "competition": competition['name'],
                                    "places": "1"
                                })
        assert _purchase.status_code == 200

        logout = client.get(url_for('logout'))
        assert logout.status_code == 302
        assert logout.headers['Location'].endswith('/')

        _index = client.get(logout.location)
        assert _index.status_code == 200
