import os

driverRelPath='/googleTranslate/resources/drivers/chromedriver'

config = {
    'BASE_DIR':os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    'DEFAULT_URL':'https://www.google.com/',
    'WEB_DRIVER': f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}{driverRelPath}'
}

if __name__=="__main__":
    print(config['BASE_DIR'])
