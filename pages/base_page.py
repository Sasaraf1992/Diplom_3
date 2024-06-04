import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import StellarBurgerBasePageLocators as BP
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Клик на кнопку 'Личный кабинет'")
    def click_account_button_in_header(self):
        self.driver.find_element(*BP.PERSONAL_ACCOUNT_BUTTON).click()

    @staticmethod
    def time_to_wait(sleep):
        time.sleep(sleep)

    @allure.step("Ждать, пока url не будет содержать")
    def wait_until_url_contains(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_contains(url))

    @allure.step("Клик на кнопку Лента заказов в шапке")
    def click_order_feed_button_on_header(self):
        self.driver.find_element(*BP.HEADER_ORDER_FEED_BUTTON).click()

    @allure.step("Клик на кнопку Конструктор в шапке")
    def click_constructor_button_on_header(self):
        self.driver.find_element(*BP.HEADER_CONSTRUCTOR_BUTTON).click()
