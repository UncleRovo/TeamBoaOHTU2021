*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Click Browse Link
    Go To Home Page
    Click Link  Selaa vinkkejä
    Browse Page Should Be Open