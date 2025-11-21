from PyroUbot import *

__MODULE__ = "ɢᴀᴍᴇ"
__HELP__ = """
<b>🎮 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɢᴀᴍᴇ 🎮</b>

<blockquote><b>🎲 ʀᴀɴᴅᴏᴍ ɢᴀᴍᴇ:
• <code>{0}game</code> - ᴍᴜɴᴄᴜʟᴋᴀɴ ɢᴀᴍᴇ ʀᴀɴᴅᴏᴍ</b></blockquote>

<blockquote><b>🎯 ᴜsᴀʜᴀ ᴅᴀɴ ᴍᴇɴᴀɴɢ! 500+ ɢᴀᴍᴇ ᴛᴇʀsᴇᴅɪᴀ!</b></blockquote>
"""


@PY.UBOT("catur")
@PY.TOP_CMD
async def _(client, message):
    try:
        x = await client.get_inline_bot_results("GameFactoryBot")
        msg = message.reply_to_message or message
        await client.send_inline_bot_result(
            message.chat.id, x.query_id, x.results[0].id, reply_to_message_id=msg.id
        )
    except Exception as error:
        await message.reply(error)


@PY.UBOT("game")
@PY.TOP_CMD
async def game_cmd(client, message):
    try:
        x = await client.get_inline_bot_results("gamee")
        msg = message.reply_to_message or message
        random_index = random.randint(0, len(x.results) - 1)
        await client.send_inline_bot_result(
            message.chat.id, x.query_id, x.results[random_index].id, reply_to_message_id=msg.id
        )
    except Exception as error:
        await message.reply(error)
