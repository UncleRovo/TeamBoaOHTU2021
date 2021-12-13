*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser And Login User
Suite Teardown  Logout And Close Browser

*** Test Cases ***
Click Add Link
    Go To Home Page
    Click Link  Lisää uusi vinkki
    New Choose Type Page Should Be Open

Add Article
    Go To New Choose Type Page
    Set Type  article
    Click Button  Lisää
    Add Article Page Should Be Open
    Set Title  Art Icle
    Set Author  A. Uthor
    Set Doi  10.1010/10
    Click Button  Lisää
    Go To Browse Page
    Page Should Contain  Art Icle

Add Blog
    Go To New Choose Type Page
    Set Type  blog
    Click Button  Lisää
    Add Blog Page Should Be Open
    Set Title  Test blog
    Set Author  Test author
    Set URL  https://www.google.fi
    Click Button  Lisää
    Go To Browse Page
    Page Should Contain  Test blog

Add Video
    Go To New Choose Type Page
    Set Type  video
    Click Button  Lisää
    Add Video Page Should Be Open
    Set Title  Test video
    Set Channel  Test channel
    Set URL  https://www.google.fi
    Click Button  Lisää
    Go To Browse Page
    Page Should Contain  Test video

Add Book
    Go To New Choose Type Page 
    Set Type  book
    Click Button  Lisää
    Add Book Page Should Be Open
    Set Title  Test book
    Set Author  Test author
    Set Isbn  9780471397120
    Click Button  Lisää
    Go To Browse Page
    Page Should Contain  Test book
