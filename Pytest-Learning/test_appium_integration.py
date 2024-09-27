import time

import allure
import pytest
from allure_commons.types import AttachmentType
from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep.call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)


def get_data():
    return [

        ["Delhi"],
        ["Dubai"],
        ["Nira la"],

    ]


def setup_function():
    """global appium_service
    appium_service = AppiumService()
    appium_service.start()"""

    desired_caps = {'deviceName': 'Android', 'platformName': 'Android',
                    'appPackage': 'com.goibibo',
                    'appActivity': 'com.goibibo.common.HomeActivity',
                    'automationName': 'UiAutomator2'}

    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    global driver
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)
    driver.implicitly_wait(10)


def teardown_function():
    time.sleep(3)
    driver.quit()
    # appium_service.stop()


@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.parametrize("city", get_data())
def test_goibibo_login(city):
    driver.find_element(AppiumBy.ID, 'com.truecaller:id/cl_primary_cta').click()
    time.sleep(2)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Close').click()
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Hotels']").click()
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Search Anywhere']").click()
    time.sleep(2)

    search_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.EditText"))
    )
    search_field.send_keys(city[0])

    if city[0] == 'Delhi':
        city_name = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, ', India')]")
    elif city[0] == 'Dubai':
        city_name = driver.find_element(AppiumBy.XPATH,
                                        "//android.widget.TextView[contains(@text, ', United Arab Emirates')]")

    time.sleep(2)
    print(city_name)
    assert city[0] in city_name.text
    allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)