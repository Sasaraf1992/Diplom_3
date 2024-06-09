import requests
import settings
from endpoints.base_object import BaseObject
import allure


class CreateUser(BaseObject):
    @allure.step('Создание пользователя')
    def user_creation(self, data):
        self.response = requests.post(settings.URL_USER_CREATION, json = data)
        self.response_json = self.response.json()
        self.token = self.response_json.get('accessToken')
    @allure.step('Удаление пользователя')
    def delete_user(self, data, token):
        self.response = requests.delete(settings.URL_USER_DELETE, json = data,  headers={'Authorization': f'{token}'})