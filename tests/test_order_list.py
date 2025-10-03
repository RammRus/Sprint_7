import pytest
import allure
import requests
from urls import *

class TestOrderList:
    @allure.title('Проверка списка заказов')
    def test_get_order_list(self):
        with allure.step('Отправка GET-запроса на получение списка заказов'):
            response = requests.get(f"{main_url}api/v1/orders/track")
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 200
        with allure.step('Проверка, что тело ответа содержит "orders"'):
            assert 'orders' in response.json()
        with allure.step('Проверка, что в теле ответа возвращается список'):
            assert isinstance(response.json()['orders'], list)