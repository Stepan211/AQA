from selenium.webdriver.common.by import By     # Импорт из Seleniuma всех способов поиска элементов 
from pages.homepages import HomePage
from pages.feedback import FeedbackPage
from pages.corporation_info import CorporationInfoPage

# Пишем Selenium тесты для UI
# Сутью selenium тестов найти в HTML коде уникальный признак/имя когда обращаемся, чтобы он понял

def test_chapter_feedback(open_browser):
    homepage = HomePage(open_browser)     # Именно на этом шаге сохраняется значения браузера в self.open_browser описанный на странице homepage
    homepage.open()
    homepage.click_feedback()
    feedbackpage = FeedbackPage(open_browser)
    feedbackpage.check_title_is('Обратная связь')


def test_chapter_corporation(open_browser):
    homepage = HomePage(open_browser)
    homepage.open()
    homepage.click_corporation_info()
    corporation_info = CorporationInfoPage(open_browser)
    corporation_info.check_subchapter_count(4)
