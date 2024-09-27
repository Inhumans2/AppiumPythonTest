import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {'deviceName': 'Android', 'platformName': 'Android', 'appPackage': 'com.oneplus.calculator',
                'appActivity': 'com.oneplus.calculator.Calculator',
                'automationName': 'UiAutomator2'}

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
driver.implicitly_wait(5)
# wait = WebDriverWait(driver, 2)
driver.find_element(AppiumBy.ID, 'com.oneplus.calculator:id/digit_2').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'plus').click()
driver.find_element(AppiumBy.ID, 'com.oneplus.calculator:id/digit_8').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'equals').click()

result = driver.find_element(AppiumBy.ID, 'com.oneplus.calculator:id/result').text
driver.find_element(AppiumBy.ID, 'com.oneplus.calculator:id/clr').click()
print(result)
assert int(result) == 8

time.sleep(5)

driver.quit()
