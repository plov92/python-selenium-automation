from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@given('Open Target main page')
def open_target_page(context):
    context.app.main_page.open_target_page()

@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product(product)


@then('Verify that correct search results shown for {product}')
def verify_results(context, product):
    context.app.search_results_page.verify_results(product)


@then('Add one product into Cart')
def add_product_into_cart(context):
    context.app.cart_page.add_product_into_cart()


@then('Check Cart has item')
def check_cart(context):
    context.app.cart_page.check_cart()

@when('Click on Cart icon')
def click_cart_icon(context):
    context.app.cart_page.click_cart_icon()

@then('Verify “Your cart is empty” message is shown')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()