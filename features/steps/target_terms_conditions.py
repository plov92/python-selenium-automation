from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window()
    print('Original window: ', context.original_window)
    sleep(5)


@when('Click on Target terms and conditions link')
def click_terms_conditions(context):
    context.app.signin_page.click_terms_conditions()
    sleep(2)

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.app.base_page.switch_to_new_window()
    sleep(2)

@then('Verify Terms and Conditions page is opened')
def verify_terms_conditions_url(context):
    context.app.base_page.verify_partial_url('terms-conditions')

@then('User can close new window and switch back to original')
def close_new_window_and_switch_to_original(context):
    context.app.base_page.close()
    sleep(10)


