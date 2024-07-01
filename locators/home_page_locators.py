from selenium.webdriver.common.by import By


class HomePageLocator:
    question_0 = [By.ID, 'accordion__heading-0']
    answer_0 = [By.XPATH, './/*[@id="accordion__panel-0"]/p']
    expected_question_0 = 'Сколько это стоит? И как оплатить?'
    expected_answer_0 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    question_1 = [By.ID, 'accordion__heading-1']
    answer_1 = [By.XPATH, './/*[@id="accordion__panel-1"]/p']
    expected_question_1 = 'Хочу сразу несколько самокатов! Так можно?'
    expected_answer_1 = ('Пока что у нас так: один заказ — один самокат. '
                         'Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')
    question_2 = [By.ID, 'accordion__heading-2']
    answer_2 = [By.XPATH, './/*[@id="accordion__panel-2"]/p']
    expected_question_2 = 'Как рассчитывается время аренды?'
    expected_answer_2 = ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
                         'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
                         'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
    question_3 = [By.ID, 'accordion__heading-3']
    answer_3 = [By.XPATH, './/*[@id="accordion__panel-3"]/p']
    expected_question_3 = 'Можно ли заказать самокат прямо на сегодня?'
    expected_answer_3 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    question_4 = [By.ID, 'accordion__heading-4']
    answer_4 = [By.XPATH, './/*[@id="accordion__panel-4"]/p']
    expected_question_4 = 'Можно ли продлить заказ или вернуть самокат раньше?'
    expected_answer_4 = ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку '
                         'по красивому номеру 1010.')
    question_5 = [By.ID, 'accordion__heading-5']
    answer_5 = [By.XPATH, './/*[@id="accordion__panel-5"]/p']
    expected_question_5 = 'Вы привозите зарядку вместе с самокатом?'
    expected_answer_5 = ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже '
                         'если будете кататься без передышек и во сне. Зарядка не понадобится.')
    question_6 = [By.ID, 'accordion__heading-6']
    answer_6 = [By.XPATH, './/*[@id="accordion__panel-6"]/p']
    expected_question_6 = 'Можно ли отменить заказ?'
    expected_answer_6 = ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. '
                         'Все же свои.')
    question_7 = [By.ID, 'accordion__heading-7']
    answer_7 = [By.XPATH, './/*[@id="accordion__panel-7"]/p']
    expected_question_7 = 'Я жизу за МКАДом, привезёте?'
    expected_answer_7 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
