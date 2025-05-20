import pytest
from Test_Scripts.conftest import init_driver
from Test_Scripts.source.pages.ElementsPage import ElementsPage


@pytest.mark.usefixtures('init_driver')
@pytest.mark.elementsradiobtnpositive
class TestElementsRadioBtnPositive:

        @pytest.mark.radiobtn1
        def test_radiobtn_page(self):
            elements_page = ElementsPage(self.driver)
            elements_page.go_to_radiobtn()

        @pytest.mark.radiobtn2
        def test_radiobtn_select_yes(self):
            elements_page = ElementsPage(self.driver)
            elements_page.go_to_radiobtn()
            elements_page.select_radio_yes()
            selected_radio = 'Yes'
            elements_page.check_message_after_select_radio(selected_radio)

        @pytest.mark.radiobtn3
        def test_radiobtn_select_impressive(self):
            elements_page = ElementsPage(self.driver)
            elements_page.go_to_radiobtn()
            elements_page.select_radio_impressive()
            selected_radio = 'Impressive'
            elements_page.check_message_after_select_radio(selected_radio)

        @pytest.mark.radiobtn4
        def test_radiobtn_select_no(self):
            elements_page = ElementsPage(self.driver)
            elements_page.go_to_radiobtn()
            elements_page.check_no_radio_cant_be_selected()


