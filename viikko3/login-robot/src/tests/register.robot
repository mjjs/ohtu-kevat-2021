*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command
    Input Credentials  esko  kayttaja123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input New Command
    Input Credentials  kalle  kayttaja123
    Output Should Contain  Username taken

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  ka  kayttaja123
    Output Should Contain  Username must be at least three characters long

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  kalle  k
    Output Should Contain  Password must be at least eight characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  kalle  kayttajamme
    Output Should Contain  Password must include at least one number
