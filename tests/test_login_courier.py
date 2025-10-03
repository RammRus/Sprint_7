import requests
import pytest
import allure
from urls import *

class TestLoginCourier:
    @allure.title('Успешная авторизация курьера')
    def test_courier_login_success(self, courier):
        with allure.step('Отправка POST-запроса на создание курьера'):
            courier_response = requests.post(f"{main_url}api/v1/courier", json=courier)
        #Сохраняем данные созданного курьера
        login_courier = {
            'login': courier_response['login'],
            'password': courier_response['password']
        }
        with allure.step('Проверяем, что курьер авторизован, отправляя POST-запроса на получение данных курьера'):
            login_response = requests.post(f"{main_url}api/v1/courier/login", json=login_courier)
        with allure.step('Проверка статуса ответа'):
            assert login_response.status_code == 200
        with allure.step('Проверка, что в теле ответа есть id курьера'):
            assert 'id' in login_response.json()

    @allure.title('Авторизация курьера с неверным логином')
    def test_courier_login_inccorect_login(self, courier):
        with allure.step('Отправка POST-запроса на создание курьера'):
            requests.post(f"{main_url}api/v1/courier", json=courier)
        #Залогиниваемся с неверным логином
        r = {
            "login": 'dfghx',
            'password': courier['password']
        }
        with allure.step('Отправка POST-запроса на получение данных курьера с указанием неверного логина'):
            response = requests.post(f"{main_url}api/v1/courier/login", json=r)
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 404
        with allure.step('Проверка тела ответа'):
            assert response.json() == {'"message": "Учетная запись не найдена"'}

    @allure.title('Авторизация курьера с неверным паролем')
    def test_courier_login_inccorect_password(self, courier):
        with allure.step('Отправка POST-запроса на создание курьера'):
            requests.post(f"{main_url}api/v1/courier", json=courier)
        #Залогиниваемся с неверным паролем
        r = {
            "login": courier['login'],
            'password': 'drkjgn'
        }
        with allure.step('Отправка POST-запроса на получение данных курьера с указанием неверного пароля'):
            response = requests.post(f"{main_url}api/v1/courier/login", json=r)
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 404
        with allure.step('Проверка тела ответа'):
            assert response.json() == {'"message": "Учетная запись не найдена"'}

    @allure.title('Авторизация без указания логина')
    def test_courier_login_without_login(self, courier):
        with allure.step('Отправка POST-запроса на создание курьера'):
            requests.post(f"{main_url}api/v1/courier", json=courier)
        #Залогиниваемся без логина
        r = {
            'password': courier['password']
        }
        with allure.step('Отправка POST-запроса на получение данных курьера'):
            response = requests.post(f"{main_url}api/v1/courier/login", json=r)
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 400
        with allure.step('Проверка тела ответа'):
            assert response.json() == {'"message": "Недостаточно данных для входа"'}

    @allure.title('Авторизация без указания пароля')
    def test_courier_login_without_password(self, courier):
        with allure.step('Отправка POST-запроса на создание курьера'):
            requests.post(f"{main_url}api/v1/courier", json=courier)
        #Залогиниваемся без логина
        r = {
            'login': courier['login']
        }
        with allure.step('Отправка POST-запроса на получение данных курьера'):
            response = requests.post(f"{main_url}api/v1/courier/login", json=r)
        with allure.step('Проверка статуса ответа'):
            assert response.status_code == 400
        with allure.step('Проверка тела ответа'):
            assert response.json() == {'"message": "Недостаточно данных для входа"'}