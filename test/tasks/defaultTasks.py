from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
options = Options()

def openBrowser(driverPath,defaultUrl):
    if 'geckodriver' in driverPath: browser=webdriver.Firefox(capabilities=DesiredCapabilities().FIREFOX,executable_path=r''+driverPath)
    elif 'chromedriver' in driverPath: browser=webdriver.Chrome(desired_capabilities=DesiredCapabilities().CHROME,executable_path=r''+driverPath)

    browser.get(defaultUrl)
    return browser

def clickOn(driver : webdriver.Chrome,**elementString) -> webdriver:
    driver.find_element_by_xpath(elementString['clickableElement']).click()
def writeOn(driver : webdriver.Chrome,**kwargs) -> webdriver:
    driver.find_element_by_xpath(kwargs['writableElement']).send_keys(kwargs['theText'])

