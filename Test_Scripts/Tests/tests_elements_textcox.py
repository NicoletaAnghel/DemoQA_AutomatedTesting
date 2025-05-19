import pytest
from Test_Scripts.conftest import init_driver
from Test_Scripts.source.pages.ElementsPage import ElementsPage

@pytest.mark.usefixtures('init_driver')

@pytest.mark.elementstextpositive
class TestElementsTextPositive:

        @pytest.mark.testbox1
        def test_complete_form(self):
            elements_page = ElementsPage(self.driver)
            elements_page.click_text_box()


        @pytest.mark.testbox
        def test_submit_form(self):
            print('config')

        @pytest.mark.testbox
        def test_complete_form(self):
            print('config')

@pytest.mark.elementstextnegative
class TestElementsTextNegative:

    @pytest.mark.testbox_negative
    def test_complete_form_no_fullname(self):
        print('config')

    @pytest.mark.testbox_negative
    def test_complete_form_no_email(self):
        print('config')

    @pytest.mark.testbox_negative
    def test_complete_form_no_current_address(self):
        print('config')

    @pytest.mark.testbox_negative
    def test_complete_form_no_perm_address(self):
        print('config')

