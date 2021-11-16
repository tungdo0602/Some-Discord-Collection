import requests, os

token = ""
server_id = ""

delete = requests.post(f'https://discord.com/api/v9/guilds/{server_id}/delete', headers={'authorization': token})
if delete.status_code == 204:
	print("Successfully deleted server!")
else:
	print(f"Failed to delete server! ERROR {delete.status_code}")