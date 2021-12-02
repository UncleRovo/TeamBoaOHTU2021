*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Click Add Link
    Go To Home Page
    Click Link  Lisää uusi vinkki
    New Choose Type Page Should Be Open

Add Blog
    Go To New Choose Type Page
    Set Type  blog
    Click Button  Lisää
    Add Blog Page Should Be Open
    Set Title  Test blog
    Set Author  Test author
    Set URL  https://www.google.fi
    Click Button  Lisää
    Go To Browse Page
    Page Should Contain  Test blog

Add Video
    Go To New Choose Type Page
    Set Type  video
    Click Button  Lisää
    Add Video Page Should Be Open
    Set Title  Test video
    Set Channel  Test channel
    Set URL  https://www.google.fi
    Click Button  Lisää
    Go To Browse Page
    Page Should Contain  Test video

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

Set Channel
    [Arguments]  ${channel}
    Input Text  channel  ${channel}

Set URL
    [Arguments]  ${url}
    Input Text  url  ${url}