import settings
from locators.restore_password_page_locators import StellarBurgerRestorePasswordPage as RP
from locators.login_page_locators import StellarBurgerRegistrationLocators as RL
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure
from pages.login_page import StellarBurgerLoginPage
from pages.restore_page import StellarBurgersRestorePage
from pages.personal_account_page import StellarBurgerPersonalAccountPage


class TestPersonalAccount:
    @allure.title("Тест перехода на страницу Личного кабинета по клику на кнопку в шапке")
    def test_personal_account_transition_after_reg(self, driver, fake_user_required_login_password):
        email, password = fake_user_required_login_password
        lp = StellarBurgerLoginPage(driver)
        lp.time_to_wait(1)
        lp.click_account_button_in_header()
        lp.email_field_fill(email)
        lp.password_field_fill(password)
        lp.click_login_button()
        lp.time_to_wait(1)
        lp.click_account_button_in_header()
        account_profile_page = settings.URL_ACCOUNT_PROFILE
        lp.time_to_wait(3)
        assert driver.current_url == account_profile_page

    @allure.title("Тест перехода в раздел История заказов")
    def test_order_history_button_active(self, driver, fake_user_required_login_password):
        email, password = fake_user_required_login_password
        lp = StellarBurgerLoginPage(driver)
        lp.time_to_wait(1)
        lp.click_account_button_in_header()
        lp.email_field_fill(email)
        lp.password_field_fill(password)
        lp.time_to_wait(1)
        lp.click_login_button()
        lp.click_account_button_in_header()
        pa = StellarBurgerPersonalAccountPage(driver)
        lp.time_to_wait(1)
        pa.click_order_history_button()
        order_history_page = settings.URL_ORDER_HISTORY
        lp.wait_until_url_contains(order_history_page)
        assert driver.current_url == order_history_page

    @allure.title("Тест выхода из аккаунта")
    def test_exit_button_active(self, driver, fake_user_required_login_password):
        email, password = fake_user_required_login_password
        lp = StellarBurgerLoginPage(driver)
        lp.time_to_wait(1)
        lp.click_account_button_in_header()
        lp.email_field_fill(email)
        lp.password_field_fill(password)
        lp.time_to_wait(1)
        lp.click_login_button()
        lp.click_account_button_in_header()
        pa = StellarBurgerPersonalAccountPage(driver)
        lp.time_to_wait(2)
        pa.click_exit_button()
        login_page = settings.URL_LOGIN_PAGE
        lp.wait_until_url_contains(login_page)
        assert driver.current_url == login_page
