from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('Open Target Help page')
def open_target_help(context):
    context.app.target_help_page.open_target_help()


@when('Choose Gift Cards from Browse Help dropdown')
def choose_gift_cards(context):
    context.app.target_help_page.choose_gift_cards()


@then('Verify Gift Card Page opened')
def verify_gift_cards(context):
    context.app.target_help_page.verify_gift_cards()