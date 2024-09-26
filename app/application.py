from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.header import Header
from pages.base_page import Page
from pages.signin_page import SigninPage
from pages.signin_popup import SigninPopup

class Application:
    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.signin_popup = SigninPopup(driver)
        self.signin_page = SigninPage(driver)

