from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Page

class CartPage(Page):
    ADD_PRODUCT_INTO_CART = (By.XPATH, "//button[contains(text(), 'Add to cart')]")
    ADD_TO_CART_RIGHT = (By.CSS_SELECTOR, '[id*="addToCartButtonOrTextIdFor"][data-test="orderPickupButton"]')
    CHECK_CART = (By.XPATH, "//a[contains(text(), 'View cart & check out')]")
    CART_SUMMARY = (By.CSS_SELECTOR, "[data-test='cart-summary-title']")
    CLICK_CART = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
    CART_EMPTY = (By.XPATH, "//h1[contains(text(), 'Your cart is empty')]")
    def add_product_into_cart(self):
        elements = self.driver.find_elements(*self.ADD_PRODUCT_INTO_CART)
        sleep(5)
        elements[0].click()
        sleep(5)

    def check_cart(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.ADD_TO_CART_RIGHT)).click()
        # self.driver.find_element(*self.ADD_TO_CART_RIGHT).click()
        # sleep(5)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.CHECK_CART)).click()
        assert self.driver.find_element(*self.CART_SUMMARY)

    def click_cart_icon(self):
        self.driver.find_element(*self.CLICK_CART).click()
        sleep(5)

    def verify_cart_empty(self):
        self.driver.find_element(*self.CART_EMPTY)