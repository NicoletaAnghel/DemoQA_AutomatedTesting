import pytest
from Test_Scripts.conftest import init_driver
from Test_Scripts.source.pages.ElementsPage import ElementsPage


@pytest.mark.usefixtures('init_driver')
@pytest.mark.elementcheckboxespositive
class TestElementsCheckPositive:

        @pytest.mark.checkbox1
        def test_check_box_page(self):
            elements_page = ElementsPage(self.driver)
            elements_page.go_to_checkbox()

        @pytest.mark.checkbox2
        def test_check_box_extend_options(self):
            elements_page = ElementsPage(self.driver)
            elements_page.go_to_checkbox()
            elements_page.click_extender_by_index(0)
            elements_page.click_extender_by_index(1)
            elements_page.click_extender_by_index(2)
            elements_page.click_extender_by_index(5)

        @pytest.mark.checkbox3
        def test_check_box_extend_documents_options(self):
            elements_page = ElementsPage(self.driver)
            elements_page.go_to_checkbox()
            elements_page.click_extender_by_index(0)
            elements_page.click_extender_by_index(2)
            elements_page.click_extender_by_index(3)
            elements_page.click_extender_by_index(4)

        @pytest.mark.checkbox4
        def test_check_box_select_all_options(self):
            elements_page = ElementsPage(self.driver)
            elements_page.go_to_checkbox()
            elements_page.click_checkbox_by_index(0)
            selected_checkboxes = ['home', 'desktop', 'notes', 'commands', 'documents',
                                   'workspace', 'react', 'angular', 'veu', 'office',
                                   'public', 'private', 'classified', 'general',
                                   'downloads', 'wordFile', 'excelFile']
            elements_page.check_message_after_checking_boxes(selected_checkboxes)

        @pytest.mark.checkbox5
        def test_check_box_select_desktop(self):
            elements_page = ElementsPage(self.driver)
            elements_page.go_to_checkbox()
            elements_page.click_extender_by_index(0)
            elements_page.click_checkbox_by_index(1)
            selected_checkboxes = [ 'desktop', 'notes', 'commands']
            elements_page.check_message_after_checking_boxes(selected_checkboxes)

        @pytest.mark.checkbox6
        def test_check_box_select_public(self):
            elements_page = ElementsPage(self.driver)
            elements_page.go_to_checkbox()
            elements_page.click_extender_by_index(0)
            elements_page.click_extender_by_index(2)
            elements_page.click_extender_by_index(4)
            elements_page.click_checkbox_by_index(5)
            selected_checkboxes = ['public']
            elements_page.check_message_after_checking_boxes(selected_checkboxes)

        @pytest.mark.checkbox6
        def test_check_box_select_public(self):
            elements_page = ElementsPage(self.driver)
            elements_page.go_to_checkbox()
            elements_page.click_extender_by_index(0)
            elements_page.click_extender_by_index(3)
            elements_page.click_checkbox_by_index(5)
            selected_checkboxes = ['excelFile']
            elements_page.check_message_after_checking_boxes(selected_checkboxes)



