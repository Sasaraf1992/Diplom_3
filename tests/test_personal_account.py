import settings
import allure
from pages.login_page import StellarBurgerLoginPage
from pages.personal_account_page import StellarBurgerPersonalAccountPage
from pages.main_page import StellarBurgerMainPage


class TestPersonalAccount:
    @allure.title("Тест перехода на страницу Личного кабинета по клику на кнопку в шапке")
    def test_personal_account_transition_after_reg(self, driver, fake_user):
        email, password = fake_user
        lp = StellarBurgerLoginPage(driver)
        mp = StellarBurgerMainPage(driver)
        mp.click_account_button_in_header()
        lp.email_field_fill(email)
        lp.password_field_fill(password)
        lp.click_login_button()
        mp.click_account_button_in_header()
        account_profile_page = settings.URL_ACCOUNT_PROFILE
        mp.wait_until_url_contains(account_profile_page)
        assert mp.current_url_page() == account_profile_page

    @allure.title("Тест перехода в раздел История заказов")
    def test_order_history_button_active(self, driver, fake_user):
        email, password = fake_user
        lp = StellarBurgerLoginPage(driver)
        mp = StellarBurgerMainPage(driver)
        mp.click_account_button_in_header()
        lp.email_field_fill(email)
        lp.password_field_fill(password)
        lp.click_login_button()
        mp.click_account_button_in_header()
        pa = StellarBurgerPersonalAccountPage(driver)
        pa.wait_until_history_button_show()
        pa.click_order_history_button()
        order_history_page = settings.URL_ORDER_HISTORY
        lp.wait_until_url_contains(order_history_page)
        assert mp.current_url_page() == order_history_page

    @allure.title("Тест выхода из аккаунта")
    def test_exit_button_active(self, driver, fake_user):
        email, password = fake_user
        mp = StellarBurgerMainPage(driver)
        lp = StellarBurgerLoginPage(driver)
        mp.click_account_button_in_header()
        lp.email_field_fill(email)
        lp.password_field_fill(password)
        lp.click_login_button()
        mp.click_account_button_in_header()
        pa = StellarBurgerPersonalAccountPage(driver)
        pa.wait_until_history_button_show()
        pa.click_exit_button()
        login_page = settings.URL_LOGIN_PAGE
        lp.wait_until_url_contains(login_page)
        assert mp.current_url_page() == login_page
