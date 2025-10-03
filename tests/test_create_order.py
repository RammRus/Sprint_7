import pytest
import allure
from data import DataOrder
import requests
from urls import *

class TestCreateOrder:
    @allure.title('Создание заказа с разным указанием цветов самоката')
    @pytest.mark.parametrize(
    "data",
    [
        pytest.param({**DataOrder().data_order(), 'color': ['BLACK']}, id='Черный'),
        pytest.param({**DataOrder().data_order(), 'color': ['GREY']}, id='Серый'),
        pytest.param({**DataOrder().data_order(), 'color': ['BLACK', 'GREY']}, id='Черный и серый'),
        pytest.param({**DataOrder().data_order()}, id='Без цвета')
    ]
)
    def test_create_order_colors(self, data):
        with allure.step('Отправка POST-запроса на создание заказа'):
            response = requests.post(f'{main_url}api/v1/orders', json=data)
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 201
        with allure.step('Проверка, что в теле ответа присутствует "track"'):
            assert 'track' in response.json()