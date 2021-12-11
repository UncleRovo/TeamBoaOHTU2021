*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser And Login User 
Suite Teardown  Logout And Close Browser

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

Search Matches Only Books
    Go To Browse Page
    Set Search Word  the
    Set Type  book
    Click Button  Hae
    Page Should Contain  The Lord of the Rings
    Page Should Not Contain  Kings and Generals


*** Keywords ***
Set Search Word
    [Arguments]  ${search_word}
    Input Text  key  ${search_word}

Set Type
    [Arguments]  ${type_of_search}
    Select From List By Value  name:type  ${type_of_search}