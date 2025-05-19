import pytest
from Test_Scripts.conftest import init_driver
from Esitetest.source.helpers.config_helpers import get_base_url

@pytest.mark.usefixtures('init_driver')

class TestElementsCheckPositive:

        @pytest.mark.checkbox
        def test_check_box(self):
            print('ss')


class TestElementsCheckNegative:

    @pytest.mark.checkbox_negative
    def test_check_box(self):
        print('ss')