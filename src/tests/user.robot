*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Click Register Link
    Go To Home Page
    Click Link  Rekisteröi uusi käyttäjä
    Register A New User Page Should Be Open

Register Should Succeed With Valid Username And Password
    Go To Home Page
    Click Link  Rekisteröi uusi käyttäjä
    Register A New User Page Should Be Open
    Set Username  Joonatan13
    Set Password  salasana24
    Submit Registration
    Register Should Succeed  Olet kirjautunut käyttäjätunnuksella: Joonatan13
    Click Link  Kirjaudu ulos


Register Should Fail With A Username That Is Already In Use
    Go To Home Page
    Click Link  Rekisteröi uusi käyttäjä
    Register A New User Page Should Be Open
    Set Username  Joonatan13
    Set Password  salasana24
    Submit Registration
    Registering Should Fail With Message  Virhe: Rekisteröinti ei onnistunut

Logging In Should Work With A Valid Username And Password
    Go To Home Page
    Click Link  Kirjaudu sisään
    Login Page Should Be Open
    Set Username  Joonatan13
    Set Password  salasana24
    Submit Credentials
    Login Should Succeed  Olet kirjautunut käyttäjätunnuksella: Joonatan13
    Click Link  Kirjaudu ulos

Login Should Not With Invalid Username
    Go To Home Page
    Click Link  Kirjaudu sisään
    Login Page Should Be Open
    Set Username  Joonatan
    Set Password  salasana24
    Submit Credentials
    Login Should Fail With Message  Kirjautuminen ei onnistunut

Login Should Not With Invalid Password
    Go To Home Page
    Click Link  Kirjaudu sisään
    Login Page Should Be Open
    Set Username  Joonatan13
    Set Password  salasana
    Submit Credentials
    Login Should Fail With Message  Kirjautuminen ei onnistunut


*** Keywords ***
Registering Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}