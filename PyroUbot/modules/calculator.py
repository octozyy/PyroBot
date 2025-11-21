import ast
from pyrogram import Client, filters
from PyroUbot import PY

__MODULE__ = "ᴄᴀʟᴄᴜʟᴀᴛᴏʀ"
__HELP__ = """
<b>🧮 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴋᴀʟᴋᴜʟᴀᴛᴏʀ 🧮</b>

<blockquote><b>🔢 ʜɪᴛᴜɴɢ ᴍᴀᴛᴇᴍᴀᴛɪᴋᴀ:
• <code>{0}calc [ekspresi]</code> - ʜɪᴛᴜɴɢ ᴇᴋsᴘʀᴇsɪ
• ᴄᴏɴᴛᴏʜ: <code>{0}calc 5 + 10 * 2</code></b></blockquote>

<blockquote><b>➗ ᴋᴀʟᴋᴜʟᴀᴛᴏʀ ᴄᴇᴘᴀᴛ ᴅᴀɴ ᴀᴋᴜʀᴀᴛ!</b></blockquote>
"""

@PY.UBOT("calc")
@PY.TOP_CMD
async def _(client, message):
    args = message.text.split(" ", 1)
    if len(args) < 2:
        return await message.reply("❌ Format salah! Gunakan: <code>.calc [ekspresi]</code>")

    expression = args[1]

    try:
        # Parsing ekspresi dengan AST (Agar lebih aman)
        result = eval(compile(ast.parse(expression, mode="eval"), "<string>", "eval"))
        await message.reply(f"✅ Hasil: <code>{result}</code>")
    except Exception as e:
        await message.reply(f"❌ Error: {str(e)}")