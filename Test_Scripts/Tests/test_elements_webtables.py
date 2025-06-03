import time

import pytest
from Test_Scripts.conftest import init_driver
from Test_Scripts.source.helpers.generate_random_address_details import RandomInputs
from Test_Scripts.source.helpers.generate_random_email_and_username import generate_random_email_and_password
from Test_Scripts.source.pages.ElementsPage import ElementsPage



@pytest.mark.usefixtures('init_driver')
@pytest.mark.elementswebtablespositive
class TestElementsWebTablesPositive:

    @pytest.mark.webtables1
    def test_click_web_tables(self):
        elements_page = ElementsPage(self.driver)
        elements_page.go_to_webtables()

    @pytest.mark.webtables2
    def test_web_tables_add_user(self):
        elements_page = ElementsPage(self.driver)
        elements_page.go_to_webtables()
        elements_page.click_add_employee()

        random_inputs = RandomInputs()
        fname = random_inputs.random_names()
        elements_page.add_fname(fname)
        lname = random_inputs.random_names()
        elements_page.add_lname(lname)

        email = generate_random_email_and_password()
        elements_page.add_email(email ['email'])

        age = random_inputs.random_age()
        elements_page.add_age(age)

        salary = random_inputs.random_salary()
        elements_page.add_salary(salary)

        department = random_inputs.random_depart_name()
        elements_page.add_department(department)

        elements_page.click_submit_btn()


    @pytest.mark.webtables3
    def test_web_tables_edit_first_user(self):
        elements_page = ElementsPage(self.driver)
        elements_page.go_to_webtables()
        elements_page.click_edit_btn_first_user()

        elements_page.delete_salary()

        random_inputs = RandomInputs()
        salary = random_inputs.random_salary()
        elements_page.add_salary(salary)

        elements_page.click_submit_btn()
        elements_page.check_salary_change(salary)


    @pytest.mark.webtables4
    def test_web_tables_delete_second_user(self):
        elements_page = ElementsPage(self.driver)
        elements_page.go_to_webtables()
        elements_page.delete_second_user()




