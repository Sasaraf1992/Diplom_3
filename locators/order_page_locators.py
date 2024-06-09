from selenium.webdriver.common.by import By



class StellarBurgerOrderPageLocators:
    SECOND_ORDER = [By.XPATH, ".//ul[@class='OrderFeed_list__OLh59']/li[2]"] # Лист ингредиентов
    MODAL_ORDER_WINDOW = [By.XPATH, ".//div[contains(@class, 'Modal_orderBox')]"] # Модальное окно заказа
    # История заказов в лк пользователя
    USER_ORDERS_HISTORY = [
        By.XPATH, './/li[contains(@class,"OrderHistory_listItem")]/a/div/p[contains(@class,"digits")]'] #История заказов пользователя

    ORDER_NUMBERS = [By.XPATH, '//p[@class="text text_type_digits-default"]']  # Номера всех заказов в ленте
    LAST_ORDER = [By.XPATH, '//li[1]//p[@class="text text_type_digits-default"]']  # Номер последнего заказа в ленте
    ORDER_IN_PROGRESS = [By.CSS_SELECTOR, 'ul.OrderFeed_orderListReady__1YFem li']  # Номер в разделе "В работе"
    # Счётчик "Выполнено за всё время"
    ALL_TIME_COUNTER = [By.XPATH, '//p[text()="Выполнено за все время:"]/../p[contains(@class,"OrderFeed_number")]']
    # Счётчик "Выполнено за сегодня"
    TODAY_COUNTER = [By.XPATH, '//p[text()="Выполнено за сегодня:"]/../p[contains(@class,"OrderFeed_number")]']

