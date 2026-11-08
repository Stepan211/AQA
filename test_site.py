import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By     # Импорт из Seleniuma всех способов поиска элементов 

@pytest.fixture()
def open_browser():
    browser = webdriver.Chrome()              # Открывает браузер
    browser.maximize_window()                 # Открыть окно на полную
    yield browser
    


# Пишем Selenium тесты для UI

def test_open_feedback(open_browser):
    open_browser.get('https://elar.ru/')     # Переходим на нужную страницу
    elar = open_browser.find_element(By.LINK_TEXT, value="Обратная связь")
    elar.click()
    title = open_browser.find_element(By.CSS_SELECTOR, value='h2')
    assert title.text == 'Обратная связь'