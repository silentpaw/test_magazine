import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def test_magazine(browser):
     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
     browser.get(link)
     button = WebDriverWait(browser, 100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
    
