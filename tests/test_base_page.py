import allure
from global_params import base_url, order_url, dzen_url
from pages.base_page import BasePage


class TestBasePage:

    @allure.title('Проверка открытия домашней страницы по клику на лого "Самокат"')
    @allure.description('После клика по лого проверяем, что get_current_link() == base_url')
    def test_redirect_to_home_page(self, driver):
        driver.get(order_url)

        base_page = BasePage(driver)
        base_page.wait_for_order_button_load()
        base_page.click_scooter_logo()

        assert base_page.get_current_link() == base_url

    @allure.title('Проверка редиректа на Дзен по клику на лого "Яндекс"')
    @allure.description('После клика по лого переключаемся на новую открытую вкладку '
                        'и проверяем, что get_current_link() == dzen_url')
    def test_redirect_to_dzen_page(self, driver):
        driver.get(order_url)

        base_page = BasePage(driver)
        base_page.wait_for_order_button_load()
        base_page.click_yandex_logo()

        # Переключение между вкладками
        original_window = driver.current_window_handle
        new_window = [window for window in driver.window_handles if window != original_window][0]
        driver.switch_to.window(new_window)

        base_page.wait_for_load_after_redirect(dzen_url)

        assert base_page.get_current_link() == dzen_url
