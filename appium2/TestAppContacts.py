import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {'deviceName': 'Android', 'platformName': 'Android', 'appPackage': 'com.android.contacts',
                'appActivity': 'com.oneplus.contacts.activities.OPPeopleActivity',
                'automationName': 'UiAutomator2'}

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
wait = WebDriverWait(driver, 2)  # Explicit Wait

add_contact_button = wait.until(
    EC.element_to_be_clickable((AppiumBy.ID, 'com.android.contacts:id/floating_action_button')))
add_contact_button.click()
choose_account = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.TextView[@text='PHONE']")))
choose_account.click()
driver.find_element(AppiumBy.ID, 'com.android.contacts:id/edit_fullName').send_keys('Anirudh')
driver.hide_keyboard()
phone_number_edit = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, "//android.widget.EditText[@text='Phone']")))
phone_number_edit.send_keys('9560165760')
driver.find_element(AppiumBy.ID, 'com.android.contacts:id/menu_save').click()
time.sleep(2)

driver.quit()
