import time

from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium2.scroll_util import scroll_util

desired_caps = {'deviceName': 'Android', 'platformName': 'Android',
                'appPackage': 'com.nis.app',
                'appActivity': 'com.nis.app.ui.activities.HomeActivity',
                'automationName': 'UiAutomator2'""",'noReset: True'"""}

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
wait = WebDriverWait(driver, 2)
driver.implicitly_wait(10)

driver.find_element(AppiumBy.XPATH,
                    '//android.widget.CheckBox[@resource-id="com.nis.app:id/language_checkbox" and @text="English (English)"]').click()
time.sleep(2)
driver.find_element(AppiumBy.ID, 'com.nis.app:id/continue_reading_button').click()
"""if driver.find_element(AppiumBy.XPATH, '//androidx.viewpager.widget.ViewPager[@resource-id="com.nis.app:id/card_list"]/android.view.ViewGroup'):
    driver.find_element(AppiumBy.ID, 'com.nis.app:id/buttonGoogleLogin').click()"""
time.sleep(5)
scroll_util.swipe_up(4, driver)
time.sleep(2)
"""window_click = wait.until(EC.element_to_be_clickable(
    (AppiumBy.ID, 'com.nis.app:id/news_card')))
window_click.click()"""
time.sleep(2)
scroll_util.swipe_down(3, driver)

time.sleep(2)
scroll_util.swipe_left(2, driver)
driver.find_element(AppiumBy.ID, 'com.nis.app:id/toolbar_back').click()
time.sleep(2)
scroll_util.swipe_right(1, driver)
time.sleep(2)
scroll_util.swipe_left(1, driver)
time.sleep(5)
driver.quit()
