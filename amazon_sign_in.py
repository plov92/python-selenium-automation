from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(10)
driver.find_element(By.XPATH, '//i[@aria-label="Amazon"]')

driver.find_element(By.ID, 'ap_email')
driver.find_element(By.ID, 'continue')
driver.find_element(By.XPATH, '//a[text()="Conditions of Use"]')
driver.find_element(By.XPATH, "//span[contains(text(), 'Need help?')]")
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-expand']").click()
driver.find_element(By.XPATH, "//a[contains(text(), 'Forgot your password?')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Other issues with Sign-In')]")
driver.find_element(By.ID, 'createAccountSubmit')
sleep(10)

print('Test case passed')
driver.quit()