import requests
#Написание запросов без использования параметров
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)

#Написание запроса Head
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)

#Написание корректных запросов
payload = {"method": "GET"}
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params = payload)
print(response.text)
#Написание корректного запроса POST
payload = {"method": "POST"}
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data = payload)
print(response.text)
#Написание корректного запроса PUT
payload = {"method": "PUT"}
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data = payload)
print(response.text)
#Написание корректного запроса DELETE
payload = {"method": "DELETE"}
response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data = payload)
print(response.text)

#Написание запросов с помощью циклов
http_methods = ['get', 'post', 'put', 'delete']
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
for http_method in http_methods:
    if http_method == 'get':
        response = requests.request(http_method, url, params = {"method": "GET"})
    elif http_method == 'post':
        response = requests.request(http_method, url, data = {"method": "POST"})
    elif http_method == 'put':
        response = requests.request(http_method, url, data = {"method": "PUT"})
    elif http_method == 'delete':
        response = requests.request(http_method, url, data = {"method": "DELETE"})
    print(response.text)
    
    #Тесты на проверку соответствия значений методам
    #Тест на проверку метода get и значения POST
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params = {"method": "POST"})
if response.text == 'Wrong method provided':
    print(response.text)
else:
    print(response.text)
    print('Значение не должно соответствовать методу')

    #Тест на проверку метода get и значения PUT
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params = {"method": "PUT"})
if response.text == 'Wrong method provided':
    print(response.text)
else:
    print(response.text)
    print('Значение не должно соответствовать методу')

    #Тест на проверку метода get и значения DELETE
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params = {"method": "DELETE"})
if response.text == 'Wrong method provided':
    print(response.text)
else:
    print(response.text)
    print('Значение не должно соответствовать методу')
    
        #Тест на проверку метода post и значения GET
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {"method": "GET"})
if response.text == 'Wrong method provided':
    print(response.text)
else:
    print(response.text)
    print('Значение не должно соответствовать методу')

    #Тест на проверку метода post и значения PUT
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {"method": "PUT"})
if response.text == 'Wrong method provided':
    print(response.text)
else:
    print(response.text)
    print('Значение не должно соответствовать методу')

    #Тест на проверку метода post и значения DELETE
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {"method": "DELETE"})
if response.text == 'Wrong method provided':
    print(response.text)
else:
    print(response.text)
    print('Значение не должно соответствовать методу')
    
    #Тест на проверку метода put и значения GET
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {"method": "GET"})
if response.text == 'Wrong method provided':
    print(response.text)
else:
    print(response.text)
    print('Значение не должно соответствовать методу')

    #Тест на проверку метода put и значения POST
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {"method": "POST"})
if response.text == 'Wrong method provided':
    print(response.text)
else:
    print(response.text)
    print('Значение не соответсвует методу')

    #Тест на проверку метода put и значения DELETE
response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {"method": "DELETE"})
if response.text == 'Wrong method provided':
    print(response.text)
else:
    print(response.text)
    print('Значение не соответсвует методу')
    
        #Тест на проверку метода delete и значения GET
response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {"method": "GET"})
if response.text == 'Wrong method provided':
    print(response.text)
else:
    print(response.text)
    print('Значение не должно соответствовать методу')

    #Тест на проверку метода delete и значения POST
response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {"method": "POST"})
if response.text == 'Wrong method provided':
    print(response.text)
else:
    print(response.text)
    print('Значение не соответсвует методу')

    #Тест на проверку метода delete и значения PUT
response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data = {"method": "PUT"})
if response.text == 'Wrong method provided':
    print(response.text)
else:
    print(response.text)
    print('Значение не соответсвует методу')