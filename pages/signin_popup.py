from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class SigninPopup(Page):
    SIGNIN_POPUP = (By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']")


    def click_signin_again(self):
        self.find_element(*self.SIGNIN_POPUP).click()
