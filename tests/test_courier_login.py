import json

import allure
import pytest
from client.client import UserAPIClient
from helpers.user_create import Helpers


class TestCourierCreate:

    @allure.title('Курьер может авторизоваться')
    def test_courier_login_happy_pass(self):
        helper = Helpers()
        user = helper.register_new_courier_and_return_login_password()
        payload = {
            'login': user[0],
            'password': user[1]}
        payload_string = json.dumps(payload)
        client = UserAPIClient()
        response = client.post_v1_courier_login(data=payload_string)
        assert response.status_code == 200 and "id" in response.text

    @allure.title('Невозможность авторизации без соответствования требованиям')
    @allure.description('для авторизации нужно передать все обязательные поля;система вернёт ошибку, если неправильно указать логин или пароль;'
                        'если какого-то поля нет, запрос возвращает ошибку;'
                        ' если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;')
    @pytest.mark.parametrize(
        'login,password, code, error',
        [
            ['f15c73d3-f525-42d7-a6ff-6e1e3c262e8b', 'f15c73d3-f525-42d7-a6ff-6e1e3c262e8b', 404, 'Учетная запись не найдена'],
            ['c_0_login', '', 400, 'Недостаточно данных для входа'],
            ['', 'c_0_password', 400, 'Недостаточно данных для входа'],
            ['c_0_login', 'c_0_login22', 404, 'Учетная запись не найдена']
        ]
    )
    def test_courier_login_errors(self, login, password, code, error):
        payload = {
            'login': login,
            'password': password
        }
        payload_string = json.dumps(payload)
        client = UserAPIClient()
        response = client.post_v1_courier_login(data=payload_string)
        assert response.status_code == code and error in response.text