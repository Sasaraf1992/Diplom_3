from selenium.webdriver.common.by import By


class StellarBurgerRestorePersonalAccountPage:
    ORDER_HISTORY_BUTTON =[By.XPATH, '//a[text() = "История заказов"]'] # Кнопка "История заказов"
    EXIT_BUTTON = [By.XPATH, '//button[text() = "Выход"]'] # Кнопка "Выход"
    USER_ORDERS_HISTORY = [
        By.XPATH, './/li[contains(@class,"OrderHistory_listItem")]/a/div/p[contains(@class,"digits")]'] # Номер заказа в "Истории заказов"