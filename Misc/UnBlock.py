import requests, os

token = ""
userid = ""

block = requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{userid}', headers={'authorization': token})
if block.status_code == 204:
	print("Successfully unblocked user!")
else:
	print(f"Failed! ERROR {block.status_code}")