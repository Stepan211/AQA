from selenium import webdriver
import pytest

@pytest.fixture()
def open_browser():
    browser = webdriver.Chrome()              # Открывает браузер
    browser.maximize_window()                 # Открыть окно на полную
    browser.implicitly_wait(4)                # Добавляет не явное ожидание загрузки веб-страницы
    yield browser