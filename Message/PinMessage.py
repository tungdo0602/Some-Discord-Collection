import requests
import os

token = ""
channel_id = ""
message_id = ""

pins = requests.put(f'https://discord.com/api/v9/channels/{channel_id}/pins/{message_id}', headers={'authorization': token})
if pins.status_code == 204:
	print("Successfully pin the message!")
else:
	print(f"Failed to pin the message! ERROR {pins.status_code}")
	