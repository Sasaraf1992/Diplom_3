from pages.base_page import BasePage
from locators.main_page_locators import StellarBurgerMainPageLocators as MP
import allure
from locators.order_page_locators import StellarBurgerOrderPageLocators as OP


class StellarBurgerOrderPage(BasePage):

    @allure.step("Клик на заказ")
    def click_order_in_order_feed(self):
        self.driver.find_element(*OP.SECOND_ORDER).click()

    @allure.step("Модальное окно заказа отображено")
    def order_pop_up_window_displayed(self):
        return self.driver.find_element(*OP.MODAL_ORDER_WINDOW).is_displayed()

    @allure.step("Получение числа заказов за всё время")
    def get_all_time_order_number(self):
        return self.driver.find_element(*OP.ALL_TIME_COUNTER).text

    @allure.step("Получение числа заказов за сегодня")
    def get_today_order_number(self):
        return self.driver.find_element(*OP.TODAY_COUNTER).text

    @allure.step("Получение номер оформленного заказа в ленте готовящихся заказов")
    def get_order_in_work_chapter_number(self):
        order_in_work = self.driver.find_element(*OP.ORDER_IN_PROGRESS).text
        formated_order = ('#' + str(order_in_work))
        return formated_order
