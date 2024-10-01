from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page
from selenium.webdriver.support.ui import Select

class TargetHelpPage(Page):

    DROPDOWN_MENU = (By.CSS_SELECTOR, 'select[id*="ViewHelpTopics"]')
    GIFTCARDS_OPTION = (By.XPATH, '//h1[text()=" Target GiftCard balance"]')
    def open_target_help(self):
        self.open('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')
        sleep(5)

    def choose_gift_cards(self):
        dd = self.find_element(*self.DROPDOWN_MENU)
        select = Select(dd)
        select.select_by_value('Gift Cards')

    def verify_gift_cards(self):
        self.wait_for_element_to_appear(*self.GIFTCARDS_OPTION)
        sleep(5)


