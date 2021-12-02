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

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

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