from lib.base_case import BaseCase
from lib.assertions import Assertions
import requests

class TestUserDelete:
    def setup(self):
        # Данные для авторизации
        self.data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        self.base_url = "https://playground.learnqa.ru/api/user"
        
        # Авторизация пользователя
        response = requests.post(f"{self.base_url}/auth", data=self.data)
        assert "auth_sid" in response.cookies, "There is no auth cookie in the response"
        assert "x-csrf-token" in response.headers, "There is no CSRF token header in the response"
        assert "user_id" in response.json(), "There is no user id in the response"
        
        self.auth_sid = response.cookies.get("auth_sid")
        self.token = response.headers.get("x-csrf-token")
        self.user_id = response.json()["user_id"]
        # Попытка удалить пользователя с ID 2
        response = requests.delete(f"{self.base_url}/2",
                                   headers={"x-csrf-token": self.token},
                                   cookies={"auth_sid": self.auth_sid})
        
        # Убедимся, что система не разрешает удаление пользователя с ID 2
        assert response.status_code == 400, f"Unexpected status code {response.status_code}. User was deleted or another error occurred."
    # Второй тест
        def test_create_user_and_delete(self):

                email = "tem6324@example.com"
        data = {
            'username': 'user123',
            'password': '12345',
            'email': email,
            'firstName': 'John',
            'lastName': 'Doe'
        }
        response = requests.post(f"{base_url}", data=data)
        Assertions.assert_code_status(response, 200)
        self.user_id = self.get_json_value(response, "id")

        # Авторизация созданного пользователя
        login_data = {
            'email': email,
            'password': '12345'
        }
        response2 = requests.post(f"{base_url}/login", data=login_data)
        Assertions.assert_code_status(response2, 200)
        self.auth_sid = self.get_cookie(response2, "auth_sid")
        self.token = self.get_header(response2, "x-csrf-token")

        # Удаление пользователя
        response3 = requests.delete(f"https://playground.learnqa.ru/api/user/{self.user_id}",
                                   headers={"x-csrf-token": self.token},
                                   cookies={"auth_sid": self.auth_sid})
        Assertions.assert_code_status(response3, 200)

        # Попытка получить данные удаленного пользователя
        response4 = requests.get(f"https://playground.learnqa.ru/api/user/{self.user_id}",
                                 headers={"x-csrf-token": self.token},
                                 cookies={"auth_sid": self.auth_sid})
        Assertions.assert_code_status(response4, 404)
        assert response4.content.decode("utf-8") == "User not found", "User has not been deleted."