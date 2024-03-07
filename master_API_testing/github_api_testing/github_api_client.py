import httpx
from pydantic import BaseModel

class User(BaseModel):
    login: str
    id: int
    avatar_url: str

class Repository(BaseModel):
    id: int
    name: str
    full_name: str
    private: bool
    owner: User

class GitHubAPIClient:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.session = httpx.Client()

    def get_user(self, username):
        response = self.session.get(f"{self.base_url}/users/{username}")
        return response

    def create_repo(self, token, data):
        headers = {"Authorization": f"token {token}"}
        response = self.session.post(f"{self.base_url}/user/repos", json=data, headers=headers)
        return response

    def update_repo(self, token, username, repo_name, data):
        headers = {"Authorization": f"token {token}"}
        response = self.session.patch(f"{self.base_url}/repos/{username}/{repo_name}", json=data, headers=headers)
        return response

    def delete_repo(self, token, username, repo_name):
        headers = {"Authorization": f"token {token}"}
        response = self.session.delete(f"{self.base_url}/repos/{username}/{repo_name}", headers=headers)
        return response
