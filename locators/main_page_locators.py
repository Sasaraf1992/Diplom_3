from selenium.webdriver.common.by import By


class StellarBurgerMainPageLocators:
    INGRIDIENT_BUTTON = [By.XPATH, '//img[@alt = "Флюоресцентная булка R2-D3"]']  # Булка "Флюоресцентная булка R2-D3"
    INGRIDIENT_POP_UP_WINDOW = [By.XPATH, '//h2[text() = "Детали ингредиента"]']  # Модальное окно ингредиента
    INGRIDIENT_POP_UP_WINDOW_CROSS_BUTTON = [By.XPATH, '//section[1]/div[1]/button[1][contains(@class, '
                                                       '"Modal_modal__close__TnseK")]']  # Кнопка "Закрыть" в
    # модальном окне ингредиента
    INGRIDIENT_POP_UP_WINDOW_CLOSED = [By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]"]  # Статус
    # "Закрыто" модального окна ингредиента
    BASKET = [By.XPATH, '//section[contains(@class,"BurgerConstructor_basket")]'] # Корзина
    CHECKOUT_BUTTON = [By.XPATH, './/div[starts-with(@class,"BurgerConstructor_basket__container")]/button'] # Кнопка "Оформить заказ"
    BUN_INGREDIENT = [By.XPATH, './/p[contains(text(), "Краторная булка N-200i")]'] # Булка "Краторная булка N-200i"
    BULKA_COUNTER = (By.XPATH, ".//ul[1]/a[2]//p[contains(@class, 'num')]") # Счётчик булки
    CREATE_ORDER = (By.XPATH, ".//button[contains(text(), 'Оформить заказ')]") # Кнопка оформить заказ"
    SUCCESSFUL_ORDER_WINDOW = [By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]"] # Модальное окно созданного заказа
    MODAL_WINDOW_ORDER_NUMBER = [By.XPATH, './/h2[contains(@class, "Modal_modal__title_shadow")]'] # Номер заказа в модальном окне
    MODAL_WINDOW_CLOSE_BUTTON = [By.XPATH, '//button[contains(@class, "Modal_modal__close")]'] # Кнопка "Закрыть" в модальном окне созданного заказа
    MODAL_OVERLAY = (By.CSS_SELECTOR, '.Modal_modal__P3_V5[style="visibility: hidden;"]')
    IMG_LOADING = [By.CSS_SELECTOR, '.Modal_modal__loading__3534A']
