from selenium import webdriver
def openBrowser(driverPath,defaultUrl):
    browser=webdriver.Chrome(executable_path=r''+driverPath)
    browser.get(defaultUrl)
    return browser