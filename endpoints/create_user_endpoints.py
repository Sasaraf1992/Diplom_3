import requests
import settings
from endpoints.base_object import BaseObject
import allure


class CreateUser(BaseObject):
    @allure.step('Создание пользователя')
    def user_creation(self, data):
        self.response = requests.post(settings.URL_USER_CREATION, json = data)