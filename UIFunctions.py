from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/'
selectors = {'CL': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button',
             'ML': 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button',
             'Customer btm': 'body > div > div > div.ng-scope > div > div.center > button:nth-child(3)',
             'Neville delete': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(5) > td:nth-child(5) > button',
             'Neville postcode': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(5) > td:nth-child(3)',
             'Hermoine Granger': '#userSelect > option:nth-child(2)',
             'Harry Potter': '#userSelect > option:nth-child(3)',
             'Ron Weasly': '#userSelect > option:nth-child(4)',
             'Albus Dumbledore': '#userSelect > option:nth-child(5)',
             'Neville Longbottom': '#userSelect > option:nth-child(6)',
             'Login btm': 'body > div > div > div.ng-scope > div > form > button',
             'Transactions': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(1)',
             'Deposit': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)',
             'Deposit text box': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input',
             'Deposit Btm': 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button',
             'Withdrawl': 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(3)',
             'account number': 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(1)',
             'Balance': 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)',
             'Amount': '#anchor0 > td:nth-child(2)',
             'back btm': 'body > div > div > div.ng-scope > div > div.fixedTopBox > button:nth-child(1)',
             'Amount2': '#anchor1 > td:nth-child(2)',
             'Amount3': '#anchor2 > td:nth-child(2)',
             'customer table': 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table'
             }


# 1
def balance_change(driver):
    driver.get(url)
    time.sleep(2)
    customer_login = driver.find_element(By.CSS_SELECTOR, selectors['CL'])
    customer_login.click()
    time.sleep(2)
    harry = driver.find_element(By.CSS_SELECTOR, selectors['Harry Potter'])
    harry.click()
    time.sleep(2)
    login_btm = driver.find_element(By.CSS_SELECTOR, selectors['Login btm'])
    login_btm.click()
    time.sleep(2)
    deposit = driver.find_element(By.CSS_SELECTOR, selectors['Deposit'])
    deposit.click()
    time.sleep(2)
    deposit_tb = driver.find_element(By.CSS_SELECTOR, selectors['Deposit text box'])
    deposit_tb.click()
    deposit_tb.send_keys('250')
    time.sleep(2)
    deposit_btm = driver.find_element(By.CSS_SELECTOR, selectors['Deposit Btm'])
    deposit_btm.click()
    time.sleep(5)
    balance = driver.find_element(By.CSS_SELECTOR, selectors['Balance'])
    print(balance.text)
    new_balance = int(balance.text)
    if new_balance >= 250:
        return new_balance
    else:
        return 404


# 2
def transaction_change(driver):
    driver.get(url)
    time.sleep(2)
    c_login = driver.find_element(By.CSS_SELECTOR, selectors['CL'])
    c_login.click()
    time.sleep(2)
    harry_p = driver.find_element(By.CSS_SELECTOR, selectors['Harry Potter'])
    harry_p.click()
    time.sleep(2)
    login_btms = driver.find_element(By.CSS_SELECTOR, selectors['Login btm'])
    login_btms.click()
    time.sleep(2)
    deposit = driver.find_element(By.CSS_SELECTOR, selectors['Deposit'])
    deposit.click()
    time.sleep(2)
    deposit_tb = driver.find_element(By.CSS_SELECTOR, selectors['Deposit text box'])
    deposit_tb.click()
    deposit_tb.send_keys('1500')
    time.sleep(2)
    deposit_btm = driver.find_element(By.CSS_SELECTOR, selectors['Deposit Btm'])
    deposit_btm.click()
    time.sleep(5)
    transactions = driver.find_element(By.CSS_SELECTOR, selectors['Transactions'])
    transactions.click()
    time.sleep(2)
    amount = driver.find_element(By.CSS_SELECTOR, selectors['Amount'])
    print(amount.text)
    time.sleep(3)
    amounts = int(amount.text)
    if amounts >= 1500:
        return amount.text
    else:
        return 404


# 3
def all_transaction_approve(driver):
    driver.get(url)
    time.sleep(2)
    c_l = driver.find_element(By.CSS_SELECTOR, selectors['CL'])
    c_l.click()
    time.sleep(2)
    h_p = driver.find_element(By.CSS_SELECTOR, selectors['Harry Potter'])
    h_p.click()
    time.sleep(2)
    login = driver.find_element(By.CSS_SELECTOR, selectors['Login btm'])
    login.click()
    time.sleep(2)
    deposit = driver.find_element(By.CSS_SELECTOR, selectors['Deposit'])
    deposit.click()
    time.sleep(2)
    deposit_tb = driver.find_element(By.CSS_SELECTOR, selectors['Deposit text box'])
    deposit_tb.click()
    deposit_tb.send_keys('200')
    time.sleep(2)
    deposit_btm = driver.find_element(By.CSS_SELECTOR, selectors['Deposit Btm'])
    deposit_btm.click()
    time.sleep(5)
    deposit_tb = driver.find_element(By.CSS_SELECTOR, selectors['Deposit text box'])
    deposit_tb.click()
    deposit_tb.send_keys('200')
    time.sleep(2)
    deposit_btm = driver.find_element(By.CSS_SELECTOR, selectors['Deposit Btm'])
    deposit_btm.click()
    time.sleep(5)
    deposit_tb = driver.find_element(By.CSS_SELECTOR, selectors['Deposit text box'])
    deposit_tb.click()
    deposit_tb.send_keys('200')
    time.sleep(2)
    deposit_btm = driver.find_element(By.CSS_SELECTOR, selectors['Deposit Btm'])
    deposit_btm.click()
    time.sleep(5)
    transaction_1 = driver.find_element(By.CSS_SELECTOR, selectors['Transactions'])
    transaction_1.click()
    time.sleep(3)
    amount_1 = driver.find_element(By.CSS_SELECTOR, selectors['Amount'])
    print(amount_1.text)
    amount_2 = driver.find_element(By.CSS_SELECTOR, selectors['Amount2'])
    print(amount_2.text)
    amount_3 = driver.find_element(By.CSS_SELECTOR, selectors['Amount3'])
    print(amount_3.text)

    amount1 = int(amount_1.text)
    amount2 = int(amount_2.text)
    amount3 = int(amount_3.text)

    if amount1 == amount2 and amount1 == amount3:
        return amount1 and amount2 and amount3
    else:
        return 404


# 4
def delete_acc(driver):
    driver.get(url)
    time.sleep(2)
    manager_acc = driver.find_element(By.CSS_SELECTOR, selectors['ML'])
    manager_acc.click()
    time.sleep(2)
    customers_btm = driver.find_element(By.CSS_SELECTOR, selectors['Customer btm'])
    customers_btm.click()
    time.sleep(2)
    neville_delete = driver.find_element(By.CSS_SELECTOR, selectors['Neville delete'])
    neville_delete.click()
    time.sleep(3)
    customer_table = driver.find_element(By.CSS_SELECTOR, selectors['customer table'])
    if 'Neville' in customer_table.text:
        return 404
    else:
        return customer_table
