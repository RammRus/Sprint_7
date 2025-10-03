import requests
import pytest
import allure
from conftest import *
from urls import *

class TestCreateCourier:
    @allure.title('Тест на создание курьера')
    def test_create_courier_success(self, courier):
        with allure.step('Отправка POST-запроса на создание курьера'):
            response = requests.post(f"{main_url}api/v1/courier", json=courier)
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 201
        with allure.step('Проверка тела ответа'):
            assert response.json() == {'ok': True}

    @allure.title('Тест на создание уже имеющегося курьера')
    def test_create_duplicate_courier(self, courier):
        data = courier()
        with allure.step('Отправка POST-запроса на создание курьера с фиксированными данными'):
            response_1 = requests.post(f"{main_url}api/v1/courier", json=data)
        with allure.step('Попытка создания уже имеющегося курьера'):
            response_2 = requests.post(f"{main_url}api/v1/courier", json=data)
        with allure.step('Проверка статуса ответа'):
            assert response_2.status_code == 409
        with allure.step('Проверка тела ответа'):
            assert response_2.json() == {'"message": "Этот логин уже используется"'}

    @allure.title('Создание курьера без заполнения логина')
    def test_create_courier_without_login(self):
        with allure.step('Отправка POST-запроса на создание курьера без указания логина в теле запроса'):
            response = requests.post(f"{main_url}api/v1/courier", data = {
            "password": generated_password(),
            "firstName": generated_name()
        })
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 400
        with allure.step('Проверка тела ответа'):
            assert response.json() == {'"message": "Недостаточно данных для создания учетной записи"'}

    @allure.title('Создание курьера без заполнения пароля')
    def test_create_courier_without_password(self):
        with allure.step('Отправка POST-запроса на создание курьера без указания пароля в теле запроса'):
            response = requests.post(f"{main_url}api/v1/courier", data={
            'login': generated_login(),
            'firstName': generated_name()
        })
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 400
        with allure.step('Проверка тела ответа'):
            assert response.json() == {'"message": "Недостаточно данных для создания учетной записи"'}
