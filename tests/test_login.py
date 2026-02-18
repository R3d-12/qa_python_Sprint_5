from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from locators import Locators
from curl import *
from data import Credentials


def wait_visible(driver, locator, timeout=20):
    WebDriverWait(driver, timeout, poll_frequency=0.1).until(
        EC.visibility_of_element_located(locator)
    )


@pytest.mark.parametrize('log_button', [Locators.LOGIN_TO_ACCOUNT_BTN, Locators.ACCOUNT_LINK])
def test_login_on_the_main_page(driver, log_button):
    """Вход по кнопкам «Войти в аккаунт» или «Личный кабинет» на главной: переход на страницу входа, авторизация."""
    driver.find_element(*log_button).click()
    wait_visible(driver, Locators.AUTHORIZATION_SUBMIT_BTN)
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(*Credentials.email_user)
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN).send_keys(*Credentials.password_user)
    driver.find_element(*Locators.AUTHORIZATION_SUBMIT_BTN).click()
    WebDriverWait(driver, 20, poll_frequency=0.1).until(EC.url_to_be(main_site))
    assert WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(Locators.ORDER_BTN)
    ), "Ошибка, авторизация не прошла"


def test_login_from_registration_form(driver):
    """Вход по ссылке «Войти» в форме регистрации: переход на страницу входа, авторизация."""
    driver.get(register_page)
    driver.find_element(*Locators.LOGIN_LINK_IN_FORM).click()
    wait_visible(driver, Locators.AUTHORIZATION_SUBMIT_BTN)
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(*Credentials.email_user)
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN).send_keys(*Credentials.password_user)
    driver.find_element(*Locators.AUTHORIZATION_SUBMIT_BTN).click()
    WebDriverWait(driver, 20, poll_frequency=0.1).until(EC.url_to_be(main_site))
    assert WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(Locators.ORDER_BTN)
    ), "Ошибка, авторизация не прошла"


def test_login_from_password_recovery_form(driver):
    """Вход по ссылке «Войти» в форме восстановления пароля: переход на страницу входа, авторизация."""
    driver.get(password_recovery)
    driver.find_element(*Locators.RECOVERY_LOGIN_LINK).click()
    wait_visible(driver, Locators.AUTHORIZATION_SUBMIT_BTN)
    driver.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(*Credentials.email_user)
    driver.find_element(*Locators.PASSWORD_INPUT_LOGIN).send_keys(*Credentials.password_user)
    driver.find_element(*Locators.AUTHORIZATION_SUBMIT_BTN).click()
    WebDriverWait(driver, 20, poll_frequency=0.1).until(EC.url_to_be(main_site))
    assert WebDriverWait(driver, 3).until(
        EC.visibility_of_element_located(Locators.ORDER_BTN)
    ), "Ошибка, авторизация не прошла"