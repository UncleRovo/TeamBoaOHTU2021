*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser And Login User
Suite Teardown  Logout And Close Browser

*** Test Cases ***

Update Article
    Go To Browse Page
    Click Button  class:edit_article
    Page Should Contain  Muokkaa lukuvinkkiä
    Set Title  updated title
    Set Tag  tag1;tag2
    Click Button  tallenna
    Go To Browse Page
    Page Should Contain  updated title

Update Video
    Go To Browse Page
    Click Button  class:edit_video
    Page Should Contain  Muokkaa videovinkkiä
    Set Channel  updated channel
    Set Tag  tag3;tag4
    Click Button  tallenna
    Go To Browse Page
    Page Should Contain  updated channel