import pytest
from faker import Faker

fake = Faker()

def generated_login(): #Генерация логина 
    generating_login = fake.user_name()
    return generating_login

def generated_password(): #Генерация пароля
    generating_password = fake.random_number(5)
    return generating_password

def generated_name(): #Генерация имени
    generating_name = fake.first_name()
    return generating_name

@pytest.fixture
def courier(): #Создание курьера
    return {
        'login': generated_login(),
        'password': generated_password(),
        'firstName': generated_name()
    }