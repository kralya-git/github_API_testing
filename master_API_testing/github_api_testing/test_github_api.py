import pytest
from github_api_client import GitHubAPIClient, User, Repository
import os

# Функция для загрузки переменных окружения из файла .env
def load_env():
    with open('.env') as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            key, value = line.strip().split('=', 1)
            os.environ[key] = value

load_env()

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

@pytest.fixture
def api_client():
    return GitHubAPIClient()

@pytest.fixture
def new_repo(api_client):
    repo_data = {
        "name": "test-repo",
        "private": True
    }
    response = api_client.create_repo(GITHUB_TOKEN, repo_data)
    assert response.status_code == 201
    repo = Repository(**response.json())
    yield repo
    # После теста удаляем созданный репозиторий
    api_client.delete_repo(GITHUB_TOKEN, repo.owner.login, repo.name)

def test_get_user(api_client):
    username = "kralya-git"
    response = api_client.get_user(username)
    assert response.status_code == 200
    user = User(**response.json())
    assert user.login == username

def test_create_repo(new_repo):
    assert new_repo.name == "test-repo"

def test_update_repo(api_client, new_repo):
    update_data = {
        "name": "new-test-repo-name",
        "private": False
    }
    response = api_client.update_repo(GITHUB_TOKEN, new_repo.owner.login, new_repo.name, update_data)
    assert response.status_code == 200
    updated_repo = Repository(**response.json())
    assert updated_repo.name == update_data['name']

def test_delete_repo(api_client, new_repo):
    response = api_client.delete_repo(GITHUB_TOKEN, new_repo.owner.login, new_repo.name)
    assert response.status_code == 204
