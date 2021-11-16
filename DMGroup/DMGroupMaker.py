import requests, os

token = ""

group = requests.post('https://discord.com/api/v9/users/@me/channels', headers={'authorization': token}, json={"recipients":["849523658426286081","775194675950649344"]})
if group.status_code == 200:
	print("done!")
else:
	print(f"Failed! ERROR {group.status_code}")