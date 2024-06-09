from locators.login_page_locators import StellarBurgerRegistrationLocators as RL
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.personal_account_locators import StellarBurgerRestorePersonalAccountPage as PA
from pages.base_page import BasePage


class StellarBurgerPersonalAccountPage(BasePage):
    @allure.step("Клик на кнопку История заказов")
    def click_order_history_button(self):
        self.find_element_with_click(PA.ORDER_HISTORY_BUTTON)


    @allure.step("Клик на кнопку Выйти из аккаунта")
    def click_exit_button(self):
        self.find_element_with_click(PA.EXIT_BUTTON)

    @allure.step("Ждём пока покажется кнопка История заказов")
    def wait_until_history_button_show(self):
        self.wait_until_element_visibility_located(PA.ORDER_HISTORY_BUTTON)

    @allure.step("Получение номера последнего заказа пользователя")
    def get_user_last_order_number(self):
        return self.get_element_text(PA.USER_ORDERS_HISTORY)

    @allure.step("Ждём пока появится последний заказ")
    def wait_until_user_last_order_show(self):
        self.wait_until_element_visibility_located(PA.USER_ORDERS_HISTORY)
