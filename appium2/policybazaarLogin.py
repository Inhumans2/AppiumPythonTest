import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {'deviceName': 'Android', 'platformName': 'Android',
                'appPackage': 'com.policybazaar',
                'appActivity': 'com.policybazaar.MainActivity',
                'automationName': 'UiAutomator2'}

capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
driver.implicitly_wait(10)

driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
time.sleep(5)
driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Login via Mobile Number"]').click()
time.sleep(2)
driver.find_element(AppiumBy.ID, 'com.google.android.gms:id/cancel').click()
driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Mobile Number').click()
driver.press_keycode(16)
driver.press_keycode(12)
driver.press_keycode(13)
driver.press_keycode(7)
driver.press_keycode(8)
driver.press_keycode(13)
driver.press_keycode(12)
driver.press_keycode(14)
driver.press_keycode(13)
driver.press_keycode(7)
time.sleep(2)
driver.hide_keyboard()
time.sleep(2)
driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Continue"]/android.view.ViewGroup').click()
time.sleep(2)
driver.execute_script("mobile: shell", {
    'command': 'am',
    'args': ['start', '-n', 'com.google.android.apps.messaging/.ui.ConversationListActivity']
})
elements = driver.find_elements(AppiumBy.ID, 'com.google.android.apps.messaging:id/conversation_snippet')
if elements:
    elements[0].click()
else:
    print("No elements found with the given ID.")

time.sleep(2)
driver.open_notifications()
time.sleep(2)
truecaller_notification = driver.find_element(AppiumBy.ID, 'com.truecaller:id/textOtp')
if truecaller_notification:
    touch_action = TouchAction(driver)
    touch_action.long_press(truecaller_notification).move_to(x=1000, y=100).release().perform()
else:
    print("True caller notification not found.")

time.sleep(2)
messages = driver.find_elements(AppiumBy.ID, 'message_text')
if messages:
    text = messages[-1].text
    print(text)
else:
    print("No messages found.")

time.sleep(2)
driver.quit()
