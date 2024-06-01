from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


import pytest
import os
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.maximize_window()
    yield driver 

def test_login_negatif(driver):
    driver.find_element(By.ID,'txtUsername').send_keys('sarah')
    driver.find_element(By.ID,'txtPassword').send_keys('admin12345')
    driver.find_element(By.ID, 'btnLogin').click()
    time.sleep(5)
    assert 'Invalid credentials' in driver.find_element(By.ID,'spanMessage').text
    time.sleep(3)
    data = driver.find_element(By.ID,'spanMessage').text
    driver.assertEqual(data,'Invalid credentials')


def test_login(driver):
    driver.find_element(By.ID,'txtUsername').send_keys('Admin')
    driver.find_element(By.ID,'txtPassword').send_keys('admin123')
    driver.find_element(By.ID, 'btnLogin').click()
    time.sleep(3)
    assert 'Welcome' in driver.find_element(By.ID,'Welcome').text
    driver.close()



