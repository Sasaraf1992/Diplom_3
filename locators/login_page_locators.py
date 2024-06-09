from selenium.webdriver.common.by import By


class StellarBurgerRegistrationLocators:
    RESTORE_PASSWORD_BUTTON = [By.XPATH, "//a[text() = 'Восстановить пароль']"] # Кнопа "Восстановить пароль
    EMAIL_FIELD = [By.XPATH, '//input[@type="text"]'] # Поле "Email"
    PASSWORD_FIELD = [By.XPATH, '//input[@type="password"]'] # Поле "Пароль"
    LOGIN_BUTTON = [By.XPATH, "//button[text() = 'Войти']"] # Кнопка "Войти"
