VALID_CLUB_EMAIL = "club-numero-1@clubs.com"
INVALID_CLUB_EMAIL = "unknown-email@mail.eu"

VALID_CLUB_NAME = "Club 1"
INVALID_CLUB_NAME = "invalid-club-name"

VALID_COMPETITION_NAME = "La Competition 1"
INVALID_COMPETITION_NAME = "invalid-competition-name"

CLUB_POINT_1 = {
        "name": "Club 4",
        "email": "club-numero-4@clubs.com",
        "points": "1"
    }

CLUB_POINTS_15 = {
        "name": "Club 5",
        "email": "club-numero-5@clubs.com",
        "points": "15"
    }


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
    },
    CLUB_POINT_1,
    CLUB_POINTS_15
]

COMPETITION_PLACE_1 = {
        "name": "La Competition 3",
        "date": "2025-07-22 12:30:00",
        "numberOfPlaces": "1"
    }

COMPETITION_PLACES_18 = {
        "name": "La Competition 4",
        "date": "2025-10-22 12:30:00",
        "numberOfPlaces": "18"
    }

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
    COMPETITION_PLACE_1,
    COMPETITION_PLACES_18
]
