import json

import allure
import pytest

from client.client import UserAPIClient
from helpers.user_create import Helpers


class TestCourierCreate:

    @allure.title('Успешное создание курьера')
    def test_courier_create_happy_pass(self):
        helper = Helpers()
        login = helper.generate_random_string(10)
        password = helper.generate_random_string(10)
        payload = {
            'login': login,
            'password': password
        }
        payload_string = json.dumps(payload)
        client = UserAPIClient()
        response = client.post_v1_courier(data=payload_string)
        assert response.status_code == 201 and '{"ok":true}' == response.text

    @allure.title('Не успешное создание курьера')
    @allure.description('если одного из полей нет, запрос возвращает ошибку; '
                        'если создать пользователя с логином, который уже есть, возвращается ошибка.')
    @pytest.mark.parametrize(
        'login,password, error',
        [
            ['c_0_login', 'c_0_login', 409],
            ['c_0_login', '', 400],
            ['', 'c_0_password', 400]
        ]
    )
    def test_courier_create_with_errors(self, login, password, error):
        payload = {
            'login': login,
            'password': password
        }
        payload_string = json.dumps(payload)
        client = UserAPIClient()
        response = client.post_v1_courier(data=payload_string)
        assert response.status_code == error