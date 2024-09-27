import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {'deviceName': 'Android', 'platformName': 'Android', 'browserName': 'Chrome',
                'automationName': 'UiAutomator2',
                'appium:chromedriverExecutable': "/Users/anirudhaggarwal/Downloads/appium-chromedriver-mac-arm64/chromedriver"}

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
driver.get("http://google.com")
# driver.find_element(AppiumBy.XPATH, '//*[@name="q"]').send_keys("Hello Appium")  # only find_element
driver.find_element(AppiumBy.CSS_SELECTOR, '*[name="q"]').send_keys("Hello Appium !!!")
print(driver.title)

time.sleep(2)

driver.quit()
