from pages.base_page import BasePage
from locators.main_page_locators import StellarBurgerMainPageLocators as MP
import allure
from locators.base_page_locators import StellarBurgerBasePageLocators as BP
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class StellarBurgerMainPage(BasePage):

    @allure.step("Клик на ингредиент")
    def click_ingridient_button(self):
        self.find_element_with_click(MP.INGRIDIENT_BUTTON)

    @allure.step("Отображение модального окна ингредиента")
    def ingridient_pop_up_windows_is_displayed(self):
        return self.find_element_with_is_displayed(MP.INGRIDIENT_POP_UP_WINDOW)

    @allure.step("Клик на кнопку Закрыть в модальном окне ингредиента")
    def ingredient_pop_up_window_cross_button(self):
        self.find_element_with_click(MP.INGRIDIENT_POP_UP_WINDOW_CROSS_BUTTON)

    @allure.step("Перетаскивание ингредиента в корзину")
    def ingridient_drag_and_drop(self):
        self.drag_and_drop(MP.BUN_INGREDIENT, MP.BASKET)

    @allure.step("Счётчик Булки")
    def counter_bulka(self):
        return self.get_element_text(MP.BULKA_COUNTER)

    @allure.step("Клик на кнопку Оформить заказ")
    def click_create_order_button(self):
        self.find_element_with_click(MP.CREATE_ORDER)

    @allure.step("Модальное окно успешного заказа открыто")
    def successful_order_modal_window_open(self):
        return self.find_element_with_is_displayed(MP.SUCCESSFUL_ORDER_WINDOW)

    @allure.step("Получение номера заказа из модального окна успешного заказа")
    def get_order_number_in_modal_window(self):
        order = self.get_element_text(MP.MODAL_WINDOW_ORDER_NUMBER)
        formated_order = ('#0' + str(order))
        return formated_order

    @allure.step("Клик на кнопку Закрыть модального окна успешного заказа")
    def click_order_pop_up_window_close_button(self):
        self.find_element_with_click(MP.MODAL_WINDOW_CLOSE_BUTTON)


    @allure.step("Клик на кнопку 'Личный кабинет'")
    def click_account_button_in_header(self):
        self.find_element_with_click(BP.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Клик на кнопку Лента заказов в шапке")
    def click_order_feed_button_on_header(self):
        self.find_element_with_click(BP.HEADER_ORDER_FEED_BUTTON)

    @allure.step("Клик на кнопку Конструктор в шапке")
    def click_constructor_button_on_header(self):
        self.find_element_with_click(BP.HEADER_CONSTRUCTOR_BUTTON)

    @allure.step("Ждём пока окно ингредиентов не показывает себя")
    def wait_until_ingredient_window_not_displayed(self):
        self.wait_until_element_not_displayed(MP.INGRIDIENT_POP_UP_WINDOW)

    @allure.step("Ждём пока ингредиенты покажут себя")
    def wait_until_ingredients_will_displayed(self):
        self.wait_until_element_visibility_located(MP.BUN_INGREDIENT)

    @allure.step("Ждём пока уйдёт оверлей")
    def wait_until_overlay_gone(self):
        self.wait_until_invisibility_element(MP.IMG_LOADING)

