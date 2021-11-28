*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Click Add Link
    Go To Home Page
    Click Link  Lisää uusi vinkki
    New Page Should Be Open

Add Article
    Go To Add Page
    Set Type  article
    Click Button  Hae
    Add Page Should Be Open
    Set Title  Test title
    Set Author  Test author
    Set URL  www.google.fi
    Click Button  Lisää
    Go To Browse Page
    Page Should Contain  Test title

*** Keywords ***
Set Type
    [Arguments]  ${type_of_new}
    Select From List By Value  name:type  ${type_of_new}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set URL
    [Arguments]  ${url}
    Input Text  url  ${url}