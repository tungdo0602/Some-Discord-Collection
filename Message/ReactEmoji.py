import requests, os

token = ""
emoji_name = ""
emoji_id = ""
channel_id = ""
message_id = ""

postemoji = requests.put(f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}/reactions/{emoji_name}:{emoji_id}/@me', headers={"authorization": token})
if postemoji.status_code == 204:
	print("successfully react emoji!")
else:
	print(f"Failed to react that emoji! ERROR {postemoji.status_code}")
os.system('pause')