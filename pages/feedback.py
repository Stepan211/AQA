from selenium.webdriver.common.by import By

class FeedbackPage:

    def __init__(self, open_browser):
        self.open_browser = open_browser

    def check_title_is(self, expected_title):
        element = self.open_browser.find_element(By.CSS_SELECTOR, value='h2')         
        assert element.text == expected_title