import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.select import Select

desired_caps = {'deviceName': 'Android', 'platformName': 'Android', 'browserName': 'Chrome',
                'automationName': 'UiAutomator2',
                'appium:chromedriverExecutable': "/Users/anirudhaggarwal/Downloads/appium-chromedriver-mac-arm64/chromedriver"}

"""appium_service = AppiumService()
appium_service.start()

print(appium_service.is_running)
print(appium_service.is_listening)"""

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
driver.get("http://wikipedia.org")
dropdown = driver.find_element(AppiumBy.CSS_SELECTOR, "#searchLanguage")
select = Select(dropdown)
select.select_by_value("hi")
print(driver.title)

options = driver.find_elements(AppiumBy.TAG_NAME, "option")
print(len(options))

for option in options:
    print("Text is : ", option.text, "There Attributes are : ", option.get_attribute("Lang"))

time.sleep(10)

driver.quit()

# appium_service.stop()
