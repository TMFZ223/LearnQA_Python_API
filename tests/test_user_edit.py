from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # REGISTER  
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        #LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #EDIT
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"fisrtName": new_name}
        )

        Assertions.assert_code_status_code(response3, 200)

        #GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_json_value_by_name(
            response4,
            "fisrtsName",
            new_name,
            "Wrong name of the user after edit"
        )
    # Попытка изменить данные пользователя, будучи неавторизованными
def test_edit_user_without_authorization(self):
    new_name = "New Name"
    response = MyRequests.put(
        "/user/2",
        data={"firstName": new_name}
    )
    Assertions.assert_code_status(response, 400)

# Попытка изменить email пользователя на новый email без символа @
def test_edit_user_email_without_at_symbol(self):
    new_email = "testemail.com"
    response = MyRequests.put(
        f"/user/{user_id}",
        headers={"x-csrf-token": token},
        cookies={"auth_sid": auth_sid},
        data={"email": new_email}
    )
    Assertions.assert_code_status(response, 400)  # Предполагаемый код ошибки для невалидного email

# Попытка изменить firstName пользователя на очень короткое значение в один символ
def test_edit_user_firstname_to_one_char(self):
    new_first_name = "A"
    response = MyRequests.put(
        f"/user/{user_id}",
        headers={"x-csrf-token": token},
        cookies={"auth_sid": auth_sid},
        data={"firstName": new_first_name}
    )
    Assertions.assert_code_status(response, 400)