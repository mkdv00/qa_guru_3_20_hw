import os

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selene.support.shared import browser

from wikipedia.utils import attachments


@pytest.fixture
def browser_config():
    load_dotenv()
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        "app": os.getenv('app_id'),
        'bstack:options': {
            "projectName": "Wiki mobile",
            "buildName": "browserstack-build-1-DEMO",
            "sessionName": "BStack session",
            "userName": os.getenv('bs_username'),
            "accessKey": os.getenv('bs_access_key')
        }
    })

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    browser.config.timeout = 10

    yield

    attachments.add_video(browser)
    browser.quit()
