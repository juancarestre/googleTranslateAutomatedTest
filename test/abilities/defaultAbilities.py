from tasks.defaultTasks import openBrowser
import sys
sys.path.append("..")
from testConfig import config

def browseTheWeb(**withBrowser):
    deafultUrl=config['DEFAULT_URL']
    webDriverPath=config['WEB_DRIVER']
    sys.path.append(config['BASE_DIR'])

    try:
        if withBrowser['withBrowser']:
            return openBrowser(withBrowser.pop('withBrowser', ''),deafultUrl)
    except KeyError:
        pass
    return openBrowser(webDriverPath,deafultUrl)
