
import allure
from pages.login_page import StellarBurgerLoginPage
from pages.personal_account_page import StellarBurgerPersonalAccountPage
from pages.main_page import StellarBurgerMainPage
from pages.order_page import StellarBurgerOrderPage



class TestOrderPage:
    @allure.title("Тест появления модального окна заказа при клике на заказ")
    def test_order_pop_up_window(self, driver):
        mp = StellarBurgerMainPage(driver)
        op = StellarBurgerOrderPage(driver)
        mp.click_order_feed_button_on_header()
        op.wait_until_order_button_displayed()
        op.click_order_in_order_feed()
        assert op.order_pop_up_window_displayed()

    @allure.title("Тест появления заказа в разделе История заказов")
    def test_order_history_in_personal_account(self, driver, fake_user):
        email, password = fake_user
        lp = StellarBurgerLoginPage(driver)
        mp = StellarBurgerMainPage(driver)
        mp.click_account_button_in_header()
        lp.email_field_fill(email)
        lp.password_field_fill(password)
        lp.click_login_button()
        mp = StellarBurgerMainPage(driver)
        mp.wait_until_ingredients_will_displayed()
        mp.ingridient_drag_and_drop()
        mp.click_create_order_button()
        mp.wait_until_overlay_gone()
        order_number = mp.get_order_number_in_modal_window()
        mp.click_order_pop_up_window_close_button()
        mp.click_account_button_in_header()
        pa = StellarBurgerPersonalAccountPage(driver)
        pa.wait_until_history_button_show()
        pa.click_order_history_button()
        pa.wait_until_user_last_order_show()
        user_order_number = pa.get_user_last_order_number()
        assert order_number == user_order_number

    @allure.title("Тест увеличение счётчика за всё время при заказе")
    def test_all_time_order_counter_increases(self, driver, fake_user):
        email, password = fake_user
        mp = StellarBurgerMainPage(driver)
        lp = StellarBurgerLoginPage(driver)
        mp.click_account_button_in_header()
        lp.email_field_fill(email)
        lp.password_field_fill(password)
        lp.click_login_button()
        mp.click_order_feed_button_on_header()
        op = StellarBurgerOrderPage(driver)
        op.wait_until_all_time_number_show()
        old_number = op.get_all_time_order_number()
        mp.click_constructor_button_on_header()
        mp.wait_until_ingredients_will_displayed()
        mp.ingridient_drag_and_drop()
        mp.click_create_order_button()
        mp.wait_until_overlay_gone()
        mp.click_order_pop_up_window_close_button()
        mp.click_order_feed_button_on_header()
        op.wait_until_all_time_number_show()
        new_number = op.get_all_time_order_number()
        assert new_number > old_number

    @allure.title("Тест увеличение счётчика за сегодня при заказе")
    def test_today_order_counter_increases(self, driver, fake_user):
        email, password = fake_user
        mp = StellarBurgerMainPage(driver)
        lp = StellarBurgerLoginPage(driver)
        mp.click_account_button_in_header()
        lp.email_field_fill(email)
        lp.password_field_fill(password)
        lp.click_login_button()
        mp.click_order_feed_button_on_header()
        op = StellarBurgerOrderPage(driver)
        op.wait_until_all_time_number_show()
        old_number = op.get_today_order_number()
        mp.click_constructor_button_on_header()
        mp.wait_until_ingredients_will_displayed()
        mp.ingridient_drag_and_drop()
        mp.click_create_order_button()
        mp.wait_until_overlay_gone()
        mp.click_order_pop_up_window_close_button()
        mp.click_order_feed_button_on_header()
        op.wait_until_all_time_number_show()
        new_number = op.get_today_order_number()
        assert new_number > old_number



    @allure.title("Тест появления номера заказа в разделе В работе")
    def test_new_order_appears_in_work_chapter(self, driver, fake_user):
        email, password = fake_user
        lp = StellarBurgerLoginPage(driver)
        mp = StellarBurgerMainPage(driver)
        mp.click_account_button_in_header()
        lp.email_field_fill(email)
        lp.password_field_fill(password)
        lp.click_login_button()
        op = StellarBurgerOrderPage(driver)
        mp.wait_until_ingredients_will_displayed()
        mp.ingridient_drag_and_drop()
        mp.click_create_order_button()
        mp.wait_until_overlay_gone()
        order_number = mp.get_order_number_in_modal_window()
        mp.click_order_pop_up_window_close_button()
        mp.click_order_feed_button_on_header()
        op.wait_until_all_time_number_show()
        op.wait_until_in_work_number_show(order_number)
        order_in_work_number = op.get_order_in_work_chapter_number()
        assert order_number == order_in_work_number
