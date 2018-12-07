from selenium import webdriver

def clickOn(driver : webdriver.Chrome,**elementString) -> webdriver:
    driver.find_element_by_xpath(elementString['clickableElement']).click()
def writeOn(driver : webdriver.Chrome,**kwargs) -> webdriver:
    driver.find_element_by_xpath(kwargs['writableElement']).send_keys(kwargs['theText'])