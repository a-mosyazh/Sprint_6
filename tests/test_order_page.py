import pytest
import allure
from global_params import base_url
from pages.order_page import OrderPage
from utils.test_data import order_data


class TestOrderPage:

    @allure.title('Проверка успешного создания заказа')
    @allure.description('После заполнения данных проверяем, что появилось '
                        'всплывающее окно с номером заказа и заголовком "Заказ оформлен"')
    @pytest.mark.parametrize(
        'name, last_name, address, metro_station, phone_number', order_data
    )
    def test_order_creation(self, driver, name, last_name, address, metro_station, phone_number):
        driver.get(base_url)

        order_page = OrderPage(driver)
        order_page.wait_for_order_button_load()
        order_page.click_order_button()
        # Заполнение первого шага создания заказа
        order_page.wait_for_first_step_load()
        order_page.set_name(name)
        order_page.set_last_name(last_name)
        order_page.set_address(address)
        order_page.search_metro_station(metro_station)
        order_page.click_metro_station()
        order_page.set_phone_number(phone_number)
        order_page.click_next_button()
        # Заполнение второго шага создания заказа
        order_page.wait_for_second_step_load()
        order_page.click_rent_date_field()
        order_page.select_rent_date()
        order_page.click_rent_period()
        order_page.select_rent_period()
        order_page.click_on_black_color()
        order_page.click_finish_order_button()
        # Ожидание окна-потверждения создания заказа
        order_page.wait_for_order_confirmation()
        # Создание заказа
        order_page.click_confirm_order_button()
        # Ожидание создания заказа
        order_page.wait_for_order_id()
        window_title = order_page.get_order_creation_window_title()
        order_id = order_page.get_order_id()

        assert window_title == 'Заказ оформлен' and int(order_id) > 0
