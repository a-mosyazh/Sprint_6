import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocator
from locators.order_page_locators import OrderPageLocator


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание загрузки кнопки "Заказать"')
    def wait_for_order_button_load(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(BasePageLocator.start_order_button))

    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button(self):
        self.driver.find_element(*BasePageLocator.start_order_button).click()

    @allure.step('Ожидание загрузки поля "Имя" на первом шаге оформления заказа')
    def wait_for_first_step_load(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocator.name_field))

    @allure.step('Указание имени')
    def set_name(self, name):
        self.driver.find_element(*OrderPageLocator.name_field).send_keys(name)

    @allure.step('Указание фамилии')
    def set_last_name(self, last_name):
        self.driver.find_element(*OrderPageLocator.surname_filed).send_keys(last_name)

    @allure.step('Указание адреса')
    def set_address(self, address):
        self.driver.find_element(*OrderPageLocator.address_field).send_keys(address)

    @allure.step('Поиск станции метро')
    def search_metro_station(self, station):
        input_field = self.driver.find_element(*OrderPageLocator.metro_station_field)
        actions = ActionChains(self.driver)
        actions.click(input_field)
        for char in station:
            actions.send_keys(char)
        actions.perform()

    @allure.step('Выбор станции метро')
    def click_metro_station(self):
        self.driver.find_element(*OrderPageLocator.metro_station_option).click()

    @allure.step('Указание номера телефона')
    def set_phone_number(self, phone_number):
        self.driver.find_element(*OrderPageLocator.phone_number_field).send_keys(phone_number)

    @allure.step('Клик по кнопке "Далее"')
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocator.next_button).click()

    @allure.step('Ожидание загрузки поля с датой на втором шаге оформления заказа')
    def wait_for_second_step_load(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocator.date_field))

    @allure.step('Клик по полю с датой')
    def click_rent_date_field(self):
        self.driver.find_element(*OrderPageLocator.date_field).click()

    @allure.step('Выбор следующего дня в календаре')
    def select_rent_date(self):
        self.driver.find_element(*OrderPageLocator.next_day_option).click()

    @allure.step('Клик по полю со сроком аренды')
    def click_rent_period(self):
        self.driver.find_element(*OrderPageLocator.rent_period).click()

    @allure.step('Выбор срока аренды')
    def select_rent_period(self):
        self.driver.find_element(*OrderPageLocator.rent_period_option).click()

    @allure.step('Выбор черного цвета самоката')
    def click_on_black_color(self):
        self.driver.find_element(*OrderPageLocator.black_color).click()

    @allure.step('Клик по кнопке "Заказать" для завершения оформления заказа')
    def click_finish_order_button(self):
        self.driver.find_element(*OrderPageLocator.finish_order_button).click()

    @allure.step('Ожидание окна для подтвержденя оформления заказа')
    def wait_for_order_confirmation(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(OrderPageLocator.order_confirmation_button))

    @allure.step('Клик по кнопке "Да" в окне-потверждении заказа')
    def click_confirm_order_button(self):
        self.driver.find_element(*OrderPageLocator.order_confirmation_button).click()

    @allure.step('Получение заголовка окна с уведомлением о создании заказа')
    def get_order_creation_window_title(self):
        title_element = self.driver.find_element(*OrderPageLocator.order_created_window_title)
        title = title_element.text.split('\n')[0]
        return title

    @allure.step('Ожидание создания заказа')
    def wait_for_order_id(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: (len(driver.find_element(*OrderPageLocator.order_details).text.split('.')[0]) >
                            len('Номер заказа: '))
        )

    @allure.step('Получение номера заказа')
    def get_order_id(self):
        order_details_element = self.driver.find_element(*OrderPageLocator.order_details)
        order_id = order_details_element.text.split('.')[0].split(': ')[1]
        return order_id
