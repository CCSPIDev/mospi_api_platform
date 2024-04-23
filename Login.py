""" How to Use /
Call the script file and pass all the pcredentials in double qoutes and assign value by (:) and seprated values by comma (,).
for e.g. Login.py "username:USERNAME, password:XYZ" 
 """



def login_agrs():
    import sys
    try:
        username_str=""
        password_str=""
        txt=str(sys.argv).split(',')
        username_str=txt[1][1:]
        password_str=txt[2][:-2]
        # print(f'{email_str},{password_str}')
        if (username_str.split(':')[0][1:]).strip().lower()=="username":
            username=(username_str.split(':')[1]).strip()
        if (password_str.split(':')[0]).strip().lower()=="password":
            password=(password_str.split(':')[1]).strip()
        # print(f'{username},{password}')
        return username,password
    except:
        return None, None
        print(f'Please Enter your email password in the following format\n"username:xyz, password:*****"')

def gettoken(username,password):
    import requests
    import json
    import pandas as pd
    try:
        response = requests.post("http://10.24.89.9/api/users/login" , json = {
            "username": username,
            "password": password
        })
        token=response.json()["response"]["token"]  
        print(f'Login Sucessful\nToken: {token}')
        return token
    except:
        print("Please enter and check all credentials or check the server adress")
            # return response
username,password=login_agrs()
login_agrs()
token_api=gettoken(username,password)