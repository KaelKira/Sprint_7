import requests
import data


class UserAPIClient:
    host = data.HOST
    headers = {"Content-type": "application/json"}

    def post_v1_courier(self, data=None):
        url = f"{self.host}/api/v1/courier"
        return requests.post(url=url, data=data, headers=self.headers)

    def post_v1_courier_login(self, data=None, header=None):
        if header is None:
            header = self.headers
        url = f"{self.host}/api/v1/courier/login"
        return requests.post(url=url,data=data, headers=header)

    def get_v1_orders(self, courier_id=None):
        url = f"{self.host}/api/v1/orders"
        if courier_id:
            url = f"{self.host}/api/v1/orders/?courierId={courier_id}"
        return requests.get(url=url, headers=self.headers)

    def post_v1_orders(self, data=None):
        url = f"{self.host}/api/v1/orders"
        return requests.post(url=url, data=data, headers=self.headers)

    def delete_v1_courier(self, courier_id=None):
        url = f"{self.host}/api/v1/courier/?courierId={courier_id}"
        return requests.delete(url=url)