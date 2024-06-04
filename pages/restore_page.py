from locators.restore_password_page_locators import StellarBurgerRestorePasswordPage as RP
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class StellarBurgersRestorePage(BasePage):
    @allure.step("Заполнение поля Email")
    def filling_out_restore_password_email_field(self, email):
        self.driver.find_element(*RP.EMAIL_RESTORE_INPUT).send_keys(email)

    @allure.step("Клик на кнопку Восстановить")
    def click_restore_button(self):
        self.driver.find_element(*RP.RESTORE_BUTTON).click()

    @allure.step("Клик на кнопку Показать Скрыть пароль")
    def click_inactive_eye_button(self):
        self.driver.find_element(*RP.EYE_BUTTON_INACTIVE).click()

    @allure.step("Поле Восстановить пароль активно")
    def restore_password_field_is_active(self):
        return self.driver.find_element(*RP.RESTORE_PASSWORD_ACTIVE_FIELD).is_displayed()

    @allure.step("Ждать, пока глаз покажет себя")
    def wait_until_eye_show(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(RP.EYE_BUTTON_INACTIVE))
