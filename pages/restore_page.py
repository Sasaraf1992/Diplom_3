from locators.restore_password_page_locators import StellarBurgerRestorePasswordPage as RP
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class StellarBurgersRestorePage(BasePage):
    @allure.step("Заполнение поля Email")
    def filling_out_restore_password_email_field(self, email):
        self.send_keys_element(RP.EMAIL_RESTORE_INPUT, email)

    @allure.step("Клик на кнопку Восстановить")
    def click_restore_button(self):
        self.find_element_with_click(RP.RESTORE_BUTTON)

    @allure.step("Клик на кнопку Показать Скрыть пароль")
    def click_inactive_eye_button(self):
        self.find_element_with_click(RP.EYE_BUTTON_INACTIVE)

    @allure.step("Поле Восстановить пароль активно")
    def restore_password_field_is_active(self):
        return self.find_element_with_is_displayed(RP.RESTORE_PASSWORD_ACTIVE_FIELD)


    @allure.step("Ждать, пока глаз покажет себя")
    def wait_until_eye_show(self):
        self.wait_until_element_visibility_located(RP.EYE_BUTTON_INACTIVE)
