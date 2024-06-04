from selenium.webdriver.common.by import By


class StellarBurgerRestorePasswordPage:
    EMAIL_RESTORE_INPUT = [By.NAME, "name"] # Поле восстановления пароля
    RESTORE_BUTTON = [By.XPATH, '//button[text() = "Восстановить"]'] # Кнопка "Восстановить"
    RESTORE_PASSWORD_ACTIVE_FIELD = [By.XPATH, '//input[@type="text"]'] # Активное поле "Восстановить пароль"
    EYE_BUTTON_INACTIVE = [By.CSS_SELECTOR, "div.input__icon.input__icon-action > svg > path"] # Кнопка "Скрыть пароль"