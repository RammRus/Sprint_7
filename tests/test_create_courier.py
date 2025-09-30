import requests
import pytest
import allure
from conftest import *
from urls import *

class TestCreateCourier:
    @allure.title('Тест на создание курьера')
    def test_create_courier_success(self, courier):
        response = requests.post(f"{main_url}api/v1/courier", json=courier)
        assert response.status_code == 201
        assert response.json() == {'ok': True}

    @allure.title('Тест на создание уже имеющегося курьера')
    def test_create_duplicate_courier(self, courier):
        data = courier()
        #Создаем курьера
        response_1 = requests.post(f"{main_url}api/v1/courier", json=data)
        #Пытаемся создать курьера с уже имеющимися данными
        response_2 = requests.post(f"{main_url}api/v1/courier", json=data)
        assert response_2.status_code == 409
        assert response_2.json() == {'"message": "Этот логин уже используется"'}

    @allure.title('Создание курьера без заполнения логина')
    def test_create_courier_without_login(self):
        response = requests.post(f"{main_url}api/v1/courier", data = {
            "password": generated_password(),
            "firstName": generated_name()
        })
        assert response.status_code == 400
        assert response.json() == {'"message": "Недостаточно данных для создания учетной записи"'}

    @allure.title('Создание курьера без заполнения пароля')
    def test_create_courier_without_password(self):
        response = requests.post(f"{main_url}api/v1/courier", data={
            'login': generated_login(),
            'firstName': generated_name()
        })
        assert response.status_code == 400
        assert response.json() == {'"message": "Недостаточно данных для создания учетной записи"'}
