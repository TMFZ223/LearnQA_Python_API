import requests
response = requests.get("https://playground.learnqa.ru/api/long_redirect")
print (response.history)
first_response = response.history[0]
second_response = response
print(first_response.url)
print(second_response.url)
print('конечный URL', second_response.url)