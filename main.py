from pyrogram import Client, filters


API_ID = ""
API_HASH = ""
BOT_TOKEN= ""

EU = Client(
    name="EUbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
  )


print("Bot has started")

EU.run()
