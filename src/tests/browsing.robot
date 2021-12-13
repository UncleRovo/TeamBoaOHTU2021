*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser And Login User
Suite Teardown  Logout And Close Browser

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
    Alert Should Be Present
    Page Should Not Contain  Building blogs
    
Browse Page Should Not Contain Original Data If Logging In As A New User
    Go To Home Page
    Click Link  Kirjaudu ulos
    Click Link  Rekisteröi uusi käyttäjä
    Set Username  Jyrmymeister
    Set Password  jjjpassword
    Submit Registration
    Go To Browse Page
    Page Should Not Contain  James B. Rew
    Page Should Not Contain  blogger
    Page Should Not Contain  Rufus
    Page Should Not Contain  The Lord of the Rings
    
Browse Page Should Contain A Newly Added Blog With The New User
    Go To New Choose Type Page
    Set Type  blog
    Click Button  Lisää
    Add Blog Page Should Be Open
    Set Title  Better Privacy
    Set Author  DuckDuckGo
    Set URL  https://www.duckduckgo.com
    Click Button  Lisää
    Go To Browse Page
    Page Should Contain  Better Privacy

Browse Page Should Contain Appropriate Data When Logging In As The Original User
    Go To Home Page
    Click Link  Kirjaudu ulos
    Click Link  Kirjaudu sisään
    Set Username  Kasper123
    Set Password  Jesper123
    Submit Credentials
    Go To Browse Page
    Page Should Contain  James B. Rew
    Page Should Contain  Rufus
    Page Should Contain  The Lord of the Rings
    Page Should Not Contain  Better Privacy
