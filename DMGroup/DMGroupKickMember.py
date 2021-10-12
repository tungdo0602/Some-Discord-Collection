import requests
import os

token = ""
dmgroup_id = ""
user_id = ""

kick = requests.delete(f'https://discord.com/api/v9/channels/{dmgroup_id}/recipients/{user_id}', headers={"authorization": token})
if kick.status_code == 204:
	print("Successfully remove member from group!")
else:
	print("Failed to remove member from group!")