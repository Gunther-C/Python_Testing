import pytest
from server import app


@pytest.fixture
def request_context():
    with app.test_request_context():
        yield


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        with app.app_context():
            yield client
