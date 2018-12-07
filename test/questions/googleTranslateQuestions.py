from selenium import webdriver
import time
from userinterface.pages.googleMain import TARGET_LANGUAGE

def checkTheTranslation(driver : webdriver.Chrome,correctTranslation):
    time.sleep(3)
    assert (driver.find_element_by_xpath(TARGET_LANGUAGE).text==correctTranslation)
