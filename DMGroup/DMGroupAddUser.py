import requests, os

token = ""
DMGroup_id = ""
userid = ""

add = requests.put(f'https://discord.com/api/v9/channels/{DMGroup_id}/recipients/{userid}', headers={'authorization': token})
if add.status_code == 204:
	print("Successfully added user to group!")
else:
	print("False to add user to group!")