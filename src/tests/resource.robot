*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.5 seconds
${HOME URL}  http://${SERVER}
${BROWSE URL}  http://${SERVER}/browse
${NEW URL}  http://${SERVER}/new
${ADD URL}  http://${SERVER}/add

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Browse Page Should Be Open
    Page Should Contain  Tallennetut lukuvinkit

New Page Should Be Open
    Page Should Contain  Lisää uusi...

Go To Home Page
    Go To  ${HOME URL}