from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target main page')
def open_target_page(context):
    context.driver.get('https://www.target.com/')
    sleep(5)


@when('Click on Cart icon')
def click_on_target_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test*="@web/CartLink"]').click()
    sleep(5)


@then('Verify "Your cart is empty" message')
def verify_cart_is_empty(context):
    context.driver.find_element(By.XPATH, "//*[text()='Your cart is empty']")
    sleep(5)
print("test case passed")