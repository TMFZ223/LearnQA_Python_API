import requests
class TestCheckHeader:
    def test_check_headers(self):
        response = requests.post("https://playground.learnqa.ru/api/homework_header")     
        # Список ожидаемых заголовков
        expected_headers = ["Date", "Content-Type", "Content-Length", "Connection", "Keep-Alive", "Server", "X-Secret-homework-header", "Cache-Control", "Expires"]
        # Получаем реальные заголовки
        real_result = response.headers
                # Проверяем, содержатся ли ожидаемые заголовки в реальных заголовках
        for header in expected_headers:
            assert header in real_result, f"Expected header '{header}' is missing in the response"
        # Вывод значений проверенных заголовков
        print("Values of the expected headers in the response:")
        for header in expected_headers:
            if header in real_result:
                print(f"{header}: {real_result[header]}")