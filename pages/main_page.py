from pages.base_page import BasePage
from locators.main_page_locators import StellarBurgerMainPageLocators as MP
import allure
from locators.base_page_locators import StellarBurgerBasePageLocators as BP
from selenium.webdriver import ActionChains
from seletools.actions import drag_and_drop

class StellarBurgerMainPage(BasePage):

    @allure.step("Клик на ингредиент")
    def click_ingridient_button(self):
        self.driver.find_element(*MP.INGRIDIENT_BUTTON).click()

    @allure.step("Отображение модального окна ингредиента")
    def ingridient_pop_up_windows_is_displayed(self):
        return self.driver.find_element(*MP.INGRIDIENT_POP_UP_WINDOW).is_displayed()

    @allure.step("Клик на кнопку Закрыть в модальном окне ингредиента")
    def ingredient_pop_up_window_cross_button(self):
        self.driver.find_element(*MP.INGRIDIENT_POP_UP_WINDOW_CROSS_BUTTON).click()

    @allure.step("Модальное окно ингредиента закрыто")
    def ingridient_pop_up_windows_is_closed(self):
        return self.driver.find_element(*MP.INGRIDIENT_POP_UP_WINDOW_CLOSED).is_displayed()

    @allure.step("Перетаскивание ингредиента в корзину")
    def ingridient_drag_and_drop(self):
        bun = self.driver.find_element(*MP.BUN_INGREDIENT)
        basket = self.driver.find_element(*MP.BASKET)
        action = ActionChains(self.driver)
        action.drag_and_drop(bun, basket).perform()

    def drag_and_drop_firefox(self, driver):
        bun = self.driver.find_element(*MP.BUN_INGREDIENT)
        basket = self.driver.find_element(*MP.BASKET)
        drag_and_drop(driver, bun, basket)

    @allure.step("Счётчик Булки")
    def counter_bulka(self):
        return self.driver.find_element(*MP.BULKA_COUNTER).text

    @allure.step("Клик на кнопку Оформить заказ")
    def click_create_order_button(self):
        self.driver.find_element(*MP.CREATE_ORDER).click()

    @allure.step("Модальное окно успешного заказа открыто")
    def successful_order_modal_window_open(self):
        return self.driver.find_element(*MP.SUCCESSFUL_ORDER_WINDOW).is_displayed()

    @allure.step("Получение номера заказа из модального окна успешного заказа")
    def get_order_number_in_modal_window(self):
        order = self.driver.find_element(*MP.MODAL_WINDOW_ORDER_NUMBER).text
        formated_order = ('#0' + str(order))
        return formated_order

    @allure.step("Клик на кнопку Закрыть модального окна успешного заказа")
    def click_order_pop_up_window_close_button(self):
        self.driver.find_element(*MP.MODAL_WINDOW_CLOSE_BUTTON).click()
