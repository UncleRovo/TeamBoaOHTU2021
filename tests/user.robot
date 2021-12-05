*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Click Register Link
    Go To Home Page
    Click Link  Rekisteröi uusi käyttäjä
    Register A New User Should Be Open

Register Should Succeed With Valid Username And Password
    Go To Home Page
    Click Link  Rekisteröi uusi käyttäjä
    Register A New User Should Be Open
    Set Username  Joonatan13
    Set Password  salasana24
    Submit Registration
    Register Should Succeed
    Click Link  Kirjaudu ulos
    

Register Should Fail With A Username That Is Already In Use
    Go To Home Page
    Click Link  Rekisteröi uusi käyttäjä
    Register A New User Should Be Open
    Set Username  Joonatan13
    Set Password  salasana24
    Submit Registration
    Registering Should Fail With Message  Virhe: Rekisteröinti ei onnistunut


*** Keywords ***
Register A New User Should Be Open
    Page Should Contain  Lisää uusi käyttäjä

Registering Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Submit Registration
    Click Button  Rekisteröi

Register Should Succeed
    Page Should Contain  Olet kirjautunut käyttäjätunnuksella: Joonatan13
