*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.5 seconds
${HOME URL}  http://${SERVER}
${BROWSE URL}  http://${SERVER}/browse
${NEW URL}  http://${SERVER}/new  #HUOM! NEW MUUTETTU NEW_CHOOSE_TYPE
${ADD URL}  http://${SERVER}/add

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Browse Page Should Be Open
    Page Should Contain  Tallennetut lukuvinkit

New Page Should Be Open   # HUOM! NEW MUUTETTU NEW_CHOOSE_TYPE
    Page Should Contain  Lisää uusi...

Add Page Should Be Open   #ADD-sivu merged with new_choose_type
    Page Should Contain  Otsikko

Go To Home Page
    Go To  ${HOME URL}

Go To Browse Page
    Go To  ${BROWSE URL}

Go To Add Page    #ADD-sivu merged with new_choose_type
    Go To  ${ADD URL}   #ADD-sivu merged with new_choose_type