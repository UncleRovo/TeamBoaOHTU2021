*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser

*** Test Cases ***
Click Browse Link
    Go To Home Page
    Click Link  Selaa vinkkejä
    Browse Page Should Be Open

#Browse Page Contains Original Blogs
#    Go To Browse Page
#    Page Should Contain  ##ADD e.g. author name for test cases
#    Page Should Contain  ##ADD e.g. author name

Browse Page Contains Original Videos
    Go To Browse Page
    Page Should Contain  Rufus
    Page Should Contain  Kings and Generals

Browse Page Contains Original Book
    Go To Browse Page
    Page Should Contain  The Lord of the Rings