import time

import pytest
from Test_Scripts.conftest import init_driver
from Test_Scripts.source.helpers.generate_random_address_details import RandomInputs
from Test_Scripts.source.helpers.generate_random_email_and_username import generate_random_email_and_password
from Test_Scripts.source.pages.ElementsPage import ElementsPage


@pytest.mark.usefixtures('init_driver')
@pytest.mark.elementstextpositive
class TestElementsTextPositive:

    @pytest.mark.testbox1
    def test_click_text_box(self):
        elements_page = ElementsPage(self.driver)
        elements_page.go_to_elements()
        elements_page.click_text_box()

    @pytest.mark.testbox2
    def test_complete_form_with_data(self):
        elements_page = ElementsPage(self.driver)
        elements_page.go_to_textbox()

        email = generate_random_email_and_password()
        elements_page.insert_email(email ['email'])

        random_inputs = RandomInputs()
        random_form_input = RandomInputs()
        fullname = random_form_input.random_names()
        caddress = random_inputs.random_address()
        paddress =random_inputs.random_address()
        elements_page.fill_form(fullname, caddress, paddress)

    @pytest.mark.testbox3
    def test_submit_form(self):
        elements_page = ElementsPage(self.driver)
        elements_page.go_to_textbox()

        email = generate_random_email_and_password()
        elements_page.insert_email(email ['email'])

        random_inputs = RandomInputs()
        random_form_input = RandomInputs()
        fullname = random_form_input.random_names()
        caddress = random_inputs.random_address()
        paddress =random_inputs.random_address()
        elements_page.fill_form(fullname, caddress, paddress)

        elements_page.submit_form()


@pytest.mark.usefixtures('init_driver')
@pytest.mark.elementstextnegative
class TestElementsTextNegative:

    @pytest.mark.testbox_negative1
    def test_complete_form_no_fullname(self):
        elements_page = ElementsPage(self.driver)
        elements_page.go_to_textbox()

        email = generate_random_email_and_password()
        elements_page.insert_email(email['email'])

        random_inputs = RandomInputs()
        caddress = random_inputs.random_address()
        paddress = random_inputs.random_address()
        elements_page.fill_form_no_name(caddress, paddress)

        elements_page.submit_form()


    @pytest.mark.testbox_negative2
    def test_complete_form_no_email(self):
        elements_page = ElementsPage(self.driver)
        elements_page.go_to_textbox()

        random_inputs = RandomInputs()
        random_form_input = RandomInputs()
        fullname = random_form_input.random_names()
        caddress = random_inputs.random_address()
        paddress = random_inputs.random_address()
        elements_page.fill_form(fullname, caddress, paddress)

        elements_page.submit_form()

    @pytest.mark.testbox_negative3
    def test_complete_form_no_current_address(self):
        elements_page = ElementsPage(self.driver)
        elements_page.go_to_textbox()

        email = generate_random_email_and_password()
        elements_page.insert_email(email['email'])

        random_inputs = RandomInputs()
        random_form_input = RandomInputs()
        fullname = random_form_input.random_names()
        paddress = random_inputs.random_address()
        elements_page.fill_form_no_caddress(fullname, paddress)

        elements_page.submit_form()

    @pytest.mark.testbox_negative4
    def test_complete_form_no_perm_address(self):
        elements_page = ElementsPage(self.driver)
        elements_page.go_to_textbox()

        email = generate_random_email_and_password()
        elements_page.insert_email(email['email'])

        random_inputs = RandomInputs()
        random_form_input = RandomInputs()
        fullname = random_form_input.random_names()
        caddress = random_inputs.random_address()
        elements_page.fill_form_no_paddress(fullname, caddress)

        elements_page.submit_form()
