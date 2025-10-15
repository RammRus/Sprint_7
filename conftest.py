import pytest
from generation import *

@pytest.fixture
def courier(): #Создание курьера
    return {
        'login': generated_login(),
        'password': generated_password(),
        'firstName': generated_name()
    }