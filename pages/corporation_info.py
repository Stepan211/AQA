from selenium.webdriver.common.by import By

class CorporationInfoPage:

    def __init__(self, open_browser):
        self.open_browser = open_browser

    def check_subchapter_count(self, count):
        chapter_corporation = self.open_browser.find_elements(By.CSS_SELECTOR, value='a.navigation__link') 
        assert len(chapter_corporation) == count

   