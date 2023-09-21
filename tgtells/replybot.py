#! /usr/bin/env python
"""
Feeds replies from TG client to a file.
Run this as a script from your own MUD client.
Then send the contents of that file separately.

Configuration details are in the next block.
Of course, you will need a Telegram API key.
"""
import requests
import json

_api_token = "use_your_own_here"
_url = f"https://api.telegram.org/bot{_api_token}/getUpdates"
_reply_file = "reply.txt"
_options = {
    "timeout": 3,
    "offset": 0,
    "limit": 1
}

req = requests.post(_url, data=_options)
updatejson = json.loads(req.text)

try:
    reply = updatejson["result"][-1]
    last_update_id = reply["update_id"]
    player_name = reply["message"]["reply_to_message"]["text"].split(' ')[0] # just take first word
    reply_text = reply["message"]["text"]

    with open(_reply_file, 'w') as replyfile:
        replyfile.write(f"tell {player_name} {reply_text}")

    # forget previous replies to prevent fetching them by mistake
    _options["offset"] = last_update_id + 1
    print(f"### Updating offset to {last_update_id + 1}")
    req = requests.post(_url, data=_options)
except KeyError as k:
    if k.args[0] == "reply_to_message":
        print(f"Oops: Update {last_update_id} is not a reply!") 
        print(f"We'll move to update #{last_update_id + 1} next cycle.")
        _options["offset"] = last_update_id + 1
        req = requests.post(_url, data=_options)
    else:
        print(f"Another KeyError somehow occurred. Check {k.args[0]}.")
except IndexError:
    if updatejson["result"] != []:
        print(updatejson)

