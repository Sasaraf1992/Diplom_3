import settings
import allure
from pages.login_page import StellarBurgerLoginPage
from pages.main_page import StellarBurgerMainPage


class TestMainPage:
    @allure.title("Тест перехода на страницу Конструктора по клику на кнопку конструктор")
    def test_constructor_header_button(self, driver):
        mp = StellarBurgerMainPage(driver)
        mp.click_account_button_in_header()
        mp = StellarBurgerMainPage(driver)
        mp.click_constructor_button_on_header()
        main_page = settings.URL
        mp.wait_until_url_contains(main_page)
        assert mp.current_url_page() == main_page

    @allure.title("Тест перехода на страницу Лента заказов по клику на кнопку Лента Заказов")
    def test_order_feed_header_button(self, driver):
        mp = StellarBurgerMainPage(driver)
        mp.click_order_feed_button_on_header()
        order_page = settings.URL_ORDER_FEED
        mp.wait_until_url_contains(order_page)
        assert mp.current_url_page() == order_page

    @allure.title("Тест появления модального окна ингредиента по клику")
    def test_ingridient_pop_up_window(self, driver):
        mp = StellarBurgerMainPage(driver)
        mp.click_ingridient_button()
        assert mp.ingridient_pop_up_windows_is_displayed()

    @allure.title("Тест закрытия модального окна ингредиента по клику")
    def test_ingridient_pop_up_window_close(self, driver):
        mp = StellarBurgerMainPage(driver)
        mp.click_ingridient_button()
        mp.ingredient_pop_up_window_cross_button()
        mp.wait_until_ingredient_window_not_displayed()
        assert not mp.ingridient_pop_up_windows_is_displayed()

    @allure.title("Тест изменения счётчика ингредиента при его добавлении в заказ")
    def test_counter_change(self, driver):
        mp = StellarBurgerMainPage(driver)
        counter_before = mp.counter_bulka()
        mp.ingridient_drag_and_drop()
        counter_after = mp.counter_bulka()
        assert counter_after > counter_before

    @allure.title("Тест создания заказа залогининым пользователям")
    def test_create_order_by_auth_user(self, driver, fake_user):
        email, password = fake_user
        mp = StellarBurgerMainPage(driver)
        lp = StellarBurgerLoginPage(driver)
        mp.click_account_button_in_header()
        lp.email_field_fill(email)
        lp.password_field_fill(password)
        lp.click_login_button()
        mp.wait_until_ingredients_will_displayed()
        mp.ingridient_drag_and_drop()
        mp.click_create_order_button()
        assert mp.successful_order_modal_window_open()
