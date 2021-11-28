import requests, os

token = ""
DMGroup_id = ""
DMGroup_name = ""

group = requests.patch(f'https://discord.com/api/v9/channels/{DMGroup_id}', headers={"authorization": token}, json={"name": DMGroup_name})
if group.status_code == 200:
	print("Successfully changed the group name!")
else:
	print(f"Failed to change the group name! ERROR {group.status_code}")