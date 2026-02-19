from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from loghelper import generate_registration_data
from data import Credentials
from locators import Locators
from curl import *


class TestRegistration:
    def test_success_registration(self, driver: WebDriver):
        driver.get(register_page)
        driver.find_element(*Locators.NAME_INPUT_REG).send_keys(*Credentials.name_user)
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(*Credentials.email_user)
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys('1234')  # менее 6 символов
        driver.find_element(*Locators.SUBMIT_REG_BUTTON).click()

        error_element = WebDriverWait(driver, 10, poll_frequency=0.1).until(
    EC.visibility_of_element_located(Locators.ERROR_PASSWORD_MESSAGE))
        assert error_element.is_displayed(), "Сообщение об ошибке 'Некорректный пароль' не появилось"