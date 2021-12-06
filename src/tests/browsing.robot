*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Click Browse Link
    Go To Home Page
    Click Link  Selaa vinkkejä
    Browse Page Should Be Open

Browse Page Contains Original Articles
    Go To Browse Page
    Page Should Contain  James B. Rew
    Page Should Contain  Helsingin kirjasto

Browse Page Contains Original Blogs
    Go To Browse Page
    Page Should Contain  Building blogs
    Page Should Contain  blogger

Browse Page Contains Original Videos
    Go To Browse Page
    Page Should Contain  Rufus
    Page Should Contain  Kings and Generals

Browse Page Contains Original Book
    Go To Browse Page
    Page Should Contain  The Lord of the Rings

Browse Page Should Not Contain A Blog After It Is Hidden
    Go To Browse Page
    Page Should Contain  Building blogs
    Click Button  Poista
    Page Should Not Contain  Building blogs