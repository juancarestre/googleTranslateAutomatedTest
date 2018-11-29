import sys
sys.path.append("..")
from testConfig import config
sys.path.append(config['BASE_DIR'])
from tasks.defaultTasks import openBrowser

from tasks.customTasks import writeOnSearchBar
from tasks.customTasks import clickOnSearchButton


class Actor(object):
    def __init__(self,name):
        self.name=name
        self.deafultUrl=config['DEFAULT_URL']
        self.webDriverPath=config['WEB_DRIVER']
        sys.path.append(config['BASE_DIR'])
        self.browser=openBrowser(self.webDriverPath,self.deafultUrl)
        

    def attemptsTo(self,*args,**kwargs):
        self.performs(*args,**kwargs)
    def wasAbleTo(self,*args,**kwargs):
        self.performs(*args,**kwargs)
    def shouldSee(self,*args,**kwargs):
        self.performs(*args,**kwargs)
        self.finish()

    def performs(self,*args,**kwargs):
        for arg in args:
            execute=arg(self.browser,**kwargs)
    
    def finish(self,*args,**kwargs):
        self.browser.close()
    
if __name__=='__main__':
    Juan = Actor('Juan')
    Juan.attemptsTo(
        writeOnSearchBar,clickOnSearchButton,text='traductor'
    )
