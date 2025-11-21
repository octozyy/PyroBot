from PyroUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "ʙɪɴɢ ᴄʜᴀᴛ"
__HELP__ = """
<b>🤖 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙɪɴɢ ᴄʜᴀᴛ 🤖</b>

<blockquote><b>💬 ᴄʜᴀᴛ ᴀɪ ʙɪɴɢ:
• <code>{0}bing [pesan]</code> - ᴄᴀʀɪ ɪɴꜰᴏ ᴛᴇʀʙᴀʀᴜ, ʙᴀɴᴛᴜ ᴘʀᴏᴅᴜᴋᴛɪᴠɪᴛᴀs, ʀᴇᴋᴏᴍᴇɴᴅᴀsɪ ᴡɪsᴀᴛᴀ/ʙᴜᴋᴜ/ꜰɪʟᴍ</b></blockquote>

<blockquote><b>🌐 ᴄʜᴀᴛ ᴅᴇɴɢᴀɴ AI ʙɪɴɢ ᴜɴᴛᴜᴋ ɪɴꜰᴏʀᴍᴀsɪ ᴅᴀɴ ʙᴀɴᴛᴜᴀɴ!</b></blockquote>
"""


@PY.UBOT("bing")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>mohon gunakan format\ncontoh : .bard query"
            )
        else:
            prs = await message.reply_text(f"<emoji id=5469745532693923461>♾</emoji>Proccesing Kingz....")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.botcahx.eu.org/api/search/bing-chat?text={a}&apikey=Boyy')

            try:
                if "message" in response.json():
                    x = response.json()["message"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")
