import settings
import allure
from pages.login_page import StellarBurgerLoginPage
from pages.restore_page import StellarBurgersRestorePage


class TestRestorePassword:
    @allure.title("Тест перехода на страницу восстановления пароля по клику на кнопку Восстановить пароль")
    def test_transition_on_restore_password_page_by_button_click(self, driver):
        lp = StellarBurgerLoginPage(driver)
        lp.time_to_wait(1)
        lp.click_account_button_in_header()
        lp.click_restore_button()
        forgot_password_page = settings.URL_FORGOT_PASSWORD_PAGE
        lp.wait_until_url_contains(forgot_password_page)
        assert driver.current_url == forgot_password_page

    @allure.title("Тест успешного ввода почты и клика по кнопке Восстановить")
    def test_restore_button_active(self, driver, fake_user_required_login_password):
        email = fake_user_required_login_password
        lp = StellarBurgerLoginPage(driver)
        lp.time_to_wait(1)
        lp.click_account_button_in_header()
        lp.click_restore_button()
        rp = StellarBurgersRestorePage(driver)
        rp.filling_out_restore_password_email_field(email)
        rp.click_restore_button()
        reset_password_page = settings.URL_RESET_PASSWORD_PAGE
        rp.wait_until_url_contains(reset_password_page)
        assert driver.current_url == reset_password_page

    @allure.title("Тест подсвечивания поля при клике на кнопку показать/скрыть пароль")
    def test_restore_password_field_active(self, driver, fake_user_required_login_password):
        email = fake_user_required_login_password
        lp = StellarBurgerLoginPage(driver)
        lp.time_to_wait(1)
        lp.click_account_button_in_header()
        lp.click_restore_button()
        rp = StellarBurgersRestorePage(driver)
        rp.filling_out_restore_password_email_field(email)
        rp.click_restore_button()
        rp.wait_until_eye_show()
        lp.time_to_wait(1)
        rp.click_inactive_eye_button()
        assert rp.restore_password_field_is_active()
