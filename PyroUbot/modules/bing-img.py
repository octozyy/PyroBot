import random

from pyrogram.types import InputMediaPhoto
from PyroUbot import *

__MODULE__ = "ʙɪɴɢ ɪᴍɢ"
__HELP__ = """
<b>🖼️ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙɪɴɢ ɪᴍɢ 🖼️</b>

<blockquote><b>🔍 ᴄᴀʀɪ ɢᴀᴍʙᴀʀ:
• <code>{0}pic [query]</code> - ᴄᴀʀɪ ᴘʜᴏᴛᴏ ʀᴀɴᴅᴏᴍ ᴅᴀʀɪ ɢᴏᴏɢʟᴇ</b></blockquote>

<blockquote><b>📸 ᴛᴇᴍᴜᴋᴀɴ ɢᴀᴍʙᴀʀ ᴍᴇʟᴀʟᴜɪ ʙɪɴɢ!</b></blockquote>
"""


@PY.UBOT("pic")
async def pic_bing_cmd(client, message):
    TM = await message.reply("<b>ᴍᴇᴍᴘʀᴏsᴇs...</b>")
    if len(message.command) < 2:
        return await TM.edit(f"<code>{message.text}</code> [ǫᴜᴇʀʏ]")
    x = await client.get_inline_bot_results(
        message.command[0], message.text.split(None, 1)[1]
    )
    get_media = []
    for X in range(4):
        try:
            saved = await client.send_inline_bot_result(
                client.me.id, x.query_id, x.results[random.randrange(len(x.results))].id
            )
            saved = await client.get_messages(
                client.me.id, int(saved.updates[1].message.id)
            )
            get_media.append(InputMediaPhoto(saved.photo.file_id))
            await saved.delete()
        except:
            pass
    if len(get_media) == 0:
        return await TM.edit("<b>❌ ɪᴍᴀɢᴇ ᴘʜᴏᴛᴏ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")
    else:
        await client.send_media_group(
            message.chat.id,
            get_media,
            reply_to_message_id=message.id,
        )
        return await TM.delete()
