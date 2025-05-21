import logger
from Test_Scripts.source.selenium_extended import SeleniumExtended
from Test_Scripts.source.locators.Elements_locators import ElementsPageLocators
from Test_Scripts.source.helpers.config_helpers import get_base_url

class ElementsPage(ElementsPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    endpoint = 'elements/'
    def go_to_elements(self):

        base_url = get_base_url()
        elements_page_url = base_url + self.endpoint
        logger.info(f'Going to:  {elements_page_url}')
        self.driver.get(elements_page_url)

    def click_text_box(self):
        self.sl.wait_and_click(self.TextBoxButton)

    endpoint1= 'text-box/'
    def go_to_textbox(self):
        base_url = get_base_url()
        elements_page_url = base_url + self.endpoint1
        logger.info(f'Going to:  {elements_page_url}')
        self.driver.get(elements_page_url)

    def insert_email(self, email):
        self.sl.wait_and_input_text(self.EmailField, email)

    def fill_form(self, fullname, caddress, paddress):
        self.sl.wait_and_input_text(self.FullNameField, fullname)
        self.sl.wait_and_input_text(self.CurrentAddressField, caddress)
        self.sl.wait_and_input_text(self.PermanentAddressField, paddress)

    def fill_form_no_name(self, caddress, paddress):
        self.sl.wait_and_input_text(self.CurrentAddressField, caddress)
        self.sl.wait_and_input_text(self.PermanentAddressField, paddress)

    def fill_form_no_caddress(self, fullname, paddress):
        self.sl.wait_and_input_text(self.FullNameField, fullname)
        self.sl.wait_and_input_text(self.PermanentAddressField, paddress)

    def fill_form_no_paddress(self, fullname, caddress):
        self.sl.wait_and_input_text(self.FullNameField, fullname)
        self.sl.wait_and_input_text(self.CurrentAddressField, caddress)

    def submit_form(self):
        self.sl.wait_element_to_be_visible_and_clickable(self.SubmitButton)

    endpoint2 = 'checkbox/'
    def go_to_checkbox(self):
        base_url = get_base_url()
        elements_page_url = base_url + self.endpoint2
        logger.info(f'Going to:  {elements_page_url}')
        self.driver.get(elements_page_url)

    def click_extender_by_index(self, index):
        extenders = self.driver.find_elements(*ElementsPageLocators.CollapseAllButton)
        if index < len(extenders):
            extenders[index].click()
        else:
            raise IndexError(f"Extender index {index} out of range (found {len(extenders)})")

    def click_checkbox_by_index(self, index):
        checkboxes = self.driver.find_elements(*ElementsPageLocators.Checkboxes)
        if index < len(checkboxes):
            checkboxes[index].click()
        else:
            raise IndexError(f"Checkbox index {index} out of range (found {len(checkboxes)})")

    def check_message_after_checking_boxes(self, selected_checkboxes):
        if isinstance(selected_checkboxes, str):
            selected_checkboxes = [selected_checkboxes]

        expected_items = [item.capitalize() for item in selected_checkboxes]

        expected_text = "You have selected :\n" + "\n".join(expected_items)

        assert expected_text, "The result message does not match the expected text"

    endpoint3 = 'radio-button/'
    def go_to_radiobtn(self):
        base_url = get_base_url()
        elements_page_url = base_url + self.endpoint3
        logger.info(f'Going to:  {elements_page_url}')
        self.driver.get(elements_page_url)

    def select_radio_yes(self):
        self.sl.wait_and_click(self.RadioLabelYes)

    def select_radio_impressive(self):
        self.sl.wait_and_click(self.RadioLabelImpressive)

    def check_message_after_select_radio(self, selected_radio):
        expected_text = f"You have selected {selected_radio[0]}"
        self.sl.wait_until_element_contains_text(self.RadioBoxResultMessage, expected_text)

    def check_no_radio_cant_be_selected(self):
        self.sl.cant_select_radio_button(self.NoRadio, self.RadioLabelNo)

    endpoint4 = 'webtables/'
    def go_to_webtables(self):
        base_url = get_base_url()
        elements_page_url = base_url + self.endpoint4
        logger.info(f'Going to:  {elements_page_url}')
        self.driver.get(elements_page_url)



