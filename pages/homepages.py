from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, open_browser):
        self.open_browser = open_browser

    def open(self):
        self.open_browser.get('https://elar.ru/')

    def click_feedback(self):
        elar = self.open_browser.find_element(By.LINK_TEXT, value="Обратная связь")   
        elar.click()

    def click_corporation_info(self):
        elar = self.open_browser.find_element(By.LINK_TEXT, value="О корпорации") 
        elar.click()
