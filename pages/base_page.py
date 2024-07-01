import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocator


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание загрузки кнопки "Заказать"')
    def wait_for_order_button_load(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(BasePageLocator.start_order_button))

    @allure.step('Клик по лого "Яндекс"')
    def click_yandex_logo(self):
        self.driver.find_element(*BasePageLocator.yandex_logo).click()

    @allure.step('Клик по лого "Самокат"')
    def click_scooter_logo(self):
        self.driver.find_element(*BasePageLocator.scooter_logo).click()

    @allure.step('Получение текущей ссылки вкладки')
    def get_current_link(self):
        return self.driver.current_url

    @allure.step('Ожидание полного окончания редиректа')
    def wait_for_load_after_redirect(self, expected_url):
        WebDriverWait(self.driver, 20).until(expected_conditions.url_to_be(expected_url))
