import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from curl import *
from locators import Locators
from data import Credentials


#фикстура настройки браузера
@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1600,900")
    options.add_experimental_option("prefs", {
            "profile.password_manager_leak_detection": False
        })
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.get(main_site)
    yield browser
    browser.quit()

#фикстура для авторизации юзера
@pytest.fixture
def login(driver: WebDriver):
    driver.get(login_page)
    WebDriverWait(driver, 20, poll_frequency=0.1).until(EC.url_to_be(login_page))
    
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(*Credentials.email_user)
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN).send_keys(*Credentials.password_user)
    driver.find_element(*Locators.AUTHORIZATION_SUBMIT_BTN).click()
    
    WebDriverWait(driver, 20, poll_frequency=0.1).until(EC.url_to_be(main_site))

    return driver