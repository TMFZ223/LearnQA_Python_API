import requests
import json
class TestCheckCookie:
    def test_check_cookies(self):
        response = requests.post("https://playground.learnqa.ru/api/homework_cookie")
        expected_result = '{"HomeWork": "hw_value"}'
        real_result = json.dumps(response.cookies.get_dict())
        print('real result =', real_result)
        print('expected result =', expected_result)
        assert real_result == expected_result, "cookie mismatch"