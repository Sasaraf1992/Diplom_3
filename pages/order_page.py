from pages.base_page import BasePage
from locators.main_page_locators import StellarBurgerMainPageLocators as MP
import allure
from locators.order_page_locators import StellarBurgerOrderPageLocators as OP


class StellarBurgerOrderPage(BasePage):

    @allure.step("Клик на заказ")
    def click_order_in_order_feed(self):
        self.find_element_with_click(OP.SECOND_ORDER)

    @allure.step("Ждём пока появится кнопка заказа")
    def wait_until_order_button_displayed(self):
        self.wait_until_element_visibility_located(OP.SECOND_ORDER)

    @allure.step("Модальное окно заказа отображено")
    def order_pop_up_window_displayed(self):
        return self.find_element_with_is_displayed(OP.MODAL_ORDER_WINDOW)

    @allure.step("Получение числа заказов за всё время")
    def get_all_time_order_number(self):
        return self.get_element_text(OP.ALL_TIME_COUNTER)

    @allure.step("Получение числа заказов за сегодня")
    def get_today_order_number(self):
        return self.get_element_text(OP.TODAY_COUNTER)

    @allure.step("Получение номер оформленного заказа в ленте готовящихся заказов")
    def get_order_in_work_chapter_number(self):
        order_in_work = self.get_element_text(OP.ORDER_IN_PROGRESS)
        formated_order = ('#' + str(order_in_work))
        return formated_order

    @allure.step("Ждём пока число заказов за всё время появится")
    def wait_until_all_time_number_show(self):
        self.wait_until_element_visibility_located(OP.ALL_TIME_COUNTER)

    @allure.step("Ждём пока появится номер заказа В работе")
    def wait_until_in_work_number_show(self, order):
        self.wait_until_element_text_present(OP.ORDER_IN_PROGRESS, str(order[-1]))
