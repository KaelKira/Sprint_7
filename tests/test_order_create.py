import json
import allure
import pytest
from client.client import UserAPIClient
from data import order_data_black, order_data_grey, order_data_multicolor, order_data_no_color


class TestCreateOrder:

    @allure.title('Создание заказа')
    @allure.description('можно указать один из цветов — BLACK или GREY; можно указать оба цвета; '
                        'можно совсем не указывать цвет; тело ответа содержит track.')
    @pytest.mark.parametrize('color', [order_data_black, order_data_grey, order_data_multicolor, order_data_no_color])
    def test_create_order_with_color_field_success(self, color):
        client = UserAPIClient()
        payload_string = json.dumps(color)
        response = client.post_v1_orders(data=payload_string)
        assert response.status_code == 201 and 'track' in response.json()