from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
import pytest

from locators import Locators
from curl import *

#клик по "Соусы" и "Начинки"
@pytest.mark.parametrize('click_section', [Locators.SAUCES_TAB, Locators.FILLINGS_TAB])
def test_section(driver, click_section):
    driver.find_element(*click_section).click()

    tab_element = driver.find_element(*click_section)
    class_attribute = tab_element.get_attribute('class')

    assert 'tab_tab_type_current__2BEPc' in class_attribute, "Вкладка не активна"
    
#клик по "Булки"
def test_section_buns(driver):
    driver.find_element(*Locators.SAUCES_TAB).click() #предусловие
    driver.find_element(*Locators.BUNS_TAB).click()
    WebDriverWait(driver, 10).until(lambda d: 'tab_tab_type_current__2BEPc' in d.find_element(*Locators.BUNS_TAB).get_attribute('class'))

    tab_element = driver.find_element(*Locators.BUNS_TAB)
    class_attribute = tab_element.get_attribute('class')

    assert 'tab_tab_type_current__2BEPc' in class_attribute, "Вкладка не активна"