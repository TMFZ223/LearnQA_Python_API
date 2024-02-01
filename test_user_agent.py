import pytest
import requests
class TestUserAgent:
    User_agents = [("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", 'Mobile', 'No', 'Android'), ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1", 'Mobile', 'Chrome', 'iOS'), ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", 'Googlebot', 'Unknown', 'Unknown'), ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0", 'Web', 'Chrome', 'No'), ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1", 'Mobile', 'No', 'iPhone')]
    @pytest.mark.parametrize('user_agent, expected_platform, expected_browser, expected_device', User_agents)
    def test_check_user_agents(self, user_agent, expected_platform, expected_browser, expected_device):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        headers = {"User-Agent": user_agent}
        response = requests.get(url, headers=headers)
        actual_result = response.json()
        print(actual_result)
        assert actual_result['platform'] == expected_platform, f"Expected platform '{expected_platform}', but got '{actual_result['platform']}'"
        assert actual_result['browser'] == expected_browser, f"Expected browser '{expected_browser}', but got '{actual_result['browser']}'"
        assert actual_result['device'] == expected_device, f"Expected device '{expected_device}', but got '{actual_result['device']}'"