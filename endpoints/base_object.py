import requests
import settings
import allure


class BaseObject:
    response = None

    @allure.step('Удаление пользователя')
    def delete_user(self, data):
        self.response = requests.delete(settings.URL_USER_DELETE, json=data)