from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('Open Target.com')
def open_target_page(context):
    context.app.main_page.open_target_page()
    sleep(5)


@when('Click on Sign in')
def click_signin(context):
    context.app.header.click_signin()
    sleep(5)

@when('Click on Sign in again')
def click_signin_again(context):
    context.app.signin_popup.click_signin_again()
    sleep(5)
@then('Verify Sign in form opened')
def verify_signin_form(context):
    context.app.signin_page.verify_signin_form()
    sleep(5)

@then('Input email {email}')
def input_email(context, email):
    context.app.signin_page.input_email(email)

@then('Input password {password}')
def input_password(context, password):
    context.app.signin_page.input_password(password)


@then('Click on Sign in with password')
def click_signin_with_password(context):
    context.app.signin_page.click_signin_with_password()


@then('Verify user is logged in')
def verify_user_logged_in(context):
    context.app.signin_page.verify_user_logged_in()

