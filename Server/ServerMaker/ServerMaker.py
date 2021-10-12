import requests
import os
import time

null = None
true = True
false = False

token = "ODk3MzM1MzI2NTY4MjM1MDA5.YWUKsw.tegBv7ric8wYAgMwoxyTsbffWtE"
while token == token:
	maker = requests.post('https://discord.com/api/v9/guilds', headers={'authorization': token}, json={"name":"Test1", "icon": null, "channels":[{"id":"00", "parent_id": null, "name": "Information", "type": "4"}, {"id": "01", "parent_id": "00", "name": "welcome-and-rules", "type": "0"}, {"id": "02", "parent_id": "00", "name": "announcements", "type": "0"}, {"id": "03", "parent_id": "00", "name": "resources", "type": "0"}, {"id": "10", "parent_id": null, "name": "Text Channels", "type": "4"}, {"id": "11", "parent_id": "10", "name": "general", "type": "0"}, {"id": "12", "parent_id": "10", "name": "meeting-plans", "type": "0"}, {"id": "13", "parent_id": "10", "name": "off-topic", "type": "0"}, {"id": "20", "parent_id": null, "name": "Voice Channels", "type": "4"}, {"id": "21", "parent_id": "20", "name": "Lounge", "type": "2"}, {"id": "22", "parent_id": "20", "name": "Meeting Room 1", "type": "2"}, {"id": "22", "parent_id": "20", "name": "Meeting Room 2", "type": "2"}], "system_channel_id": "11", "roles": [{"id": "00", "name": "@everyone", "permissions": "1071698660929"}, {"id": "01", "name": "officers (example)", "mentionable": true, "hoist": true, "permissions": "1073175068247", "color": "3066993"}], "guild_template_code": "2TffvPucqHkN"})
	if maker.status_code == 201:
		print("Successfully make server")
	else:
		print(f"Failed ERROR {maker.status_code}")