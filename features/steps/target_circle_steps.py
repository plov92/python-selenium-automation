from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@given('Open Target Circle page')
def open_circle(context):
    context.driver.get('https://www.target.com/circle')
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.cell-item-content'))
    )

@when('Identify benefit cells')
def identify_benefit_cells(context):
    context.benefit_cells = context.driver.find_elements(By.CSS_SELECTOR, '.cell-item-content')

@then('Verify there are 10 benefit cells')
def verify_benefit_cells(context):
    benefit_cells = context.benefit_cells
    assert len(benefit_cells) == 10, f'Expected 10 benefit cells and got {len(benefit_cells)}'