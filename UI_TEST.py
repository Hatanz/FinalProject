from UIFunctions import *
from selenium import webdriver
import pytest


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    return driver


class TestZivUIBankTesting:

    @pytest.mark.usefixtures('driver')
    def test_Balance(self,driver):
        actual = balance_change(driver) != 404
        assert actual, 'the balance need to change'

    @pytest.mark.usefixtures('driver')
    def test_transaction_change(self,driver):
        actual = transaction_change(driver) != 404
        assert actual, 'the transaction need to be seen'

    @pytest.mark.usefixtures('driver')
    def test_all_transaction_approve(self,driver):
        actual = all_transaction_approve(driver) != 404
        assert actual, 'all the transaction need to be correct'

    @pytest.mark.usefixtures('driver')
    def test_delete_acc(self,driver):
        actual = delete_acc(driver) != 404
        assert actual, 'Neville need to be deleted'
