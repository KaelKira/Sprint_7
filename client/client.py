import json

import requests

class UserAPIClient:
    host = 'https://qa-scooter.praktikum-services.ru'
    headers = {"Content-type": "application/json"}

    def post_v1_courier(self, path="/api/v1/courier", data=None):
        url = f"{self.host}{path}"
        return requests.post(url=url, data=data, headers=self.headers)

    def post_v1_courier_login(self, path="/api/v1/courier/login", data=None, header=None):
        if header is None:
            header = self.headers
        url = f"{self.host}{path}"
        return requests.post(url=url,data=data, headers=header)

    def get_v1_orders(self, path="/api/v1/orders"):
        url = f"{self.host}{path}"
        return requests.get(url=url, headers=self.headers)

    def post_v1_orders(self, path="/api/v1/orders", data=None):
        url = f"{self.host}{path}"
        return requests.post(url=url, data=data, headers=self.headers)