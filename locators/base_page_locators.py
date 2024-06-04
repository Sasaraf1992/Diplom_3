from selenium.webdriver.common.by import By


class StellarBurgerBasePageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text() = 'Личный Кабинет']")  # Кнопка "Личный Кабинет"
    HEADER_CONSTRUCTOR_BUTTON = [By.LINK_TEXT, "Конструктор"] # Кнопка "Конструктор"
    HEADER_ORDER_FEED_BUTTON = [By.LINK_TEXT, "Лента Заказов"] # Кнопка "Лента заказов"
