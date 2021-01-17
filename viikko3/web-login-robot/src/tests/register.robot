*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Validate

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kalle
    Set Password And Password Confirmation  kalle456  kalle456
    Click Register Button
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password And Password Confirmation  abcdefg123  abcdefg123
    Click Register Button
    Register Should Fail With Message  Username must be at least three characters long

Register With Valid Username And Too Short Password
    Set Username  esko
    Set Password And Password Confirmation  a  a
    Click Register Button
    Register Should Fail With Message  Password must be at least eight characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  username
    Set Password And Password Confirmation  abcdefg123  ajgj84gj89
    Click Register Button
    Register Should Fail With Message  Password and password confirmation do not match

Login After Successful Registration
    Set Username  kallee
    Set Password And Password Confirmation  kalle456  kalle456
    Click Register Button
    Welcome Page Should Be Open
    Go To Login Page
    Login Page Should Be Open
    Set Username  kallee
    Set Password  kalle456
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  k
    Set Password And Password Confirmation  kalle456  kalle456
    Click Register Button
    Register Should Fail With Message  Username must be at least three characters long
    Go To Login Page
    Login Page Should Be Open
    Set Username  k
    Set Password  kalle456
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Click Register Button
    Click Button  Register

Go To Register Page And Validate
    Go To Register Page
    Register Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password And Password Confirmation
    [Arguments]  ${password}  ${confirmation}
    Input Password  password  ${password}
    Input Password  password_confirmation  ${confirmation}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
