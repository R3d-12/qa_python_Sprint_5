from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from loghelper import generate_registration_data
from locators import Locators
from curl import *


class TestRegistration:
    def test_success_registration(self, driver):
        name, email, password = generate_registration_data()
        driver.get(register_page)
        driver.find_element(*Locators.NAME_INPUT_REG).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT_REG).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_REG).send_keys(password)
        driver.find_element(*Locators.SUBMIT_REG_BUTTON).click()

        WebDriverWait(driver, 20, poll_frequency=0.1).until(EC.url_to_be(login_page))
        assert driver.current_url == login_page, "Ошибка, регистрация не получислась"