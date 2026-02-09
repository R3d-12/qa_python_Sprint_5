from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from locators import Locators
from curl import *
from data import Credentials

# вход по кнопкам "Войти" в аккаунт и ЛК
@pytest.mark.parametrize('log_button', [Locators.LOGIN_TO_ACCOUNT_BTN, Locators.ACCOUNT_LINK])
def test_login_on_the_main_page(driver,log_button):
    driver.find_element(*log_button).click()
    WebDriverWait(driver, 20, poll_frequency=0.1).until(EC.url_to_be(login_page))
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(*Credentials.email_user)
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN).send_keys(*Credentials.password_user)
    driver.find_element(*Locators.AUTHORIZATION_SUBMIT_BTN).click()

    WebDriverWait(driver, 20, poll_frequency=0.1).until(EC.url_to_be(main_site))
    assert driver.current_url == main_site, "Ошибка, авторизация не прошла"

# вход по кнопке в форме регистрации
def test_login_from_registration_form(driver):
    driver.get(register_page)
    driver.find_element(*Locators.LOGIN_LINK).click()
    WebDriverWait(driver, 20, poll_frequency=0.1).until(EC.url_to_be(login_page))
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(*Credentials.email_user)
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN).send_keys(*Credentials.password_user)
    driver.find_element(*Locators.AUTHORIZATION_SUBMIT_BTN).click()

    WebDriverWait(driver, 20, poll_frequency=0.1).until(EC.url_to_be(main_site))
    assert driver.current_url == main_site, "Ошибка, авторизация не прошла"

# вход по кнопке в форме восстановления пароля
def test_login_from_password_recovery_form (driver):
    driver.get(password_recovery)
    driver.find_element(*Locators.RECOVERY_LOGIN_LINK).click()
    WebDriverWait(driver, 20, poll_frequency=0.1).until(EC.url_to_be(login_page))
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(*Credentials.email_user)
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN).send_keys(*Credentials.password_user)
    driver.find_element(*Locators.AUTHORIZATION_SUBMIT_BTN).click()

    WebDriverWait(driver, 20, poll_frequency=0.1).until(EC.url_to_be(main_site))
    assert driver.current_url == main_site, "Ошибка, авторизация не прошла"