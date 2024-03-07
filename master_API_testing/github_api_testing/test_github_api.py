import pytest
from github_api_client import GitHubAPIClient, User

@pytest.fixture
def api_client():
    return GitHubAPIClient()

def test_get_user(api_client):
    username = "octocat"  # Изменять имя пользователя тут!!!
    response = api_client.get_user(username)
    assert response.status_code == 200
    user_data = response.json()
    user = User(**user_data)
    assert user.login == username  # Проверяем, что логин в ответе соответствует запрашиваемому

# Запуск - `pytest` в терминале