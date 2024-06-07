import pytest
from selenium import webdriver
import settings
import allure
from faker import Faker
from data import StellarBurgerTestData as SD
from endpoints.create_user_endpoints import CreateUser

fake = Faker()


@pytest.fixture(params=['chrome'], scope='function')
def driver(request):

    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get(settings.URL)

    yield browser

    browser.quit()


@allure.step("Создание фейкового пользователя")
@pytest.fixture(scope='function')
def fake_user():
    cu = CreateUser()
    email = SD.FAKE_USER['email']
    password = SD.FAKE_USER['password']
    name = SD.FAKE_USER['name']
    cu.user_creation(data={'email': email, 'password': password, 'name': name})
    token = cu.token
    yield email, password

    cu.delete_user(data={'email': email, 'password': password, 'name': name}, token = token)
