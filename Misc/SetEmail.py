import requests
import time
import os
import random

#You will get something's going on

token = ""
email = ""
password = ""


setemail = requests.patch('https://discord.com/api/v9/users/@me', headers={'authorization': token}, json={"email": email,"password": password})
print(setemail.status_code)