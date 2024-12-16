VALID_CLUB_EMAIL = "club-numero-1@clubs.com"
INVALID_CLUB_EMAIL = "unknown-email@mail.eu"

VALID_CLUB_NAME = "Club 1"
INVALID_CLUB_NAME = "invalid-club-name"

MOCK_CLUB_POINT_1 = [{"name": "Club 1", "email": "club-numero-1@clubs.com", "points": "1"}]
MOCK_CLUB_POINTS_18 = [{"name": "Club 1", "email": "club-numero-1@clubs.com", "points": "18"}]

MOCK_BDD_CLUBS = [
    {
        "name": VALID_CLUB_NAME,
        "email": VALID_CLUB_EMAIL,
        "points": "14"
    },
    {
        "name": "Club 2",
        "email": "club-numero-2@clubs.com",
        "points": "24"
    },
    {
        "name": "Club 3",
        "email": "club-numero-3@clubs.com",
        "points": "34"
    }
]


VALID_COMPETITION_NAME = "La Competition 1"
INVALID_COMPETITION_NAME = "invalid-competition-name"

MOCK_COMPETITION_PLACES_18 = [{"name": "La Competition 1", "date": "2025-10-22 12:30:00", "numberOfPlaces": "18"}]

MOCK_COMPETITION_PLACES_1 = [{"name": "La Competition 1", "date": "2025-10-22 12:30:00", "numberOfPlaces": "1"}]

COMPETITION_INVALID_DATE = {"name": "La Competition 5", "date": "2020-05-22 13:30:00", "numberOfPlaces": "18"}

MOCK_BDD_COMPETITIONS = [
    {
        "name": VALID_COMPETITION_NAME,
        "date": "2025-03-27 10:00:00",
        "numberOfPlaces": "15"
    },
    {
        "name": "La Competition 2",
        "date": "2025-05-22 13:30:00",
        "numberOfPlaces": "7"
    },
    COMPETITION_INVALID_DATE
]



