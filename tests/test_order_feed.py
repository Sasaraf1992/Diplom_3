import settings
from locators.restore_password_page_locators import StellarBurgerRestorePasswordPage as RP
from locators.login_page_locators import StellarBurgerRegistrationLocators as RL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure
from pages.login_page import StellarBurgerLoginPage
from pages.restore_page import StellarBurgersRestorePage
from pages.personal_account_page import StellarBurgerPersonalAccountPage
from pages.main_page import StellarBurgerMainPage
from selenium.webdriver.common.action_chains import ActionChains
from locators.main_page_locators import StellarBurgerMainPageLocators as MP
import time
from pages.order_page import StellarBurgerOrderPage
import pytest


class TestOrderPage:
    @allure.title("Тест появления модального окна заказа при клике на заказ")
    def test_order_pop_up_window(self, driver):
        op = StellarBurgerOrderPage(driver)
        op.time_to_wait(1)
        op.click_order_feed_button_on_header()
        op.time_to_wait(1)
        op.click_order_in_order_feed()
        assert op.order_pop_up_window_displayed()

    @allure.title("Тест появления заказа в разделе История заказов")
    def test_order_history_in_personal_account(self, driver, fake_user_required_login_password):
        email, password = fake_user_required_login_password
        lp = StellarBurgerLoginPage(driver)
        lp.time_to_wait(1)
        lp.click_account_button_in_header()
        lp.email_field_fill(email)
        lp.password_field_fill(password)
        lp.click_login_button()
        mp = StellarBurgerMainPage(driver)
        mp.time_to_wait(1)
        mp.drag_and_drop_firefox(driver)
        mp.click_create_order_button()
        mp.time_to_wait(5)
        order_number = mp.get_order_number_in_modal_window()
        mp.click_order_pop_up_window_close_button()
        mp.click_account_button_in_header()
        pa = StellarBurgerPersonalAccountPage(driver)
        mp.time_to_wait(1)
        pa.click_order_history_button()
        mp.time_to_wait(1)
        user_order_number = pa.get_user_last_order_number()
        assert order_number == user_order_number

    @allure.title("Тест увеличение счётчиков при заказе")
    @pytest.mark.parametrize("order_type", ["all_time", "today"])
    def test_order_counter_increases(self, driver, fake_user_required_login_password, order_type):
        email, password = fake_user_required_login_password
        lp = StellarBurgerLoginPage(driver)
        lp.time_to_wait(1)
        lp.click_account_button_in_header()
        lp.email_field_fill(email)
        lp.password_field_fill(password)
        lp.click_login_button()

        mp = StellarBurgerMainPage(driver)
        mp.time_to_wait(2)
        mp.click_order_feed_button_on_header()

        op = StellarBurgerOrderPage(driver)
        op.time_to_wait(2)

        if order_type == "all_time":
            old_number = op.get_all_time_order_number()
        elif order_type == "today":
            old_number = op.get_today_order_number()

        op.click_constructor_button_on_header()
        mp.drag_and_drop_firefox(driver)
        mp.click_create_order_button()
        mp.time_to_wait(3)
        mp.click_order_pop_up_window_close_button()
        mp.click_order_feed_button_on_header()
        mp.time_to_wait(2)
        if order_type == "all_time":
            new_number = op.get_all_time_order_number()
        elif order_type == "today":
            new_number = op.get_today_order_number()
        assert new_number > old_number

    @allure.title("Тест появления номера заказа в разделе В работе")
    def test_new_order_appers_in_in_work_chapter(self, driver, fake_user_required_login_password):
        email, password = fake_user_required_login_password
        lp = StellarBurgerLoginPage(driver)
        lp.time_to_wait(1)
        lp.click_account_button_in_header()
        lp.email_field_fill(email)
        lp.password_field_fill(password)
        lp.click_login_button()
        mp = StellarBurgerMainPage(driver)
        mp.time_to_wait(1)
        op = StellarBurgerOrderPage(driver)
        op.time_to_wait(1)
        mp.drag_and_drop_firefox(driver)
        mp.click_create_order_button()
        mp.time_to_wait(3)
        order_number = mp.get_order_number_in_modal_window()
        mp.click_order_pop_up_window_close_button()
        mp.time_to_wait(1)
        mp.click_order_feed_button_on_header()
        mp.time_to_wait(7)
        order_in_work_number = op.get_order_in_work_chapter_number()
        assert order_number == order_in_work_number
