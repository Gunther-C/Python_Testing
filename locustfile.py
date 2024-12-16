from locust import HttpUser, TaskSet, task, between
from server import app

from tests.mocks import MOCK_BDD_CLUBS, MOCK_BDD_COMPETITIONS
from tests.mocks import VALID_EMAIL, VALID_CLUB_NAME, CLUB_POINT_15
from tests.mocks import VALID_COMPETITION_NAME, COMPETITION_PLACES_18

app.clubs = MOCK_BDD_CLUBS
app.competitions = MOCK_BDD_COMPETITIONS


class ClubBehavior(TaskSet):

    @task
    def index(self):
        response = self.client.get("/")
        if response.status_code != 200:
            response.failure("Échec de l'accès à la page d'accueil")

    @task
    def show_summary(self):
        response = self.client.post("/show_summary", data={"email": VALID_EMAIL})
        if response.status_code != 200:
            response.failure("Échec de la connexion")

    @task
    def book(self):
        response = self.client.get(f"/book/{VALID_COMPETITION_NAME}/{VALID_CLUB_NAME}")
        if response.status_code != 200:
            response.failure("Échec de l'accès à la page d'accueil")

    @task
    def purchase_places(self):
        response = self.client.post("/purchase_places",
                                    data={
                                         "club": CLUB_POINT_15['name'],
                                         "competition": COMPETITION_PLACES_18['name'],
                                         "places": "1"
                                     })
        if response.status_code != 200:
            response.failure("Échec de l'accès à la page d'accueil")


class WebsiteUser(HttpUser):
    tasks = [ClubBehavior]
    wait_time = between(2, 6)
