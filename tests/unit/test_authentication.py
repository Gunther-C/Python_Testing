import pytest
from flask import url_for
from server import app
from tests.mocks import MOCK_BDD_CLUBS, VALID_EMAIL, UNKNOWN_EMAIL

app.clubs = MOCK_BDD_CLUBS


class TestAuthentication:
    def test_index(self, request_context, client):
        rv = client.get(url_for('index'))
        assert rv.status_code == 200
        assert "GUDLFT Registration".encode() in rv.data

    def test_show_summary(self, request_context, client):
        rv = client.post(url_for('show_summary'), data={'email': VALID_EMAIL})
        assert rv.status_code == 200
        assert f"{VALID_EMAIL}".encode() in rv.data

    def test_unknown_email(self, request_context, client):
        rv = client.post(url_for('show_summary'), data={"email": UNKNOWN_EMAIL}, follow_redirects=False)
        assert rv.status_code == 302

        with client.session_transaction() as session:
            flashed_messages = session.get('_flashes', [])
            assert any("No club found with the provided email address." in message
                       for category, message in flashed_messages
                       ), "The expected error message was not found."
