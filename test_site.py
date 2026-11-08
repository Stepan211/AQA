import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By     # Импорт из Seleniuma всех способов поиска элементов 

@pytest.fixture()
def open_browser():
    browser = webdriver.Chrome()              # Открывает браузер
    browser.maximize_window()                 # Открыть окно на полную
    browser.implicitly_wait(4)                # Добавляет не явное ожидание загрузки веб-страницы
    yield browser
    


# Пишем Selenium тесты для UI
# Сутью selenium тестов найти в HTML коде уникальный признак/имя когда обращаемся, чтобы он понял

def test_chapter_feedback(open_browser):
    open_browser.get('https://elar.ru/')                                    # Переходим на нужную страницу
    elar = open_browser.find_element(By.LINK_TEXT, value="Обратная связь")  # Ищем по совпадению в тексте один элемент
    elar.click()                                                            # Кликаем 
    title = open_browser.find_element(By.CSS_SELECTOR, value='h2')          
    assert title.text == 'Обратная связь'

def test_chapter_corporation(open_browser):
    open_browser.get('https://elar.ru/')
    elar = open_browser.find_element(By.LINK_TEXT, value="О корпорации")
    elar.click()
    chapter_corporation = open_browser.find_elements(By.CSS_SELECTOR, value='a.navigation__link')  # Ищем по совпадению в тексте список элементов, которые попадают под эти условия
    assert len(chapter_corporation) == 4                                                           # Проверяю что, количество разделов 4 