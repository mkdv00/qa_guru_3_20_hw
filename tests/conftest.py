import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene.support.shared import browser

from config import settings
from wikipedia.utils import attachments


@pytest.fixture
def browser_config():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        "app": settings.app_id,
        'bstack:options': {
            "projectName": "Wiki mobile",
            "buildName": "browserstack-build-1-DEMO",
            "sessionName": "BStack session",
            "userName": settings.bs_username,
            "accessKey": settings.bs_access_key
        }
    })

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    browser.config.timeout = 10

    yield

    attachments.add_video(browser)
    browser.quit()
