from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from locators import Locators
from curl import *

# переход из ЛК в конструктор по клику "Конструктор" и на логотип
@pytest.mark.parametrize('in_constructor', [Locators.CONSTRUCTOR_LINK, Locators.LOGO_LINK])
def test_transitions_from_personal_account(driver,login, in_constructor):
    driver.find_element(*Locators.ACCOUNT_LINK).click()
    WebDriverWait(driver, 20, poll_frequency=0.1).until(EC.url_to_be(account_profile))
    driver.find_element(*in_constructor).click()
    WebDriverWait(driver, 20, poll_frequency=0.1).until(EC.url_to_be(main_site))
    assert driver.current_url == main_site, "ошибка"