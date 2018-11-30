import sys
sys.path.append("..")
from actor import Actor
from tasks.customTasks import writeOnSearchBar
from tasks.customTasks import clickOnSearchButton
from tasks.customTasks import writeOnSourceLanguageInputThe
from tasks.customTasks import AsTranslationInAtLeastThreeSecondsThe
from tasks.defaultTasks import clickOn
from tasks.defaultTasks import writeOn
from userinterface.pages.googleMain import SEARCH_BUTTON
from userinterface.pages.googleMain import SEARCH_INPUT_BAR
from abilities.defaultAbilities import browseTheWeb
from browersCons import FIREFOX,CHROME

Juan=None

@given(u'Juan is on Google Translate searching by {Keyword} and using the webbrowser {WebBrowser}')
def step_impl(context,Keyword,WebBrowser):
    global Juan

    Juan=Actor(named='Juan')
    
    #Juan.can(browseTheWeb,withBrowser=CHROME)
    #Juan.can(browseTheWeb,withBrowser=FIREFOX)
    Juan.can(browseTheWeb)

    Juan.wasAbleTo(
        writeOn,clickOn,writableElement=SEARCH_INPUT_BAR,theText=Keyword,clickableElement=SEARCH_BUTTON
    )

@when(u'Juan try to translate from english to spanish {theWord}')
def step_impl(context,theWord):
    Juan.attemptsTo(
        writeOnSourceLanguageInputThe,text=theWord
    )


@then(u'Juan should see {Translation}')
def step_impl(context,Translation):
    Juan.shouldSee(
        AsTranslationInAtLeastThreeSecondsThe,text=Translation
    )
    


    