from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from locators import Locators
from curl import *

# переход в профиль авторизованного пользователя
def test_personal_account_of_an_authorized_user(driver,login):
    driver.find_element(*Locators.ACCOUNT_LINK).click()
    WebDriverWait(driver, 20, poll_frequency=0.1).until(EC.url_to_be(account_profile))
    assert driver.current_url == account_profile, "Ошибка"
