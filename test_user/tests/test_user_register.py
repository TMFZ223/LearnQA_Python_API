import pytest
import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):
    
    # Создание пользователя с некорректным email - без символа @
    def test_create_user_with_incorrect_email(self):
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstname': 'learnqa',
            'lastname': 'learnqa',
            'email': 'vinkotovexample.com'  # Некорректный email
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_json_value_by_name(
            response,
            "error",
            "Invalid email format",
            f"Unexpected response content {response.content}"
        )

    # Создание пользователя без указания одного из полей
    @pytest.mark.parametrize('field', ['password', 'username', 'firstname', 'lastname', 'email'])
    def test_create_user_missing_field(self, field):
        data = {
            'password': '1234',
            'username': 'learnqa',
            'firstname': 'learnqa',
            'lastname': 'learnqa',
            'email': 'vinkotov@example.com'
        }
        data.pop(field)

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.status_code == 400, f"Unexpected status code {response.status_code} when missing field {field}"

    # Создание пользователя с очень коротким именем в один символ
    def test_create_user_with_short_name(self):
        data = {
            'password': '1234',
            'username': 'l',  # Короткое имя
            'firstname': 'learnqa',
            'lastname': 'learnqa',
            'email': 'vinkotov@example.com'
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.status_code == 400, f"Unexpected status code {response.status_code}"

    # Создание пользователя с очень длинным именем - длиннее 250 символов.
    def test_create_user_with_long_name(self):
        long_name = "l" * 251  # Создаем имя длиннее 250 символов
        data = {
            'password': '1234',
            'username': long_name,
            'firstname': 'learnqa',
            'lastname': 'learnqa',
            'email': 'vinkotov@example.com'
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.status_code == 400, f"Unexpected status code {response.status_code}"