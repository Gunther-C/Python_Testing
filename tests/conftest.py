import pytest
from server import app
from tests.mocks import MOCK_BDD_CLUBS, MOCK_BDD_COMPETITIONS
from tests.mocks import MOCK_INSUFFICIENT_POINT, MOCK_UPDATE_POINT
from tests.mocks import MOCK_PLACES_LIMIT, MOCK_COMPETITION_PLACES_LIMIT
from tests.mocks import MOCK_FULL_FLOW


@pytest.fixture
def request_context():
    with app.app_context():
        with app.test_request_context():
            yield


@pytest.fixture
def client(request_context):
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        yield client


@pytest.fixture
def mock_clubs():
    app.clubs = MOCK_BDD_CLUBS
    return app.clubs


@pytest.fixture
def mock_invalid_clubs():
    app.clubs = []
    return app.clubs


@pytest.fixture
def mock_competitions():
    app.competitions = MOCK_BDD_COMPETITIONS
    return app.competitions


@pytest.fixture
def mock_insufficient_points():
    app.clubs = [MOCK_INSUFFICIENT_POINT[0]]
    app.competitions = [MOCK_INSUFFICIENT_POINT[1]]
    return app.clubs[0], app.competitions[0]


@pytest.fixture
def mock_update_points():
    app.clubs = [MOCK_UPDATE_POINT[0]]
    app.competitions = [MOCK_UPDATE_POINT[1]]
    return app.clubs[0], app.competitions[0]


@pytest.fixture
def mock_places_limit():
    app.clubs = [MOCK_PLACES_LIMIT[0]]
    app.competitions = [MOCK_PLACES_LIMIT[1]]
    return app.clubs[0], app.competitions[0]


@pytest.fixture
def mock_competition_places_limit():
    app.clubs = [MOCK_COMPETITION_PLACES_LIMIT[0]]
    app.competitions = [MOCK_COMPETITION_PLACES_LIMIT[1]]
    return app.clubs[0], app.competitions[0]


@pytest.fixture
def mock_full_flow():
    app.clubs = [MOCK_FULL_FLOW[0]]
    app.competitions = [MOCK_FULL_FLOW[1]]
    return app.clubs[0], app.competitions[0]
