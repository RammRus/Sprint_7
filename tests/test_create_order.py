import pytest
import allure
from data import DataOrder
import requests
from urls import *

class TestCreateOrder:
    @allure.title('Создание заказа с разным указанием цветов самоката')
    @pytest.mark.parametrize("colors", [
        (["BLACK"]), #Черный
        (["GREY"]), #Серый
        (["BLACK", "GREY"]), #Черный и серый
        ([]) #Без цвета
    ])
    def test_create_order_colors(self, colors):
        data = DataOrder().data_order()
        if colors:
            data['color'] = colors
        else:
            data.pop('color', None)

        response = requests.post(f'{main_url}api/v1/orders')
        assert response.status_code == 201
        assert 'track' in response.json()