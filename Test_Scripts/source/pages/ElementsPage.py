import logger

from Test_Scripts.source.selenium_extended import SeleniumExtended
from Test_Scripts.source.locators.Elements_locators import ElementsPageLocators
from Test_Scripts.source.helpers.config_helpers import get_base_url

class ElementsPage(ElementsPageLocators):

    endpoint = '/elements/'
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_elements(self):

        base_url = get_base_url()
        elements_page_url = base_url + self.endpoint
        logger.info(f'Going to:  {elements_page_url}')
        self.driver.get(elements_page_url)

    def click_text_box(self):
        self.sl.wait_and_click(self.TestBoxButton)


