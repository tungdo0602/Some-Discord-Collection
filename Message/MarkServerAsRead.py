import requests, os

token = ""
serverid = ""

mark = requests.post(f'https://discord.com/api/v9/guilds/{serverid}/ack', headers={'authorization': token})
if mark.status_code == 204:
	print("Done!")
else:
	print(f"Failed! ERROR {mark.status_code}")