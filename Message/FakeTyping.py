import requests
import time

token = ""
channel_id = ""

while token == token:
	typing = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/typing', headers={"authorization": token})
	print(typing.status_code)
	time.sleep(1)