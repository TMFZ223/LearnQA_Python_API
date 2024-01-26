import time
import requests

# Создание задачи
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
token = response.json()['token']
seconds = response.json()['seconds']

# Выполнение запроса до того, как задача готова
payload = {"token": token}
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params = payload)
assert response.json()['status'] == 'Job is NOT ready', "задача не готова"

# Ожидание
time.sleep(seconds)

# Выполнение запроса после того, как задача готова
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params = payload)
assert response.json()['status'] == 'Job is ready', "Задача готова"
assert 'result' in response.json(), "Наличие поля Result"
print(response.text)
print("Тест пройден")