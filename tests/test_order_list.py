import pytest
import allure
import requests
from urls import *

@allure.title('Проверка списка заказов')
def test_get_order_list():
    response = requests.get(f"{main_url}api/v1/orders/track")
    assert response.status_code == 200
    assert 'orders' in response.json()
    assert isinstance(response.json()['orders'], list)