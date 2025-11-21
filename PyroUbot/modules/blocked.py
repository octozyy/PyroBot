from PyroUbot import *
from pyrogram.raw.functions.contacts import GetBlocked

__MODULE__ = "ʙʟᴏᴄᴋᴇᴅ"
__HELP__ = """
<b>🚫 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙʟᴏᴄᴋᴇᴅ 🚫</b>

<blockquote><b>🔓 ᴍᴀɴᴀᴊᴇᴍᴇɴ ʙʟᴏᴄᴋɪʀᴀɴ:
• <code>{0}unblockall</code> - ᴜɴʙʟᴏᴄᴋ sᴇᴍᴜᴀ ᴜsᴇʀ ᴅɪ ᴄᴏɴᴛᴀᴄᴛ
• <code>{0}getblock</code> - ʟɪʜᴀᴛ ᴊᴜᴍʟᴀʜ ʏᴀɴɢ ᴅɪʙʟᴏᴄᴋɪʀ</b></blockquote>

<blockquote><b>📞 ᴋᴇʟᴏʟᴀ ʙʟᴏᴄᴋɪʀᴀɴ ᴄᴏɴᴛᴀᴄᴛ ᴅᴇɴɢᴀɴ ᴍᴜᴅᴀʜ!</b></blockquote>
"""

@PY.UBOT("unblockall")
async def _(user, message):
    sks = await EMO.BERHASIL(user)
    prs = await EMO.PROSES(user)
    _prs = await message.reply(f"{prs}sedang melakukan unblockall...")
    mecha = await user.invoke(GetBlocked(offset=0, limit=100))
    user_ids = [entry.peer_id.user_id for entry in mecha.blocked]
    for x in user_ids:
        try:
            await user.unblock_user(x)
        except:
            pass
    await _prs.edit(f"{sks}berhasil melakukan unblockall users")

@PY.UBOT("getblock")
async def _(user, message):
    prs = await EMO.PROSES(user)
    _prs = await message.reply(f"{prs}sedang mengecek...")
    mecha = await user.invoke(GetBlocked(offset=0, limit=100))
    user_ids = [entry.peer_id.user_id for entry in mecha.blocked]
    teko = len(user_ids)
    if user_ids:
        try:
            await _prs.edit(f"kamu memblockir : {teko} users")
        except Exception as i:
            await _prs.edit(f"{i}")
    else:
        await _prs.edit(f"tidak ada yang di blockir")
