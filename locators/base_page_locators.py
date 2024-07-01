from selenium.webdriver.common.by import By


class BasePageLocator:
    start_order_button = [By.XPATH, './/*[contains(@class, "Header")]//button[text()="Заказать"]']
    yandex_logo = [By.XPATH, './/img[@alt="Yandex"]']
    scooter_logo = [By.XPATH, './/img[@alt="Scooter"]']
