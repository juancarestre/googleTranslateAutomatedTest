from selenium import webdriver
from userinterface.pages.googleMain import SEARCH_BUTTON
from userinterface.pages.googleMain import SEARCH_INPUT_BAR
from userinterface.pages.googleMain import SOURCE_LANGUAGE
from userinterface.pages.googleMain import TARGET_LANGUAGE
import time

def writeOnSearchBar(driver : webdriver.Chrome,**kwargs) -> webdriver:
    driver.find_element_by_xpath(SEARCH_INPUT_BAR).send_keys(kwargs['text'])

def clickOnSearchButton(driver : webdriver.Chrome,**kwargs) -> webdriver:
    driver.find_element_by_xpath(SEARCH_BUTTON).click()

def writeOnSourceLanguageInputThe(driver : webdriver.Chrome,**kwargs) -> webdriver:
    driver.find_element_by_id(SOURCE_LANGUAGE).send_keys(kwargs['text'])

def AsTranslationInAtLeastThreeSecondsThe(driver : webdriver.Chrome,**kwargs) -> webdriver:
    time.sleep(3)
    assert (driver.find_element_by_xpath(TARGET_LANGUAGE).text==kwargs['text'])


if __name__=='__main__':
    writeOnSearchBar()