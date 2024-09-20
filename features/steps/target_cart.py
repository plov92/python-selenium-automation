from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@given('Open Target main page')
def open_target_page(context):
    context.driver.get('https://www.target.com/')
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'search'))
    )

@when('Search for {product}')
def search_product(context, product):
    # print(item)
    # Search field => enter tea
    context.driver.find_element(By.ID, 'search').send_keys(product)
    # Search button => click
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-test='resultsHeading']"))
    )  # wait for search results page to load


@then('Verify that correct search results shown for {product}')
def verify_results(context, product):
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in actual_result, f'Expected {product}, got actual {actual_result}'


@then('Add one product into Cart')
def add_product_into_cart(context):
    #context.driver.find_element(By.CSS_SELECTOR, "[id*='addToCartButton']").click()
    #elements = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="chooseOptionsButton"]')))
    elements = context.driver.find_elements(By.XPATH, "//button[contains(text(), 'Add to cart')]")
    sleep(5)
    elements[0].click()
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="orderPickupButton"]'))).click()
    #context.driver.find_element(By.CSS_SELECTOR, '[data-test="orderPickupButton"]').click()
    #sleep(5)


@then('Check Cart has item')
def check_cart(context):
    WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'View cart & check out')]"))).click()
    #context.driver.find_element(By.XPATH, "//a[contains(text(), 'View cart & check out')]").click()
    #sleep(5)
    assert context.driver.find_element(By.CSS_SELECTOR, "[data-test='cart-summary-title']")
