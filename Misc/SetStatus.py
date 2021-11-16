import requests, os

token = ""
status = "" # "dnd" = do not disturb, "invisible" = offline/invisible status, "idle" = idle status

status = requests.patch('https://discord.com/api/v9/users/@me/settings', headers={'authorization': token}, json={"status": status})