
VALID_CLUB_NAME = "Club 1"
VALID_CLUB_EMAIL = "club-numero-1@clubs.com"

INVALID_CLUB_NAME = "invalid-club-name"
INVALID_CLUB_EMAIL = "unknown-email@mail.eu"

LIST_CONTROL_NAME = "Club Control"
LIST_CONTROL_POINT = "10"


VALID_COMPETITION_NAME = "La Competition 1"
INVALID_COMPETITION_NAME = "invalid-competition-name"

INVALID_COMPETITION_DATE = "Competition invalid date"
COMPETITION_ONE_POINT = "Competition 1 point"


BDD_CLUBS = [
    {
        "name": VALID_CLUB_NAME,
        "email": VALID_CLUB_EMAIL,
        "points": "15"
    },
    {
        "name": "Club 2",
        "email": "club-numero-2@clubs.com",
        "points": "15"
    },
    {
        "name": LIST_CONTROL_NAME,
        "email": "club-numero-3@clubs.com",
        "points": LIST_CONTROL_POINT
    },
    {
        "name": "Club 4",
        "email": "club-numero-4@clubs.com",
        "points": "15"
    }
]

BDD_COMPETITIONS = [
    {
        "name": VALID_COMPETITION_NAME,
        "date": "2025-03-27 10:00:00",
        "numberOfPlaces": "15"
    },
    {
        "name": "La Competition 2",
        "date": "2025-05-22 13:30:00",
        "numberOfPlaces": "15"
    },
    {
        "name": INVALID_COMPETITION_DATE,
        "date": "2020-05-22 13:30:00",
        "numberOfPlaces": "15"
    },
    {
        "name": COMPETITION_ONE_POINT,
        "date": "2025-05-22 13:30:00",
        "numberOfPlaces": "1"
    }
]


MOCK_INSUFFICIENT_POINT = [
    {"name": "Club 1 point", "email": "club-point-1@clubs.com", "points": "1"},
    {"name": "Competition 18 place", "date": "2025-10-22 12:30:00", "numberOfPlaces": "18"}
]

MOCK_UPDATE_POINT = [
    {"name": "Club 1 point", "email": "club-point-1@clubs.com", "points": "1"},
    {"name": "Competition une place", "date": "2025-10-22 12:30:00", "numberOfPlaces": "1"}
]

MOCK_PLACES_LIMIT = [
    {"name": "Club 18 points", "email": "club-numero-18@clubs.com", "points": "18"},
    {"name": "Competition 18 place", "date": "2025-10-22 12:30:00", "numberOfPlaces": "18"}
]

MOCK_COMPETITION_PLACES_LIMIT = [
    {"name": "Club 18 points", "email": "club-numero-18@clubs.com", "points": "18"},
    {"name": "Competition une place", "date": "2025-10-22 12:30:00", "numberOfPlaces": "1"}
]

MOCK_FULL_FLOW = [
    {"name": "Club 1 point", "email": "club-point-1@clubs.com", "points": "1"},
    {"name": "Competition une place", "date": "2025-10-22 12:30:00", "numberOfPlaces": "1"}
]

MOCK_BDD_CLUBS = [
    {
        "name": "Club 1",
        "email": "club-numero-1@clubs.com",
        "points": "15"
    },
    {
        "name": "Club 2",
        "email": "club-numero-2@clubs.com",
        "points": "15"
    },
    {
        "name": "Club Control",
        "email": "club-numero-3@clubs.com",
        "points": "10"
    },
    {
        "name": "Club 4",
        "email": "club-numero-4@clubs.com",
        "points": "15"
    }
]

MOCK_BDD_COMPETITIONS = [
    {
        "name": "La Competition 1",
        "date": "2025-03-27 10:00:00",
        "numberOfPlaces": "15"
    },
    {
        "name": "La Competition 2",
        "date": "2025-05-22 13:30:00",
        "numberOfPlaces": "15"
    },
    {
        "name": "Competition invalid date",
        "date": "2020-05-22 13:30:00",
        "numberOfPlaces": "15"
    },
    {
        "name": "Competition 1 point",
        "date": "2025-05-22 13:30:00",
        "numberOfPlaces": "1"
    }
]



