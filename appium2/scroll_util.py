import time

from appium.webdriver.common.appiumby import AppiumBy


class scroll_util:

    @staticmethod
    def scrollToTextByAndroidUIAutomator(text, driver):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            "new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text(\"" + text + "\").instance(0))").click()

    @staticmethod
    def swipe_up(howManySwipes, driver):
        for i in range(1, howManySwipes+1):
            driver.swipe(514, 1700, 514, 100, 1000)

    @staticmethod
    def swipe_down(howManySwipes, driver):
        for i in range(1, howManySwipes+1):
            time.sleep(2)
            driver.swipe(514, 200, 514, 1700, 1000)

    @staticmethod
    def swipe_left(howManySwipes, driver):
        for i in range(1, howManySwipes+1):
            driver.swipe(930, 1000, 90, 1000, 1000)

    @staticmethod
    def swipe_right(howManySwipes, driver):
        for i in range(1, howManySwipes+1):
            driver.swipe(90, 1000, 930, 1000, 1000)
