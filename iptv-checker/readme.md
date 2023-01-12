# IPTV CHECKER BOT

## What does this bot do?
The Telegram bot checks the status of IPTV lists through the Xtream Codes API. Then it returns the following information:

|Field|Information|
|----|-----|
|User|IPTV List Username|
|Password|IPTV list password|
|Expiration Date| Date on which the IPTV list will stop working |
|Creation Date| Date the IPTV list was created |
|Active connections| Maximum number of people that can connect to that IPTV list at the same time|
|Current connections| Number of people who are watching that IPTV list at the moment|
|Number of Streams|Total number of broadcasts on the IPTV list|
|Server|Address and port to access the Xtream Codes panel|
|Customer Area|Web page of the panel from which you can view the channels without a player|

## How does the bot work?

You just have to send him the link of your IPTV list and he will take care of the rest. Only works with Xtream Codes lists


## Do you have any IPTV list?

No, this repository does not store, create, or distribute illegal content. The bot has been designed for educational purposes

## How can I collaborate?
There are two ways to collaborate:
- Adding new features to the bot through _pull-request_.


## Can I use the code to create another bot?
Yes, as long as you comply with the [MIT LICENSE]([(https://github.com/mak-iptv/)](https://github.com/mak-iptv/)](https://github.com/mak-iptv/iptv1)/iptv-checker/blob/main/LICENSE).

If you are going to use it on Heroku, we make it a little easier for you. You just have to click on the following button



## What environment variables do I need?
|Field|Information|
|----|-----|
|TOKEN | Telegram bot token|
|WEBHOOK| Server address |
|PORT|Server port|

## Can I not use a WebHook?
Yes, you can use the bot without WebHook by modifying the `bot.py` file.
