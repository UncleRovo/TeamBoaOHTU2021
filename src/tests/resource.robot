*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.5 seconds
${HOME URL}  http://${SERVER}
${BROWSE URL}  http://${SERVER}/browse
${NEW_CHOOSE_TYPE URL}  http://${SERVER}/new_choose_type
${ADD ARTICLE URL}  http://${SERVER}/new_article
${REGISTER PAGE}  http://${SERVER}/register

*** Keywords ***
Open And Configure Browser And Register User
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To Home Page
    Click Link  Rekisteröi uusi käyttäjä
    Register A New User Page Should Be Open
    Set Username  Kasper123
    Set Password  Jesper123
    Submit Registration
    Register Should Succeed  Olet kirjautunut käyttäjätunnuksella: Kasper123

Open And Configure Browser And Login User
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To Home Page
    Click Link  Kirjaudu sisään
    Login Page Should Be Open
    Set Username  Kasper123
    Set Password  Jesper123
    Submit Credentials
    Login Should Succeed  Olet kirjautunut käyttäjätunnuksella: Kasper123

Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Logout And Close Browser
    Go To Home Page
    Click Link  Kirjaudu ulos
    Close Browser

Browse Page Should Be Open
    Page Should Contain  Tallennetut lukuvinkit

New Choose Type Page Should Be Open
    Page Should Contain  Lisää uusi...

Add Article Page Should Be Open
    Page Should Contain  Lisää uusi artikkeli

Add Video Page Should Be Open
    Page Should Contain  Lisää uusi video

Add Blog Page Should Be Open
    Page Should Contain  Lisää uusi blogi

Add Book Page Should Be Open
    Page Should Contain  Lisää uusi kirja

Go To Home Page
    Go To  ${HOME URL}

Go To Browse Page
    Go To  ${BROWSE URL}

Go To New Choose Type Page 
    Go To  ${NEW_CHOOSE_TYPE URL}

Go To Register Page
    Go To  ${REGISTER PAGE}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Submit Registration
    Click Button  Register

Register A New User Page Should Be Open
    Page Should Contain  Lisää uusi käyttäjä

Register Should Succeed
    [Arguments]  ${message}
    User Is Logged In  ${message}

User Is Logged In
    [Arguments]  ${message}
    Page Should Contain  ${message}

Login Should Succeed
    [Arguments]  ${message}
    User Is Logged In  ${message}

Login Page Should Be Open
    Page Should Contain  Kirjaudu sisään

Submit Credentials
    Click Button  Login