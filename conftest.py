from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options    



@pytest.fixture()
def open_browser():
    options = Options()
    options.add_argument('--headless=new')            # Используем новый фоновый режим для стабильного рендеринга
    options.add_argument('--window-size=1920,1080')   # Принудительно задаем Full HD разрешение до старта браузера
# Дополнительные флаги против зависаний в headless-режиме
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    open_browser = webdriver.Chrome(options=options)   # Открывает браузер
    open_browser.implicitly_wait(3)                    # Добавляет не явное ожидание загрузки веб-страницы
    yield open_browser
    open_browser.close()