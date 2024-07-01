import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидание загрузки блока с вопросом')
    def wait_for_load_home_page(self, question):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(question))

    @allure.step('Ожидание кликабельности блока с вопросом')
    def wait_for_clickable(self, question):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(question))

    @allure.step('Скролл до блока с вопросом')
    def scroll_down(self, question):
        question_btn = self.driver.find_element(*question)
        self.driver.execute_script("arguments[0].scrollIntoView();", question_btn)

    @allure.step('Клик по вопросу')
    def click_on_question(self, question):
        self.driver.find_element(*question).click()

    @allure.step('Получение текста блока')
    def get_element_text(self, element):
        return self.driver.find_element(*element).text
