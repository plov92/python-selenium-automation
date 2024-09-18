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

driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26hvadid%3D675149237887%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D9012128%26hvnetw%3Dg%26hvpone%3D%26hvpos%3D%26hvptwo%3D%26hvqmt%3De%26hvrand%3D13123008774198399354%26hvtargid%3Dkwd-10573980%26hydadcr%3D28883_14649097%26ref%3Dpd_sl_7j18redljs_e%26tag%3Damazusnavi-20%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
sleep(10)


driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")
driver.find_element(By.ID, "ap_customer_name")
driver.find_element(By.ID, "ap_email")
driver.find_element(By.ID, "ap_password")
driver.find_element(By.ID, "ap_password_check")
driver.find_element(By.ID, "continue")
driver.find_element(By.XPATH, '//a[text()="Conditions of Use"]')
driver.find_element(By.XPATH, '//a[text()="Privacy Notice"]')
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")

sleep(10)

print('Test case passed')
driver.quit()