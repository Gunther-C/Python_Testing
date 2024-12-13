import pytest
from server import app
from tests.mocks import MOCK_BDD_CLUBS, MOCK_BDD_COMPETITIONS
from tests.mocks import COMPETITION_PLACE_1, COMPETITION_PLACES_18
from tests.mocks import CLUB_POINT_1, CLUB_POINTS_15


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
def club_point1():
    original_club1 = CLUB_POINT_1.copy()
    yield CLUB_POINT_1
    CLUB_POINT_1.clear()
    CLUB_POINT_1.update(original_club1)


@pytest.fixture
def mock_competitions():
    app.competitions = MOCK_BDD_COMPETITIONS
    return app.competitions


@pytest.fixture
def competitions_place1():
    original_competition = COMPETITION_PLACE_1.copy()
    yield COMPETITION_PLACE_1
    COMPETITION_PLACE_1.clear()
    COMPETITION_PLACE_1.update(original_competition)


@pytest.fixture
def competitions_places18():
    original_competition = COMPETITION_PLACES_18.copy()
    yield COMPETITION_PLACES_18
    COMPETITION_PLACES_18.clear()
    COMPETITION_PLACES_18.update(original_competition)


@pytest.fixture
def mocks_clubs_competitions(mock_clubs, mock_competitions):
    return
