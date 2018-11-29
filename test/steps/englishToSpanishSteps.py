import sys
sys.path.append("..")
from actor import Actor
from tasks.customTasks import writeOnSearchBar
from tasks.customTasks import clickOnSearchButton
from tasks.customTasks import writeOnSourceLanguageInputThe
from tasks.customTasks import AsTranslationInAtLeastThreeSecondsThe


Juan=None

@given(u'Juan is on Google Translate searching by {Keyword}')
def step_impl(context,Keyword):
    global Juan
    Juan=Actor('Juan')
    Juan.wasAbleTo(
        writeOnSearchBar,clickOnSearchButton,text=Keyword
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


    