import pytest
from selenium import webdriver
import settings
import allure
from faker import Faker
from data import StellarBurgerTestData as SD
from endpoints.create_user_endpoints import CreateUser

fake = Faker()


@pytest.fixture(params=['firefox', 'chrome'], scope='function')
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.maximize_window()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
        browser.maximize_window()

    browser.get(settings.URL)

    yield browser

    browser.quit()


@allure.step("Создание фейкового пользователя отдельно пароль и email")
@pytest.fixture(scope='function')
def fake_user_required_login_password():
    cu = CreateUser()
    email = fake.email()
    password = fake.password()
    cu.user_creation(data={'email': email, 'password': password, 'name': 'Dmitry'})
    yield email, password

    cu.delete_user(data={'email': email, 'password': password, 'name': 'Dmitry'})
