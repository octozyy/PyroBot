from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import OWNER_ID, bot, ubot, get_expired_date
from PyroUbot.core.database import get_list_from_vars


class MSG:     
    def EXP_MSG_UBOT(X):
        return f"""
<blockquote><b>❏ ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>
<b>├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ ɪᴅ:</b> <code>{X.me.id}</code>
<b>╰ ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴛᴇʟᴀʜ ʜᴀʙɪs</b></blockquote>
"""

    def START(message):
        return f"""
<u><b>🚀 Selamat Datang, </b></u><a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>! 

<blockquote><b>⚡ Sistem Info:</b>
• 🐍 Python: 3.10.12
• 🔥 Pyrogram: 3.0.2  
• 👥 Total Pengguna: {len(ubot._ubot)} users

<u><b>📋 Panduan Menu:</b></u>
<b>🆘 Help Menu: Lihat semua fitur bot</b>
<b>🤖 Buat Userbot: Buat akun bot pribadi</b>
<b>💳 Beli Userbot: Dapatkan akses premium</b>
<b>📞 Support: Hubungi owner jika ada masalah</b></blockquote>

<u><b>🎯 Pilih opsi di bawah ini:</b></u>"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<blockquote><b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b>

<b>⎆ ᴍᴏᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ:</b>
 <b>├ ᴅᴀɴᴀ​</b>
 <b>├────• </b>
 <b>├────• an **</b>
 <b>├ Qris </b>
 <b>├────• https://files.catbox.moe/jvyfvo.jpg</b>
 ᴜɴᴛᴜᴋ ᴍᴇᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ʟᴀɪɴɴʏᴀ ʙɪꜱᴀ ʟᴀɴɢꜱᴜɴɢ ʜᴜʙ ᴏᴡɴᴇʀ, ᴀᴅᴍɪɴ ᴅᴀɴ sᴇʟᴇʀ.

<b>⌭ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ʙᴜᴋᴛɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ</b></blockquote>
"""

    async def UBOT(count):
        ub = ubot._ubot[int(count)]
        expired = await get_expired_date(ub.me.id)
        exp = expired.strftime("%d-%m-%Y") if expired else "Tidak ada"
        return f"""
<blockquote><b>🤖 ᴜsᴇʀʙᴏᴛ ᴋᴇ {int(count) + 1}/{len(ubot._ubot)}</b>

👤 <b>ᴀᴋᴜɴ:</b> <a href=tg://user?id={ub.me.id}>{ub.me.first_name} {ub.me.last_name or ''}</a>
🆔 <b>ɪᴅ:</b> <code>{ub.me.id}</code>
🌐 <b>ᴅᴄ:</b> <code>{ub.me.dc_id}</code>
⏰ <b>ᴇxᴘɪʀᴇᴅ:</b> <code>{exp}</code></blockquote>
"""

    def POLICY():
        return """
<b>⚠️ Kebijakan Penggunaan Userbot:</b>

• Gunakan userbot dengan bijak dan sesuai aturan Telegram.
• Jangan gunakan untuk spam atau aktivitas ilegal.
• Pastikan akun Anda aman dan tidak dibagikan ke orang lain.
• Admin tidak bertanggung jawab atas penyalahgunaan.
"""
