import requests, time, os

token = ""
username = "" # username must not have #tag
tag = "" # user tag, like 1234 or 9999 (don't need #) if 0001 = 1 or 0900 = 900

frq = requests.post('https://discord.com/api/v9/users/@me/relationships', headers={"authorization": token}, json={"username": username,"discriminator": tag})
if frq.status_code == 204:
	print("Successfully sent friend request!")
else:
	print(f"Failed to sent! ERROR {frq.status_code}")

os.system('pause')