from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target.com')
def open_target_page(context):
    context.driver.get('https://www.target.com/')
    sleep(5)


@when('Click on Sign in')
def click_signin(context):
    context.driver.find_element(By.XPATH, "//*[text()='Sign in']").click()
    sleep(5)

@when('Click on Sign in again')
def click_signin_again(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']").click()
    sleep(5)
@then('Verify Sign in form opened')
def verify_signin_form(context):
    context.driver.find_element(By.XPATH, "//*[text()='Sign into your Target account']")
    sleep(5)
print("test case passed")