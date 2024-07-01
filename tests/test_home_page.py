import pytest
import allure
from global_params import base_url
from pages.home_page import HomePage
from utils.test_data import question_answer_box_data


class TestHomePage:

    @allure.title('Проверка соответствия вопросов и ответов в секции "Вопросы о важном"')
    @allure.description('Для вопроса проверяем, что actual_answer == expected_answer '
                        'and actual_question == expected_question')
    @pytest.mark.parametrize(
        'question, answer, expected_question, expected_answer', question_answer_box_data
    )
    def test_answers_are_relate_to_questions(self, driver, question, answer, expected_question, expected_answer):
        driver.get(base_url)

        home_page = HomePage(driver)
        home_page.wait_for_load_home_page(question)
        home_page.scroll_down(question)
        home_page.wait_for_clickable(question)
        home_page.click_on_question(question)
        actual_question = home_page.get_element_text(question)
        actual_answer = home_page.get_element_text(answer)

        assert actual_answer == expected_answer and actual_question == expected_question
