import pytest
from Test_Scripts.conftest import init_driver
from Test_Scripts.source.pages.ElementsPage import ElementsPage


@pytest.mark.usefixtures('init_driver')
@pytest.mark.elementswebtablespositive
class TestElementsWebTablesPositive:

    @pytest.mark.webtables1
    def test_click_webtables(self):
        elements_page = ElementsPage(self.driver)
        elements_page.go_to_webtables()

    @pytest.mark.webtables2
    def test_webtables_add_user(self):
        elements_page = ElementsPage(self.driver)
        elements_page.go_to_webtables()

    @pytest.mark.webtables3
    def test_webtables_edit_user(self):
        elements_page = ElementsPage(self.driver)
        elements_page.go_to_webtables()

    @pytest.mark.webtables3
    def test_webtables_delete_user(self):
        elements_page = ElementsPage(self.driver)
        elements_page.go_to_webtables()

    @pytest.mark.webtables5
    def test_webtables_check_users_no(self):
        elements_page = ElementsPage(self.driver)
        elements_page.go_to_webtables()

