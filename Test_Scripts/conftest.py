
import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.chrome.service import Service as ChService
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions
import os
import allure



@pytest.fixture(scope='class')
def init_driver(request):
    supported_browsers = ['chrome', 'ch', 'headlesschrome', 'firefox', 'ff', 'headlessfirefox']

    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception('The environment variable "BROWSER" must be set.')

    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f'Provided browser "{browser}" is not supported. Supported: {supported_browsers}')

    driver = None

    if browser in ('chrome', 'ch'):
        chrome_options = ChOptions()
        chrome_prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }
        chrome_options.add_experimental_option("prefs", chrome_prefs)
        driver = webdriver.Chrome(service=ChService(), options=chrome_options)

    elif browser in ('headlesschrome'):
        chrome_options = ChOptions()
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(service=ChService(), options=chrome_options)

    elif browser in ('firefox', 'ff'):
        firefox_profile = FirefoxProfile()
        firefox_profile.set_preference("dom.webnotifications.enabled", False)
        firefox_profile.set_preference("signon.rememberSignons", False)
        firefox_options = FFOptions()
        driver = webdriver.Firefox(service=FFService(), options=firefox_options)

    elif browser in ('headlessfirefox'):
        firefox_options = FFOptions()
        firefox_options.add_argument('--headless')
        firefox_options.add_argument('--disable-gpu')
        firefox_options.add_argument('--no-sandbox')
        driver = webdriver.Firefox(service=FFService(), options=firefox_options)

    if driver:
        driver.maximize_window()
        request.cls.driver = driver
        yield driver
        driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":

        xfail = hasattr(report, "wasxfail")

        if (report.skipped and xfail) or (report.failed and not xfail):
            is_frontend_test = True if 'init_driver' in item.fixturenames else False

            if is_frontend_test:
                results_dir = os.environ.get("RESULTS_DIR", r"C:\Users\nicol\PycharmProjects\DemoQA_AutomatedTesting\Test_Scripts\reports")
                if not results_dir:
                    raise Exception("Environment variable 'RESULTS_DIR' must be set.")

                screen_shot_path = os.path.join(results_dir, item.name + '.png')
                driver_fixture = item.funcargs['request']
                allure.attach(driver_fixture.cls.driver.get_screenshot_as_png(),
                              name='screenshot',
                              attachment_type=allure.attachment_type.PNG)



