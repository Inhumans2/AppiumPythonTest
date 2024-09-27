import time
from pathlib import Path

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from appium2.scroll_util import scroll_util

desired_caps = {'deviceName': 'Android', 'platformName': 'Android',
                'appPackage': 'in.amazon.mShop.android.shopping',
                'appActivity': 'com.amazon.mShop.home.HomeActivity',
                'automationName': 'UiAutomator2'}

# desired capabilities mein 'app' : str(Path().absolute().parent)+'\\app\\amazon.apk' where pathlib use

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
wait = WebDriverWait(driver, 2)
driver.implicitly_wait(5)
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Select English').click()
driver.find_element(AppiumBy.ID, 'in.amazon.mShop.android.shopping:id/continue_button').click()
time.sleep(6)
window_cart = wait.until(EC.element_to_be_clickable(
    (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='in.amazon.mShop.android.shopping:id/cart_count']")))
# window_cart = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="in.amazon.mShop.android.shopping:id/cart_count"]')
window_cart_count = window_cart.text
cart_count_num = int(window_cart_count)
if cart_count_num > 0:
    driver.find_element(AppiumBy.XPATH,
                        '(//android.widget.ImageView[@resource-id="in.amazon.mShop.android.shopping:id/bottom_tab_button_icon"])[3]').click()
    time.sleep(3)
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Delete"]').click()
    time.sleep(5)
driver.find_element(AppiumBy.ID, 'in.amazon.mShop.android.shopping:id/chrome_search_hint_view').click()
driver.find_element(AppiumBy.ID, 'in.amazon.mShop.android.shopping:id/rs_search_src_text').send_keys('Mobile Cover')
driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="mobile cover"]').click()
time.sleep(5)
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Add to cart").instance(0))').click()
scroll_util.scrollToTextByAndroidUIAutomator("Add to cart", driver)
time.sleep(2)
# scroll_util.swipe_up(4, driver)
# scroll_util.swipe_down(4, driver)
# driver.swipe(514,600,514,200,1000)    this is bottom to above
# driver.swipe(514,200,514,600,1000)    this is above to bottom
driver.find_element(AppiumBy.XPATH,
                    '(//android.widget.ImageView[@resource-id="in.amazon.mShop.android.shopping:id/bottom_tab_button_icon"])[3]').click()
driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Proceed to Buy (1 item)"]').click()
time.sleep(5)
driver.quit()
