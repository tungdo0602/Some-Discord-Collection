import requests, time

token = ""
channel_id = ""
message_id = ""

while token == token:
	message = input("Edit Message to> ")
	em = requests.patch(f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}', headers={"authorization": token}, data={"content": message})
	