
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from tenacity import (retry, stop_after_attempt,wait_fixed, retry_if_exception_type)
import logging
logging.basicConfig(level=logging.INFO)

def selenium_retry(func):
    return retry(
        stop=stop_after_attempt(3),
        wait=wait_fixed(1),
        retry=retry_if_exception_type((TimeoutException, StaleElementReferenceException, ElementClickInterceptedException)),
        reraise = True,
        before_sleep = lambda retry_state: logging.warning(
        f"[Retry] Attempt {retry_state.attempt_number} failed: {retry_state.outcome.exception()}"
        )
    )(func)

class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    @selenium_retry
    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout or self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    @selenium_retry
    def wait_and_click(self, locator, timeout=None):
        timeout = timeout or self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).click()

    @selenium_retry
    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout or self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )

    @selenium_retry
    def wait_until_element_is_visible(self, locator, timeout=None):
        timeout = timeout or self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    @selenium_retry
    def wait_and_get_elements(self, locator, timeout=None, err=None ):
        timeout = timeout or self.default_timeout
        err = err if err else (f'unable to find elements located by"{locator}",'
                               f'after timeout of {timeout}')
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
            return self.driver.find_elements(*locator)
        except TimeoutException:
            raise TimeoutException(err)

    @selenium_retry
    def wait_and_get_element(self, locator, timeout=None, err=None ):
        timeout = timeout or self.default_timeout
        err = err if err else (f'unable to find element located by"{locator}",'
                               f'after timeout of {timeout}')
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return self.driver.find_element(*locator)
        except TimeoutException:
            raise TimeoutException(err)

    @selenium_retry
    def wait_and_get_text(self, locator, timeout=None):
        timeout = timeout or self.default_timeout

        elm = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element_text = elm.text
        return element_text

    @selenium_retry
    def wait_element_to_be_visible_and_clickable(self, locator, timeout=None):
        timeout = timeout or self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        try:

            WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @selenium_retry
    def find_element_position(self, locator, timeout):
        timeout = timeout or self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

        element = self.driver.find_element(*locator)
        assert element.is_displayed(), "Element is not displayed"

        element_position = element.location['y']
        assert element_position < 200, "Element is not at the top of the page"

    @selenium_retry
    def selecting_option_on_dropdown(self, locator, visible_text, timeout=None):
        timeout = timeout or self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator))

        dropdown_element = self.driver.find_element(*locator)
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(visible_text)

    @selenium_retry
    def wait_until_element_is_visible_without_click(self, locator, timeout=None):
        timeout = timeout or self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )



