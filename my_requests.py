import requests

class MyRequests():
    @staticmethod
    def post (url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url, data, headers, cookies, 'POST')
    
    @staticmethod
    def get (url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url, data, headers, cookies, 'GET')
    
    @staticmethod
    def put (url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url, data, headers, cookies, 'PUT')
    
    @staticmethod
    def delete (url: str, data: dict = None, headers: dict = None, cookies: dict = None):
        return MyRequests._send(url, data, headers, cookies, 'DELETE')

    @staticmethod
    def _send(url: str, data: dict, cookies: dict, method: str):

        url = f"https://playground.learnqa.ru/api{url}"

        if headers is None:
            headers = {}
        if cookies is None:
            cookies = {}

        if method == 'GET':
            response= requests.get(url, params=data, headers=headers, cookies=cookies)
        elif method == 'POST':
            response= requests.get(url, data=data, headers=headers, cookies=cookies)
        elif method == 'PUT':
            response= requests.get(url, data=data, headers=headers, cookies=cookies)
        elif method == 'DELETE':
            response= requests.get(url, data=data, headers=headers, cookies=cookies)
        else:
            raise Exception(f"Bad HTTP metohs '{method}' was received")
        
        return response