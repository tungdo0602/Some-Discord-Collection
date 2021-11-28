import requests, os

token = ""
userid = ""

block = requests.put(f'https://discord.com/api/v9/users/@me/relationships/{userid}', headers={'authorization': token}, json={"type":2})
if block.status_code == 204:
	print("Successfully blocked user!")
else:
	print(f"Failed! ERROR {block.status_code}")