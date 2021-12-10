*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser And Login User 
Suite Teardown  Logout And Close Browser

*** comment ***
Nyt pitää vielä putsata tietokanta ennen testejä ja venkslata kirjautumisen ja rekisteröitymisen välillä alustuksessa!

*** Test Cases ***
Search Matches One Item
    Go To Browse Page
    Set Search Word  coffee
    Click Button  Hae
    Page Should Contain  How to brew a cup of coffee
    Page Should Not Contain  Helsinki

Search Matches Two Items
    Go To Browse Page
    Set Search Word  the
    Click Button  Hae
    Page Should Contain  Kings and Generals
    Page Should Contain  The Lord of the Rings
    Page Should Not Contain  Helsinki


*** Keywords ***
Set Search Word
    [Arguments]  ${search_word}
    Input Text  key  ${search_word}