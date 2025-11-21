import os
import requests
from PyroUbot import *

# Masukkan API Key Anda di sini
API_KEY = "moire"  # Ganti dengan API key yang benar

__MODULE__ = "ᴇᴘʜᴏᴛᴏ 1"
__HELP__ = """
<b>🖼️ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴇᴘʜᴏᴛᴏ 1 🖼️</b>

<blockquote><b>🎨 ᴇꜰᴇᴋ ᴛᴇxᴛ ᴛᴏ ɪᴍᴀɢᴇ:
• <code>{0}tv [text]</code> - ᴇꜰᴇᴋ ᴛᴠ ʙʟᴀᴄᴋ ᴡʜɪᴛᴇ
• <code>{0}glass [text]</code> - ᴇꜰᴇᴋ ɢʟᴀssᴇs
• <code>{0}bp [text]</code> - ᴇꜰᴇᴋ ʙʟᴀᴄᴋ ᴘɪɴᴋ
• <code>{0}bp2 [text]</code> - ᴇꜰᴇᴋ ʙʟᴀᴄᴋ ᴘɪɴᴋ 2
• <code>{0}cp [text]</code> - ᴇꜰᴇᴋ ᴄᴏᴠᴇʀ ᴘᴜʙɢ</b></blockquote>

<blockquote><b>✨ ᴜʙᴀʜ ᴛᴇxᴛ ᴍᴇɴᴊᴀᴅɪ ɪᴍᴀɢᴇ ᴅᴇɴɢᴀɴ ᴇꜰᴇᴋ ᴋᴇʀᴇɴ!</b></blockquote>
"""

def fetch_image(api_url, text):
    """
    Fungsi untuk mengambil gambar dari API
    """
    params = {"text": text, "apikey": API_KEY}
    try:
        response = requests.get(api_url, params=params)
        response.raise_for_status()

        if response.headers.get("Content-Type", "").startswith("image/"):
            return response.content
        else:
            print("Response bukan gambar:", response.text)  # Debugging
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching image: {e}")  # Debugging jika ada kesalahan
        return None

async def process_image_command(client, message, api_url, command_name):
    """
    Fungsi umum untuk menangani perintah pembuatan gambar
    """
    args = message.text.split(" ", 1)
    if len(args) < 2:
        await message.reply_text(f"<b><i>Gunakan perintah /{command_name} <teks> untuk membuat gambar.</i></b>")
        return

    request_text = args[1]
    await message.reply_text("<b><i>Sedang memproses, mohon tunggu...</i></b>")

    image_content = fetch_image(api_url, request_text)
    if image_content:
        temp_file = f"{command_name}.jpg"
        with open(temp_file, "wb") as f:
            f.write(image_content)
        await message.reply_photo(photo=temp_file)
        os.remove(temp_file)
    else:
        await message.reply_text("Gagal membuat gambar. Coba lagi nanti.")

# Handler untuk setiap perintah
@PY.UBOT("tv")
async def eraser_command(client, message):
    api_url = "https://api.botcahx.eu.org/api/ephoto/televisi"
    await process_image_command(client, message, api_url, "televisi")

@PY.UBOT("glass")
async def papercut_command(client, message):
    api_url = "https://api.botcahx.eu.org/api/ephoto/papercut"
    await process_image_command(client, message, api_url, "papercut")
    
@PY.UBOT("bp")
async def papercut_command(client, message):
    api_url = "https://api.botcahx.eu.org/api/ephoto/blackpink"
    await process_image_command(client, message, api_url, "blackpink")

@PY.UBOT("bp2")
async def papercut_command(client, message):
    api_url = "https://api.botcahx.eu.org/api/ephoto/blackpink2"
    await process_image_command(client, message, api_url, "blackpink2")
    
@PY.UBOT("bp2")
async def papercut_command(client, message):
    api_url = "https://api.botcahx.eu.org/api/ephoto/coverpubg"
    await process_image_command(client, message, api_url, "coverpubg")