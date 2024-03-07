import httpx
from pydantic import BaseModel

class User(BaseModel):
    login: str
    id: int
    node_id: str
    # добавьте другие поля по необходимости

class GitHubAPIClient:
    def __init__(self, base_url="https://api.github.com"):
        self.base_url = base_url
        self.session = httpx.Client()

    def get_user(self, username):
        response = self.session.get(f"{self.base_url}/users/{username}")
        return response
