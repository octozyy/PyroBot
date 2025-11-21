import asyncio
import importlib
from datetime import datetime

from pyrogram.enums import SentCodeType
from pyrogram.errors import *
from pyrogram.types import *
from pyrogram.raw import functions

from PyroUbot import *

otp_inputs = {}


@PY.BOT("start")
@PY.START
@PY.PRIVATE
async def _(client, message):
    buttons = BTN.START(message)
    msg = MSG.START(message)
    await message.reply_photo("https://files.catbox.moe/lwdv1r.jpg", caption=msg, reply_markup=InlineKeyboardMarkup(buttons))


@PY.CALLBACK("bahan")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if len(ubot._ubot) + 1 > MAX_BOT:
        buttons = [
            [InlineKeyboardButton("🏠 Home", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
<blockquote><b>❌ Tidak bisa membuat userbot lagi!\n\n❌ Maksimal userbot adalah {MAX_BOT}</b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    premium_users, ultra_premium_users = await get_list_from_vars(client.me.id, "PREM_USERS"), await get_list_from_vars(client.me.id, "ULTRA_PREM")
    if user_id not in premium_users and user_id not in ultra_premium_users and user_id != OWNER_ID:
        buttons = [
            [InlineKeyboardButton("Lanjutkan", callback_data="bayar_dulu")],
            [InlineKeyboardButton("Home", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            MSG.POLICY(),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = [[InlineKeyboardButton("🚀 Buat Userbot", callback_data="add_ubot")]]
        return await callback_query.edit_message_text(
            "",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    premium_users, ultra_premium_users = await get_list_from_vars(client.me.id, "PREM_USERS"), await get_list_from_vars(client.me.id, "ULTRA_PREM")
    if user_id not in premium_users and user_id not in ultra_premium_users and user_id != OWNER_ID:
        buttons = [
            [InlineKeyboardButton("🔄 Restart Userbot", callback_data=f"ress_ubot")],
            [InlineKeyboardButton("🏠 Home", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            MSG.POLICY(),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = [[InlineKeyboardButton("▶️ Lanjutkan", callback_data="buat_ubot")]]
        return await callback_query.edit_message_text(
            f"""
<blockquote><b>✅ Anda sudah membuat userbot\n\n🔄 Jika userbot Anda tidak bisa digunakan silahkan tekan tombol restart\n💎 Untuk beli premium tambahan, klik Beli Premium</b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )


@PY.CALLBACK("status")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in ubot._get_my_id:
        buttons = [
            [InlineKeyboardButton("🏠 Home", callback_data=f"home {user_id}")],
        ]
        exp = await get_expired_date(user_id)
        prefix = await get_pref(user_id)
        waktu = exp.strftime("%d-%m-%Y") if exp else "None"
        return await callback_query.edit_message_text(
            f"""
<blockquote>⌬ ᴜꜱᴇʀʙᴏᴛ ᴘʀᴇᴍɪᴜᴍ
  ᚗ ꜱᴛᴀᴛᴜꜱ : ᴘʀᴇᴍɪᴜᴍ
  ᚗ ᴘʀᴇꜰɪxᴇꜱ : {prefix[0]}
  ᚗ ᴇxᴘɪʀᴇᴅ_ᴏɴ : {waktu}</b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = [
            [InlineKeyboardButton("💎 Beli Userbot", callback_data=f"bahan")],
            [InlineKeyboardButton("🏠 Home", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
<blockquote><b>☫ ᴍᴀᴀꜰ ᴀɴᴅᴀ ʙᴇʟᴜᴍ ᴍᴇᴍʙᴇʟɪ ᴜꜱᴇʀʙᴏᴛ, ꜱɪʟᴀᴋᴀɴ ᴍᴇᴍʙᴇʟɪ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ.</b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
    )


@PY.CALLBACK("buat_ubot")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in ubot._get_my_id:
        buttons = [
            [InlineKeyboardButton("🔄 Restart Userbot", callback_data=f"ress_ubot")],
            [InlineKeyboardButton("💎 Beli Premium", callback_data="bayar_dulu")],
            [InlineKeyboardButton("🏠 Home", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
<blockquote><b>✅ Anda sudah membuat userbot\n\n🔄 Jika userbot Anda tidak bisa digunakan silahkan tekan tombol restart di atas</b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif len(ubot._ubot) + 1 > MAX_BOT:
        buttons = [
            [InlineKeyboardButton("🏠 Home", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
<blockquote><b><b>⌬ ᴛɪᴅᴀᴋ ʙɪsᴀ ᴍᴇᴍʙᴜᴀᴛ ᴜsᴇʀʙᴏᴛ!</b>

<b>⌬ ᴋᴀʀᴇɴᴀ ᴍᴀᴋsɪᴍᴀʟ ᴜsᴇʀʙᴏᴛ ᴀᴅᴀʟᴀʜ {Fonts.smallcap(str(len(ubot._ubot)))} ᴛᴇʟᴀʜ ᴛᴇʀᴄᴀᴘᴀɪ</b>

<blockquote><b>⌬ sɪʟᴀʜᴋᴀɴ ʜᴜʙᴜɴɢɪ: ᴀᴅᴍɪɴ ᴊɪᴋᴀ ᴍᴀᴜ ᴅɪʙᴜᴀᴛᴋᴀɴ ʙᴏᴛ sᴇᴘᴇʀᴛɪ sᴀʏᴀ </b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    premium_users, ultra_premium_users = await get_list_from_vars(client.me.id, "PREM_USERS"), await get_list_from_vars(client.me.id, "ULTRA_PREM")
    if user_id not in premium_users and user_id not in ultra_premium_users:
        buttons = [
            [InlineKeyboardButton("Lanjutkan", callback_data="bayar_dulu")],
            [InlineKeyboardButton("Home", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            MSG.POLICY(),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = [[InlineKeyboardButton("🚀 Buat Userbot", callback_data="add_ubot")]]
        return await callback_query.edit_message_text(
            """
<blockquote><b>📱 Untuk membuat userbot siapkan bahan berikut:

    📱 <code>phone_number</code>: nomor hp akun telegram

📱 Jika sudah tersedia silahkan klik tombol di bawah</b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )

@PY.CALLBACK("bayar_dulu")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    buttons = [
        [InlineKeyboardButton("1 Bulan (5k)", callback_data="pilih_bulan_1")],
        [InlineKeyboardButton("2 Bulan (10k)", callback_data="pilih_bulan_2")],
        [InlineKeyboardButton("3 Bulan (15k)", callback_data="pilih_bulan_3")],
        [InlineKeyboardButton("🏠 Home", callback_data=f"home {user_id}")],
    ]
    return await callback_query.edit_message_text(
        "<b>⏰ ᴘɪʟɪʜ ᴅᴜʀᴀsɪ ᴘʀᴇᴍɪᴜᴍ:</b>\n\n💰 <b>Harga per bulan: 5k</b>\n\nPilih durasi yang diinginkan:",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@PY.CALLBACK("pilih_bulan_1")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    buttons = [
        [InlineKeyboardButton("📝 Manual", callback_data="bayar_manual_1")],
        [InlineKeyboardButton("🤖 Otomatis", callback_data="bayar_otomatis_1")],
        [InlineKeyboardButton("🔙 Kembali", callback_data="bayar_dulu")],
    ]
    return await callback_query.edit_message_text(
        "<b>💳 ᴘɪʟɪʜ ᴍᴇᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴜɴᴛᴜᴋ 1 ʙᴜʟᴀɴ (5k):</b>\n\n📝 <b>Manual:</b> Bayar ke rekening, konfirmasi manual\n🤖 <b>Otomatis:</b> QRIS otomatis via API",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@PY.CALLBACK("pilih_bulan_2")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    buttons = [
        [InlineKeyboardButton("📝 Manual", callback_data="bayar_manual_2")],
        [InlineKeyboardButton("🤖 Otomatis", callback_data="bayar_otomatis_2")],
        [InlineKeyboardButton("🔙 Kembali", callback_data="bayar_dulu")],
    ]
    return await callback_query.edit_message_text(
        "<b>💳 ᴘɪʟɪʜ ᴍᴇᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴜɴᴛᴜᴋ 2 ʙᴜʟᴀɴ (10k):</b>\n\n📝 <b>Manual:</b> Bayar ke rekening, konfirmasi manual\n🤖 <b>Otomatis:</b> QRIS otomatis via API",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@PY.CALLBACK("pilih_bulan_3")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    buttons = [
        [InlineKeyboardButton("📝 Manual", callback_data="bayar_manual_3")],
        [InlineKeyboardButton("🤖 Otomatis", callback_data="bayar_otomatis_3")],
        [InlineKeyboardButton("🔙 Kembali", callback_data="bayar_dulu")],
    ]
    return await callback_query.edit_message_text(
        "<b>💳 ᴘɪʟɪʜ ᴍᴇᴛᴏᴅᴇ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴜɴᴛᴜᴋ 3 ʙᴜʟᴀɴ (15k):</b>\n\n📝 <b>Manual:</b> Bayar ke rekening, konfirmasi manual\n🤖 <b>Otomatis:</b> QRIS otomatis via API",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@PY.CALLBACK("bayar_manual_1")
@PY.CALLBACK("bayar_manual_2")
@PY.CALLBACK("bayar_manual_3")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    bulan = int(callback_query.data.split('_')[-1])
    jumlah = 5000 * bulan
    buttons = [
        [InlineKeyboardButton("✅ Konfirmasi", callback_data="confirm")],
        [InlineKeyboardButton("❌ Batal", callback_data=f"home {user_id}")],
    ]
    return await callback_query.edit_message_text(
        f"<b>💳 ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴍᴀɴᴜᴀʟ</b>\n\n📝 <b>Transfer ke:</b>\n🏦 <b>Dana:</b> 6287768378361\n💰 <b>Jumlah:</b> {toRupiah(jumlah)}\n\n📸 <b>Silahkan Kirim Bukti Pembayaran Anda.</b>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


@PY.CALLBACK("bayar_otomatis_1")
@PY.CALLBACK("bayar_otomatis_2")
@PY.CALLBACK("bayar_otomatis_3")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    bulan = int(callback_query.data.split('_')[-1])
    harga = 5000 * bulan
    import requests
    import qrcode
    import os
    import secrets

    userSaldo = 0  # Assume no saldo
    kurang = harga - userSaldo
    total = kurang + FEE_TRANSAKSI
    reff = f"DO-{secrets.token_hex(4).upper()}"

    data = {
        'api_key': API_ATLANTIC,
        'reff_id': reff,
        'nominal': total,
        'type': 'ewallet',
        'metode': 'qris'
    }

    try:
        response = requests.post('https://atlantich2h.com/deposit/create', data=data)
        res = response.json()
        if not res.get('status'):
            return await callback_query.edit_message_text(f"❌ Gagal: {res.get('message', 'Error')}")

        info = res['data']
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(info['qr_string'])
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img_path = f'/tmp/qr_{user_id}.png'
        img.save(img_path)

        teks = f"""
🏦 Beli Userbot 🏦
━━━━━━━━━━━━━━━━━━━━━━
❗ Saldo Anda kurang Rp{toRupiah(kurang)}. Deposit dulu.
🔑 Kode: `{reff}`
🎯 Ref: `{info['id']}`
💰 Kurang: Rp {toRupiah(kurang)}
🧾 Admin: Rp {toRupiah(FEE_TRANSAKSI)}
💳 Total: Rp {toRupiah(total)}
⏰ Aktif: 5 Menit

🌟 Bayar:
1. Buka e-wallet/m-banking
2. Pilih QRIS/Scan QR
3. Scan QR
4. Konfirmasi

© 2025 Ibra Decode
        """.strip()

        buttons = [[InlineKeyboardButton("❌ Batal", callback_data="batal_qris")]]
        await client.send_photo(user_id, img_path, caption=teks, reply_markup=InlineKeyboardMarkup(buttons))
        os.remove(img_path)

    except Exception as e:
        await callback_query.edit_message_text(f"❌ Error: {str(e)}")


@PY.CALLBACK("batal_qris")
async def _(client, callback_query):
    await callback_query.message.delete()
    await callback_query.answer("Dibatalkan!")


def toRupiah(number):
    return f"{number:,}".replace(",", ".")


@PY.CALLBACK("add_ubot")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    await callback_query.message.delete()
    try:
        phone = await bot.ask(
            user_id,
            (
                "<b>📱 Silahkan masukkan nomor telepon Telegram Anda dengan format kode negara.\nContoh: +628xxxxxxx</b>\n"
                "\n<b>❌ Gunakan /cancel untuk membatalkan proses membuat userbot</b>"
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "<blockquote>⏰ Pembatalan otomatis!\n🔄 Gunakan /start untuk memulai ulang</blockquote>")
    if await is_cancel(callback_query, phone.text):
        return
    phone_number = phone.text
    new_client = Ubot(
        name=str(callback_query.id),
        api_id=API_ID,
        api_hash=API_HASH,
        in_memory=False,
    )
    get_otp = await bot.send_message(user_id, "<blockquote><b>🔐 Mengirim kode OTP...</b></blockquote>")
    await new_client.connect()
    try:
        code = await new_client.send_code(phone_number.strip())
    except ApiIdInvalid as AID:
        await get_otp.delete()
        return await bot.send_message(user_id, AID)
    except PhoneNumberInvalid as PNI:
        await get_otp.delete()
        return await bot.send_message(user_id, PNI)
    except PhoneNumberFlood as PNF:
        await get_otp.delete()
        return await bot.send_message(user_id, PNF)
    except PhoneNumberBanned as PNB:
        await get_otp.delete()
        return await bot.send_message(user_id, PNB)
    except PhoneNumberUnoccupied as PNU:
        await get_otp.delete()
        return await bot.send_message(user_id, PNU)
    except Exception as error:
        await get_otp.delete()
        return await bot.send_message(user_id, f"ERROR: {error}")
    sent_code = {
        SentCodeType.APP: "<a href=tg://openmessage?user_id=777000>ᴀᴋᴜɴ ᴛᴇʟᴇɢʀᴀᴍ</a> ʀᴇsᴍɪ",
        SentCodeType.SMS: "sᴍs ᴀɴᴅᴀ",
        SentCodeType.CALL: "ᴘᴀɴɢɢɪʟᴀɴ ᴛᴇʟᴘᴏɴ",
        SentCodeType.FLASH_CALL: "ᴘᴀɴɢɢɪʟᴀɴ ᴋɪʟᴀᴛ ᴛᴇʟᴇᴘᴏɴ",
        SentCodeType.FRAGMENT_SMS: "ꜰʀᴀɢᴍᴇɴᴛ sᴍs",
        SentCodeType.EMAIL_CODE: "ᴇᴍᴀɪʟ ᴀɴᴅᴀ",
    }
    await get_otp.delete()
    otp_inputs[user_id] = ""
    buttons = [
        [InlineKeyboardButton("1", callback_data="otp_digit_1"), InlineKeyboardButton("2", callback_data="otp_digit_2"), InlineKeyboardButton("3", callback_data="otp_digit_3")],
        [InlineKeyboardButton("4", callback_data="otp_digit_4"), InlineKeyboardButton("5", callback_data="otp_digit_5"), InlineKeyboardButton("6", callback_data="otp_digit_6")],
        [InlineKeyboardButton("7", callback_data="otp_digit_7"), InlineKeyboardButton("8", callback_data="otp_digit_8"), InlineKeyboardButton("9", callback_data="otp_digit_9")],
        [InlineKeyboardButton("⌫", callback_data="otp_delete"), InlineKeyboardButton("0", callback_data="otp_digit_0"), InlineKeyboardButton("✅", callback_data="otp_enter")],
        [InlineKeyboardButton("❌", callback_data="otp_cancel")]
    ]
    otp_msg = await bot.send_message(
        user_id,
        "<b>🔑 Masukkan OTP:</b>\n\nKode: <code>(kosong)</code>",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    # Store the message id for editing
    otp_inputs[user_id] = {"code": "", "msg_id": otp_msg.id, "phone_number": phone_number, "code_obj": code, "new_client": new_client}
    return  # Exit here, callbacks will handle the rest

async def is_cancel(callback_query, text):
    if text.startswith("/cancel"):
        await bot.send_message(
            callback_query.from_user.id, "<blockquote>❌ Pembatalan otomatis!\n🔄 Gunakan /start untuk memulai ulang</blockquote>"
        )
        return True
    return False


@PY.BOT("control")
async def _(client, message):
    buttons = [
            [InlineKeyboardButton("🔄 Restart", callback_data=f"ress_ubot")],
        ]
    await message.reply(
            f"""
<blockquote><b>⎆ ᴀɴᴅᴀ ᴀᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ʀᴇꜱᴛᴀʀᴛ?!\n⎆ ᴊɪᴋᴀ ɪʏᴀ ᴘᴇɴᴄᴇᴛ ᴛᴏᴍʙᴏʟ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ</b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )

@PY.CALLBACK("ress_ubot")
async def _(client, callback_query):
    if callback_query.from_user.id not in ubot._get_my_id:
        return await callback_query.answer(
            f"you don't have acces",
            True,
        )
    for X in ubot._ubot:
        if callback_query.from_user.id == X.me.id:
            for _ubot_ in await get_userbots():
                if X.me.id == int(_ubot_["name"]):
                    try:
                        ubot._ubot.remove(X)
                        ubot._get_my_id.remove(X.me.id)
                        UB = Ubot(**_ubot_)
                        await UB.start()
                        for mod in loadModule():
                            importlib.reload(
                                importlib.import_module(f"PyroUbot.modules.{mod}")
                            )
                        return await callback_query.edit_message_text(
                            f"⎆ ʀᴇꜱᴛᴀʀᴛ ʙᴇʀʜᴀꜱɪʟ ᴅɪʟᴀᴋᴜᴋᴀɴ !\n\n ⎆ ɴᴀᴍᴇ: {UB.me.first_name} {UB.me.last_name or ''} | {UB.me.id}"
                        )
                    except Exception as error:
                        return await callback_query.edit_message_text(f"{error}")

@PY.BOT("restart")
async def _(client, message):
    msg = await message.reply("<b>⎆ ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ</b>")
    if message.from_user.id not in ubot._get_my_id:
        return await msg.edit(
            f"you don't have acces",
            True,
        )
    for X in ubot._ubot:
        if message.from_user.id == X.me.id:
            for _ubot_ in await get_userbots():
                if X.me.id == int(_ubot_["name"]):
                    try:
                        ubot._ubot.remove(X)
                        ubot._get_my_id.remove(X.me.id)
                        UB = Ubot(**_ubot_)
                        await UB.start()
                        for mod in loadModule():
                            importlib.reload(
                                importlib.import_module(f"PyroUbot.modules.{mod}")
                            )
                        return await msg.edit(
                            f"⎆ ʀᴇꜱᴛᴀʀᴛ ʙᴇʀʜᴀꜱɪʟ ᴅɪʟᴀᴋᴜᴋᴀɴ !\n\n ⎆ ɴᴀᴍᴇ: {UB.me.first_name} {UB.me.last_name or ''} | `{UB.me.id}`"
                        )
                    except Exception as error:
                        return await msg.edit(f"{error}")

@PY.CALLBACK("cek_ubot")
async def _(client, callback_query):
    await callback_query.answer()
    if not ubot._ubot:
        await callback_query.edit_message_text("Tidak ada userbot yang aktif.")
        return
    try:
        await bot.send_message(
            callback_query.from_user.id,
            await MSG.UBOT(0),
            reply_markup=InlineKeyboardMarkup(BTN.UBOT(ubot._ubot[0].me.id, 0)),
        )
    except Exception as e:
        await callback_query.edit_message_text(f"Error: {e}\nStart bot di PM dulu!")

@PY.CALLBACK("cek_masa_aktif")
async def _(client, callback_query):
    user_id = int(callback_query.data.split()[1])
    expired = await get_expired_date(user_id)
    try:
        xxxx = (expired - datetime.now()).days
        return await callback_query.answer(f"⎆ ᴛɪɴɢɢᴀʟ {xxxx} ʜᴀʀɪ ʟᴀɢɪ", True)
    except:
        return await callback_query.answer("⎆ sᴜᴅᴀʜ ᴛɪᴅᴀᴋ ᴀᴋᴛɪғ", True)

@PY.CALLBACK("del_ubot")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id not in await get_list_from_vars(client.me.id, "ADMIN_USERS"):
        return await callback_query.answer(
            f"❌ ᴛᴏᴍʙᴏʟ ɪɴɪ ʙᴜᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴜ {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    try:
        show = await bot.get_users(callback_query.data.split()[1])
        get_id = show.id
        get_mention = f"{get_id}"
    except Exception:
        get_id = int(callback_query.data.split()[1])
        get_mention = f"{get_id}"
    for X in ubot._ubot:
        if get_id == X.me.id:
            await X.unblock_user(bot.me.username)
            await remove_ubot(X.me.id)
            ubot._get_my_id.remove(X.me.id)
            ubot._ubot.remove(X)
            await X.log_out()
            await callback_query.answer(
                f"⎆ {get_mention} ʙᴇʀʜᴀsɪʟ ᴅɪʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀsᴇ", True
            )
            await callback_query.edit_message_text(
                await MSG.UBOT(0),
                reply_markup=InlineKeyboardMarkup(
                    BTN.UBOT(ubot._ubot[0].me.id, 0)
                ),
            )
            await bot.send_message(
                X.me.id,
                MSG.EXP_MSG_UBOT(X),
                reply_markup=InlineKeyboardMarkup(BTN.EXP_UBOT()),
            )

    
@PY.CALLBACK("otp_digit_([0-9])")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    digit = callback_query.data.split("_")[-1]
    if user_id not in otp_inputs:
        return await callback_query.answer("Sesi OTP tidak ditemukan!", show_alert=True)
    otp_inputs[user_id]["code"] += digit
    current_code = otp_inputs[user_id]["code"]
    masked = current_code
    buttons = [
        [InlineKeyboardButton("1", callback_data="otp_digit_1"), InlineKeyboardButton("2", callback_data="otp_digit_2"), InlineKeyboardButton("3", callback_data="otp_digit_3")],
        [InlineKeyboardButton("4", callback_data="otp_digit_4"), InlineKeyboardButton("5", callback_data="otp_digit_5"), InlineKeyboardButton("6", callback_data="otp_digit_6")],
        [InlineKeyboardButton("7", callback_data="otp_digit_7"), InlineKeyboardButton("8", callback_data="otp_digit_8"), InlineKeyboardButton("9", callback_data="otp_digit_9")],
        [InlineKeyboardButton("⌫", callback_data="otp_delete"), InlineKeyboardButton("0", callback_data="otp_digit_0"), InlineKeyboardButton("✅", callback_data="otp_enter")],
        [InlineKeyboardButton("❌", callback_data="otp_cancel")]
    ]
    await callback_query.edit_message_text(
        f"<b>🔑 Masukkan OTP:</b>\n\nKode: <code>{masked}</code>",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@PY.CALLBACK("otp_delete")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id not in otp_inputs:
        return await callback_query.answer("Sesi OTP tidak ditemukan!", show_alert=True)
    otp_inputs[user_id]["code"] = otp_inputs[user_id]["code"][:-1]
    current_code = otp_inputs[user_id]["code"]
    masked = "*" * len(current_code) if current_code else "(kosong)"
    buttons = [
        [InlineKeyboardButton("1", callback_data="otp_digit_1"), InlineKeyboardButton("2", callback_data="otp_digit_2"), InlineKeyboardButton("3", callback_data="otp_digit_3")],
        [InlineKeyboardButton("4", callback_data="otp_digit_4"), InlineKeyboardButton("5", callback_data="otp_digit_5"), InlineKeyboardButton("6", callback_data="otp_digit_6")],
        [InlineKeyboardButton("7", callback_data="otp_digit_7"), InlineKeyboardButton("8", callback_data="otp_digit_8"), InlineKeyboardButton("9", callback_data="otp_digit_9")],
        [InlineKeyboardButton("⌫", callback_data="otp_delete"), InlineKeyboardButton("0", callback_data="otp_digit_0"), InlineKeyboardButton("✅", callback_data="otp_enter")],
        [InlineKeyboardButton("❌", callback_data="otp_cancel")]
    ]
    await callback_query.edit_message_text(
        f"<b>🔑 Masukkan OTP:</b>\n\nKode: <code>{masked}</code>",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@PY.CALLBACK("otp_enter")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id not in otp_inputs:
        return await callback_query.answer("Sesi OTP tidak ditemukan!", show_alert=True)
    otp_code = otp_inputs[user_id]["code"]
    if not otp_code:
        return await callback_query.answer("Kode OTP kosong! Masukkan kode terlebih dahulu.", show_alert=True)
    phone_number = otp_inputs[user_id]["phone_number"]
    code = otp_inputs[user_id]["code_obj"]
    new_client = otp_inputs[user_id]["new_client"]
    del otp_inputs[user_id]
    await callback_query.message.delete()
    # Proceed with sign in
    try:
        await new_client.sign_in(
            phone_number.strip(),
            code.phone_code_hash,
            phone_code=" ".join(str(otp_code)),
        )
    except PhoneCodeInvalid as PCI:
        return await bot.send_message(user_id, PCI)
    except PhoneCodeExpired as PCE:
        return await bot.send_message(user_id, PCE)
    except BadRequest as error:
        return await bot.send_message(user_id, f"ERROR: {error}")
    except SessionPasswordNeeded:
        try:
            two_step_code = await bot.ask(
                user_id,
                "🔐 Akun Anda telah mengaktifkan verifikasi dua langkah. Silahkan kirimkan passwordnya.\n\n❌ Gunakan /cancel untuk membatalkan proses membuat userbot</b>",
                timeout=300,
            )
        except asyncio.TimeoutError:
            return await bot.send_message(user_id, "<blockquote>⏰ Pembatalan otomatis!\n🔄 Gunakan /start untuk memulai ulang</blockquote>")
        if await is_cancel(callback_query, two_step_code.text):
            return
        new_code = two_step_code.text
        try:
            await new_client.check_password(new_code)
        except Exception as error:
            return await bot.send_message(user_id, f"ERROR: {error}")
    session_string = await new_client.export_session_string()
    await new_client.disconnect()
    new_client.storage.session_string = session_string
    new_client.in_memory = False
    bot_msg = await bot.send_message(
        user_id,
        "⏳ Sedang memproses....\n\n⏳ Silahkan tunggu sebentar",
        disable_web_page_preview=True,
    )
    await new_client.start()
    if not user_id == new_client.me.id:
        ubot._ubot.remove(new_client)
        return await bot_msg.edit(
            "<b>❌ Harap gunakan nomor Telegram Anda di akun Anda saat ini dan bukan nomor Telegram dari akun lain</b>"
        )
    await add_ubot(
        user_id=int(new_client.me.id),
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=session_string,
    )
    for mod in loadModule():
        importlib.reload(importlib.import_module(f"PyroUbot.modules.{mod}"))
    SH = await ubot.get_prefix(new_client.me.id)
    buttons = [
        [InlineKeyboardButton("🏠 Home", callback_data=f"home {user_id}")],
    ]
    text_done = f"""
<blockquote><b>✅ Berhasil diaktifkan
👤 Name : <a href=tg://user?id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a>
🆔 ID : {new_client.me.id}
⚙️ Prefixes : {' '.join(SH)}
📞 Harap hubungi admin untuk info terbaru
🔄 Jika bot tidak respon, ketik /restart</b></blockquote>
    """
    await bot_msg.edit(text_done, disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons))
    await bash("rm -rf *session*")
    await install_my_peer(new_client)
    try:
        await new_client.join_chat("ibradecodee")
        await new_client.join_chat("syahv2doffctestimoni")
    except UserAlreadyParticipant:
        pass
    return await bot.send_message(
        LOGS_MAKER_UBOT,
        f"""
<b>⌬ ᴜsᴇʀʙᴏᴛ ᴅɪᴀᴋᴛɪғᴋᴀɴ</b>
<b> ├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a> 
<b> ╰ ɪᴅ:</b> <code>{new_client.me.id}</code>
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⦪ ᴄᴇᴋ ᴍᴀsᴀ ᴀᴋᴛɪғ ⦫",
                        callback_data=f"cek_masa_aktif {new_client.me.id}",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

@PY.CALLBACK("otp_cancel")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in otp_inputs:
        del otp_inputs[user_id]
    await callback_query.message.delete()
    await bot.send_message(user_id, "<blockquote>❌ Pembatalan otomatis!\n🔄 Gunakan /start untuk memulai ulang</blockquote>")

@PY.CALLBACK("^(p_ub|n_ub)")
async def _(client, callback_query):
    query = callback_query.data.split()
    count = int(query[1])
    if query[0] == "n_ub":
        if count == len(ubot._ubot) - 1:
            count = 0
        else:
            count += 1
    elif query[0] == "p_ub":
        if count == 0:
            count = len(ubot._ubot) - 1
        else:
            count -= 1
    await callback_query.edit_message_text(
        await MSG.UBOT(count),
        reply_markup=InlineKeyboardMarkup(
            BTN.UBOT(ubot._ubot[count].me.id, count)
        ),
    )
