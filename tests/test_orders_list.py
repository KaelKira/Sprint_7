import allure
from client.client import UserAPIClient
from helpers.user_create import Helpers


class TestOrdersList:

    @allure.title('Список заказов')
    @allure.description('Проверка что тело ответа для нового курьера возвращает пустой список заказов')
    def test_empty_orders_list(self):
        helper = Helpers()
        courier_id = helper.get_courier_id()[2]
        client = UserAPIClient()
        response = client.get_v1_orders(f'/api/v1/orders?courierId={courier_id}')
        assert response.status_code == 200 and response.json()['orders'] == []