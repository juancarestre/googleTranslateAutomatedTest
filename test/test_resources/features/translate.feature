Feature: Translate from ENG to SPA and SPA to ENG

    Insert a text on the transtale input and click the transtale button to get the translation from english to spanish and from spanish to english

    Scenario Outline: English to Spanish: Insert as <text> on the transtale input and see as translation the text in spanish <theTranslation>

        Given Juan is on Google Translate searching by <Keyword> and using the webbrowser <WebBrowser>
        When Juan try to translate from english to spanish: <text>
        Then Juan should see <theTranslation>

        Examples:
        | WebBrowser | Keyword                    |  text | theTranslation |
        | CHROME     | traductor ingles a espanol |  cat     | gato           |
        | FIREFOX    | traductor ingles a espanol |  dog     | perro          |

    Scenario Outline: Spanish to English: Insert as <text> on the transtale input and see as translation the text in english <theTranslation>

        Given Juan is on Google Translate searching by <Keyword> and using the webbrowser <WebBrowser>
        When Juan try to translate from english to spanish: <text>
        Then Juan should see <theTranslation>

        Examples:
        | WebBrowser | Keyword |  text | theTranslation |
        | CHROME     | translate spanish to  english |   gato    |   cat       |
        | FIREFOX    | translate spanish to  english |   perro   |   dog       |