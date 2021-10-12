# -*- coding:utf-8 -*-
import requests
import os

def clear():
	os.system('cls')

#Config
token = ""
channel_id = int(input("Channel Id: "))
clear()
while token == token:
	message = input("Message > ")
	messagepost = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers={"authorization": token}, data={"content": message})
	if messagepost.status_code == 200:
		print("Successfully sent the message!")
	else:
		print(f"Failed to send the message. ERROR {messagepost.status_code}")
