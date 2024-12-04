from locust import HttpUser, TaskSet, task, between
from server import app
from tests.mocks import MOCK_BDD_CLUBS, VALID_EMAIL, UNKNOWN_EMAIL

app.clubs = MOCK_BDD_CLUBS


class ClubBehavior(TaskSet):

    def on_start(self):
        response = self.client.post("/show_summary", data={"email": VALID_EMAIL})
        if response.status_code != 200:
            response.failure("Échec de la connexion")
            return

    @task
    def access_home_page(self):
        with self.client.get("/", catch_response=True) as response:
            if response.status_code != 200:
                response.failure("Échec de l'accès à la page d'accueil")
                return
            response.success()


class WebsiteUser(HttpUser):
    tasks = [ClubBehavior]
    wait_time = between(2, 6)
