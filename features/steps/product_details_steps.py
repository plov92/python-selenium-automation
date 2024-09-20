from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, '[data-test="@web/VariationComponent"]')

@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)  # Keeping the sleep to wait for the page to load

@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['cream black', 'cream blue', 'cream gold']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(colors)

    for color in colors:
        print(color)
        color.click()
        sleep(2)  # Adding a short sleep to wait for the color change to take effect

        selected_color_element = context.driver.find_element(*SELECTED_COLOR)
        selected_color_text = selected_color_element.text
        print('Current color text', selected_color_text)

        # Ensure the text contains a newline character before splitting
        if '\n' in selected_color_text:
            selected_color = selected_color_text.split('\n')[1]
        else:
            selected_color = selected_color_text  # Fallback to the whole text if no newline

        actual_colors.append(selected_color)
        print('actual_colors list: ', actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
