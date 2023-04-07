from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
import openai
from pyrogram.types import CallbackQuery
from config import *
import os,sys,re,requests
import asyncio,time
from random import choice

from datetime import datetime
import logging

FORMAT = "[LEGEND-Rachit] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


StartTime = time.time()
Rachit = Client(
    "chat-gpt" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)
START = f"""
ʜᴜɪ! ɪ ᴀᴍ sʜᴏɴᴀ😘 ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴛᴇʟᴇɢʀᴀᴍ ᴄʜᴀᴛɢᴘᴛ ʙᴏᴛ

⚡ ᴏᴡɴᴇʀ - @Hyper_x_Rachit
⚡ ᴜᴘᴅᴀᴛᴇ - @Hyperxrachit
⚡ sᴜᴍᴘᴏʀᴛ - @off_road143

ᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ʙʏ ᴀᴅᴅɪɴɢ `Shona` ʙᴇғᴏʀᴇ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ.
"""
xa = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()
axx = bytearray.fromhex("49  54 7A 5F 4C 45 47 45 4E 44 5F 43 4F 44 45 52").decode()
xxc = bytearray.fromhex("4D 52 5F 53 55 4B 4B 55 4E").decode()
SOURCE = xa
UPDATE_CHNL = xxc
DEVELOPER = axx
SOURCE_TEXT = f"""
Not available.
"""


x=["❤️"]
g=choice(x)
MAIN = [
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ 😘",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
    InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇ 📲", url=f"t.me/hyperxrachit") , 
        InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ 🖱", url=f"t.me/off_road143") 
    ], 
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ 🙌", callback_data="HELP"),
        InlineKeyboardButton(text="sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ 💻", url=f"github.com/Hyper-x-Rachit/Shona_Ai")
    ],
]

PNG_BTN = [
    [
         InlineKeyboardButton(
             text="𝙰𝙳𝙳 𝙼𝙴",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
]
SOURCE_BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('SOURCE', url=f"{SOURCE}")]])
HELP_READ = "ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ... \n\n `Shona`: ᴀsᴋ ᴀɴʏᴛʜɪɴɢ ᴜ ᴡᴀɴᴛ. \n\n ᴇxᴀᴍᴘʟᴇ: `Shona Where is TajMahal?`"
HELP_BACK = [
    [
           InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="HELP_BACK"),
    ],
]

  
#         start
@Rachit.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
async def restart(client, m: Message):
        accha = await m.reply_text(
                        text = f"{g}")
        await asyncio.sleep(0.2)
        await accha.edit("Just a sec...")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(
                  sticker = STKR,
        )
        await asyncio.sleep(0.3)
        await umm.delete()
        await m.reply_photo(
            photo = START_IMG,
            caption=START,
            reply_markup=InlineKeyboardMarkup(MAIN),
        )
#  callback 
@Rachit.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
     await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BACK),
     )
    elif query.data == "HELP_BACK":
            await query.message.edit(text = START,
                  reply_markup=InlineKeyboardMarkup(MAIN),
        )
    
@Rachit.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    hmm = await message.reply_text(
                        text = HELP_READ,
                        reply_markup= InlineKeyboardMarkup(HELP_BACK),
       )
@Rachit.on_message(filters.command(['FAJIDFAJAHIGANIDFNAIFDJA', 'AFNDOAFIANIDBAOGAOHFO'], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def source(bot, m):
    
    await m.reply_photo(START_IMG, caption=SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)
#  alive
@Rachit.on_message(filters.command(["ping"], prefixes=["","+", "/", "-", "?", "$", "&","."]))
async def ping(client, message: Message):
        start = datetime.now()
        t = "**🔁|𝙱𝙰𝙱𝚄 𝙴𝙺 𝚂𝙴𝙲 𝚁𝚄𝙺𝙾 😘...**"
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("**✅|ummmm😍**")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(
                             photo=START_IMG,
                             caption=f"**Pong!**",
                             reply_markup=InlineKeyboardMarkup(PNG_BTN),
       )

#  main   
openai.api_key = OPENAI_KEY
@Rachit.on_message(filters.command(["Shona","shona","@Shona_Ai"],  prefixes=["","+", ".", "/", "-", "?", "$","#","&"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`Shona Who is elon musk?`")
        else:

            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2,
)

            x=resp['choices'][0]["message"]["content"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"{x}", parse_mode=ParseMode.MARKDOWN)     
    except Exception as e:
        await message.reply_text(f"**ERROR:    {e} ")


s = bytearray.fromhex("68 74 74 70 73 3A 2F 2F 67 69 74 68 75 62 2E 63 6F 6D 2F 4E 6F 6F 62 2D 6D 75 6B 65 73 68 2F 43 68 61 74 67 70 74 2D 62 6F 74").decode()
u = bytearray.fromhex("49  54 7A 5F 4C 45 47 45 4E 44 5F 43 4F 44 45 52").decode()
d= bytearray.fromhex("4D 52 5F 53 55 4B 4B 55 4E").decode()
if SOURCE != s:
    print("So sad, you have changed source, change it back to ` https://github.com/Hyper-x-Rachit/Chatgpt-bot `  else I won't work")
    sys.exit(1)  
if DEVELOPER!=u:
    print("So sad, you have changed Updates, change it back to `Hyper_x_Rachit ` else I won't work")
    sys.exit(1)
if UPDATE_CHNL!=d:
    print("So sad, you have change developer, change it back to `Shona_Ai ` else I won't work")
    sys.exit(1)


if __name__ == "__main__":
    print(f""" {BOT_NAME} ɪs ᴀʟɪᴠᴇ!
    """)
    try:
        Rachit.start()
        
        
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    print(f"""GIVE STAR TO THE REPO 
 {BOT_NAME} ɪs ᴀʟɪᴠᴇ!  
    """)
    idle()
    Rachit.stop()
    print("Bot stopped.")
