
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import ActionChains

import settings


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.url = settings.URL

    def find_element_with_click(self, element):
        self.driver.find_element(*element).click()

    def find_element_with_is_displayed(self, element):
        return self.driver.find_element(*element).is_displayed()

    def get_element_text(self, element):
        return self.driver.find_element(*element).text

    def send_keys_element(self, element, text):
        self.driver.find_element(*element).send_keys(text)

    def drag_and_drop(self, element, target_element):
        element = self.driver.find_element(*element)
        target_element = self.driver.find_element(*target_element)
        action = ActionChains(self.driver)
        action.drag_and_drop(element, target_element).perform()

    def wait_until_url_contains(self, url):
        WebDriverWait(self.driver, 10).until(EC.url_contains(url))

    def current_url_page(self):
        return self.driver.current_url

    def wait_until_element_not_displayed(self, element):
        WebDriverWait(self.driver, 10).until_not(EC.visibility_of_element_located(element))

    def wait_until_element_visibility_located(self, element):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element))

    def wait_until_element_clickable(self, element):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(element))

    def wait_until_invisibility_element(self, element):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(element))

    def wait_until_element_text_present(self, element, text):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(element, text))
