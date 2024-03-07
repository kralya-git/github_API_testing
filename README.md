# Предмет: Управление качеством программных систем
### Задание: протестировать API GitHub


![image](https://github.com/kralya-git/github_API_testing/assets/113534398/e81a70b1-83c6-4fcf-bced-2e2d86c1905f)
Рис.1. результат выполнения теста


Как сделать для своего API?
1. Settings -> Developer Settings -> Personal access tokens -> Tokens (classic) -> Generate new token (classic) -> Note... Expiration... Scopes... Generate token -> Copy token
2. Создать в репозитории файл .env, файл напсать GITHUB_TOKEN=... (вставить скопированный токен)
3. Запустить в консоли командой **pytest** или **pytest test_github_api.py**
