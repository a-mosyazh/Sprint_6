from selenium.webdriver.common.by import By

from utils.helpers import get_next_day

next_day = get_next_day()


class OrderPageLocator:
    name_field = [By.XPATH, './/input[@placeholder="* Имя"]']
    surname_filed = [By.XPATH, './/input[@placeholder="* Фамилия"]']
    address_field = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']
    phone_number_field = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']
    metro_station_field = [By.XPATH, './/input[@placeholder="* Станция метро"]']
    metro_station_option = [By.XPATH, './/ul[@class="select-search__options"]//button']
    next_button = [By.XPATH, './/button[text()="Далее"]']
    date_field = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']
    next_day_option = [By.XPATH, (f'.//div[@class="react-datepicker__month"]//div[text()="{next_day}" '
                                  f'and not(contains(@class, "outside-month"))]')]
    rent_period = [By.XPATH, './/div[text()="* Срок аренды"]']
    rent_period_option = [By.XPATH, './/div[text()="сутки"]']
    black_color = [By.XPATH, './/input[@id="black"]']
    finish_order_button = [By.XPATH, './/*[contains(@class, "Order_Buttons")]/button[text()="Заказать"]']
    order_confirmation_button = [By.XPATH, './/button[text()="Да"]']
    order_created_window_title = [By.XPATH, '//div[contains(@class, "Order_ModalHeader")]']
    order_details = [By.XPATH, '//div[contains(@class, "Order_Text")]']
