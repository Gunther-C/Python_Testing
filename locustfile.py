from locust import HttpUser, TaskSet, task, between
from server import app

from locust_mocks import BDD_CLUBS, BDD_COMPETITIONS
from locust_mocks import VALID_CLUB_EMAIL, VALID_CLUB_NAME, VALID_COMPETITION_NAME

app.clubs = BDD_CLUBS
app.competitions = BDD_COMPETITIONS


class ClubBehavior(TaskSet):

    @task
    def index(self):
        response = self.client.get("/")
        if response.status_code != 200:
            response.failure("Échec de l'accès à la page d'accueil")

    @task
    def show_clubs(self):
        response = self.client.get("/show_clubs")
        if response.status_code != 200:
            response.failure("Échec de la liste des clubs")

    @task
    def show_summary(self):
        response = self.client.post("/show_summary", data={"email": VALID_CLUB_EMAIL})
        if response.status_code != 200:
            response.failure("Échec de la connexion")

    @task
    def book(self):
        response = self.client.get(f"/book/{VALID_COMPETITION_NAME}/{VALID_CLUB_NAME}")
        if response.status_code != 200:
            response.failure("Échec choix d'une competition")

    @task
    def purchase_places(self):
        response = self.client.post("/purchase_places",
                                    data={
                                         "club": VALID_CLUB_NAME,
                                         "competition": VALID_COMPETITION_NAME,
                                         "places": "1"
                                     })
        if response.status_code != 200:
            response.failure("Échec de l'achat d'une place de competition")


class WebsiteUser(HttpUser):
    tasks = [ClubBehavior]
    wait_time = between(2, 6)
