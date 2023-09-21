# TGTells

Forwards received tells to a Telegram bot you control. Reply to the individual
tells by replying to the messages in the bot chat, not by typing directly into
the chat.

## Prerequisites

- Python 3.x
  - requests (for hitting the webhook)
- a Telegram API token (fill it into replybot.py)
- tintin++ 2.02

## Setup

Here, I assume you already have a bot set up using the BotFather service which
Telegram provides. If not, [read the tutorial][bot] first. Then come back to:

- Copy replybot.py into your preferred script location.
- Update the API token into the `_api_token` variable.
- Create an empty text file for storing the reply from telegram.
- Update tgtells.tin with the path to your script and reply file.
- Import the #TICKER into your client, and reload it.

Feel free to ping me on any of the usual channels if you need help.

[bot]: https://core.telegram.org/bots/tutorial
