from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target Circle page')
def open_circle(context):
    context.driver.get('https://www.target.com/circle')
    sleep(5)

@when('Identify benefit cells')
def identify_benefit_cells(context):
    context.benefit_cells = context.driver.find_elements(By.CSS_SELECTOR, '.cell-item-content')

@then('Verify there are 10 benefit cells')
def verify_benefit_cells(context):
    benefit_cells = context.benefit_cells
    assert len(benefit_cells) == 10, f'Expected 10 benefit cells and got {len(benefit_cells)}'
