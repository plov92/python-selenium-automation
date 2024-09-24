from pages.base_page import Page
from time import sleep

class MainPage(Page):
    def open_target_page(self):
        self.open('https://www.target.com/')

