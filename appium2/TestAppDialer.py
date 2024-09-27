import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

desired_caps = {'deviceName': 'Android', 'platformName': 'Android', 'appPackage': 'com.android.dialer',
                'appActivity': 'com.oneplus.contacts.activities.OPDialtactsActivity',
                'automationName': 'UiAutomator2'}

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
wait = WebDriverWait(driver, 2)
permission_allow_button = wait.until(
    EC.element_to_be_clickable((AppiumBy.ID, 'com.android.packageinstaller:id/permission_allow_button')))
permission_allow_button.click()
floating_action_button = wait.until(
    EC.element_to_be_clickable((AppiumBy.ID, 'com.android.dialer:id/floating_action_button')))
floating_action_button.click()
dial_one = wait.until(
    EC.element_to_be_clickable((AppiumBy.ID, 'com.android.dialer:id/one')))
dial_one.click()
driver.find_element(AppiumBy.ID, 'com.android.dialer:id/two').click()
dial_one.click()
driver.find_element(AppiumBy.ID, 'com.android.dialer:id/dialpad_floating_action_button').click()

time.sleep(10)

driver.quit()
