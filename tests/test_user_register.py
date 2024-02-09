import pytest
import requests
import allure
from lib.base_case import BaseCase
from lib.assertions import Assertions

@allure.feature('User Registration')  # Общая функциональность, к которой привязаны эти тесты
class TestUserRegister(BaseCase):
    
    @allure.story('Register with Incorrect Email')  # Конкретный сценарий или история
    @allure.severity(allure.severity_level.NORMAL)  # Уровень серьезности
    def test_create_user_with_incorrect_email(self):
        with allure.step("Prepare test data with incorrect email"):
            data = {
                'password': '1234',
                'username': 'learnqa',
                'firstname': 'learnqa',
                'lastname': 'learnqa',
                'email': 'vinkotovexample.com'  # Некорректный email
            }
        
        with allure.step("Send request and verify the response"):
            response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
            Assertions.assert_json_value_by_name(
                response,
                "error",
                "Invalid email format",
                f"Unexpected response content {response.content}"
            )

    @allure.story('Register with Missing Field')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('field', ['password', 'username', 'firstname', 'lastname', 'email'])
    def test_create_user_missing_field(self, field):
        with allure.step(f"Prepare test data without {field}"):
            data = {
                'password': '1234',
                'username': 'learnqa',
                'firstname': 'learnqa',
                'lastname': 'learnqa',
                'email': 'vinkotov@example.com'
            }
            data.pop(field)
        
        with allure.step("Send request and verify the status code is 400"):
            response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
            assert response.status_code == 400, f"Unexpected status code {response.status_code} when missing field {field}"

    @allure.story('Register with Short Name')
    @allure.severity(allure.severity_level.MINOR)
    def test_create_user_with_short_name(self):
        with allure.step("Prepare test data with short username"):
            data = {
                'password': '1234',
                'username': 'l',  # Короткое имя
                'firstname': 'learnqa',
                'lastname': 'learnqa',
                'email': 'vinkotov@example.com'
            }
        
        with allure.step("Send request and verify the status code is 400"):
            response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
            assert response.status_code == 400, f"Unexpected status code {response.status_code}"

    @allure.story('Register with Long Name')
    @allure.severity(allure.severity_level.MINOR)
    def test_create_user_with_long_name(self):
        with allure.step("Prepare test data with very long username"):
            long_name = "l" * 251  # Создаем имя длиннее 250 символов
            data = {
                'password': '1234',
                'username': long_name,
                'firstname': 'learnqa',
                'lastname': 'learnqa',
                'email': 'vinkotov@example.com'
            }
        
        with allure.step("Send request and verify the status code is 400"):
            response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
            assert response.status_code == 400, f"Unexpected status code {response.status_code}"