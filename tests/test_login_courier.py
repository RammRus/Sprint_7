import requests
import pytest
import allure

main_url = 'https://qa-scooter.praktikum-services.ru/'

@allure.title('Успешная авторизация курьера')
def test_courier_login_success(courier):
    #Создаем курьера
    courier_response = requests.post(f"{main_url}api/v1/courier", json=courier)
    assert courier_response.status_code == 201
    #Сохраняем данные созданного курьера
    login_courier = {
        'login': courier['login'],
        'password': courier['password']
    }
    #Проверяем авторизацию курьера
    login_response = requests.post(f"{main_url}api/v1/courier/login", json=login_courier)
    assert login_response.status_code == 200
    assert 'id' in login_response.json()

@allure.title('Авторизация курьера с неверным логином')
def test_courier_login_inccorect_login(courier):
    #Создаем курьера
    requests.post(f"{main_url}api/v1/courier", json=courier)
    #Залогиниваемся с неверным логином
    r = {
        "login": 'dfghx',
        'password': courier['password']
    }
    response = requests.post(f"{main_url}api/v1/courier/login", json=r)
    assert response.status_code == 404
    assert response.json() == {'"message": "Учетная запись не найдена"'}

@allure.title('Авторизация курьера с неверным паролем')
def test_courier_login_inccorect_password(courier):
    #Создаем курьера
    requests.post(f"{main_url}api/v1/courier", json=courier)
    #Залогиниваемся с неверным паролем
    r = {
        "login": courier['login'],
        'password': 'drkjgn'
    }
    response = requests.post(f"{main_url}api/v1/courier/login", json=r)
    assert response.status_code == 404
    assert response.json() == {'"message": "Учетная запись не найдена"'}

@allure.title('Авторизация без указания логина')
def test_courier_login_without_login(courier):
    #Создаем курьера
    requests.post(f"{main_url}api/v1/courier", json=courier)
    #Залогиниваемся без логина
    r = {
        'password': courier['password']
    }
    response = requests.post(f"{main_url}api/v1/courier/login", json=r)
    assert response.status_code == 400
    assert response.json() == {'"message": "Недостаточно данных для входа"'}

@allure.title('Авторизация без указания пароля')
def test_courier_login_without_password(courier):
    #Создаем курьера
    requests.post(f"{main_url}api/v1/courier", json=courier)
    #Залогиниваемся без логина
    r = {
        'login': courier['login']
    }
    response = requests.post(f"{main_url}api/v1/courier/login", json=r)
    assert response.status_code == 400
    assert response.json() == {'"message": "Недостаточно данных для входа"'}