from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page


class SigninPage(Page):
    SIGNIN_TEXT = (By.XPATH, "//span[contains(text(), 'Sign into your Target account')]")
    INPUT_EMAIL = (By.ID, "username")
    INPUT_PASSWORD = (By.ID, "password")
    SIGNIN_WITH_PWD = (By.XPATH, "//span[contains(text(), 'Sign in with password')]")
    PROFILE_BTN = (By.CSS_SELECTOR, '[data-test="@web/AccountLink"]')
    PASSKEYS = (By.XPATH, "//button[contains(text(), 'Create a passkey')]")
    TERMS_CONDITIONS = (By.CSS_SELECTOR, '[aria-label="terms & conditions - opens in a new window"]')

    def verify_signin_form(self):
        actual_text = self.driver.find_element(*self.SIGNIN_TEXT).text
        expected_text = "Sign into your Target account"
        assert actual_text == expected_text


    def input_email(self, email):
        self.find_element(*self.INPUT_EMAIL).send_keys(email)

    def input_password(self, password):
        self.find_element(*self.INPUT_PASSWORD).send_keys(password)

    def click_signin_with_password(self):
        self.initial_url = self.driver.current_url
        print(self.initial_url)
        self.find_element(*self.SIGNIN_WITH_PWD).click()

    def verify_user_logged_in(self):
        sleep(15)
        new_url = self.driver.current_url
        assert new_url != self.initial_url, f"Expected URL to change from '{self.initial_url}', but it did not"


    def click_terms_conditions(self):
        self.find_element(*self.TERMS_CONDITIONS).click()