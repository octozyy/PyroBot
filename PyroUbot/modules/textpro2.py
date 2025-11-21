import os
import requests
from PyroUbot import *

# Masukkan API Key Anda di sini
API_KEY = "moire"  # Ganti dengan API key yang benar

__MODULE__ = "ᴛᴇxᴛᴘʀᴏ 2"
__HELP__ = """
<b>🎨 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛᴇxᴛᴘʀᴏ 2 🎨</b>

<blockquote><b>✨ ᴇꜰᴇᴋ ᴛᴇxᴛ ᴛᴏ ɪᴍᴀɢᴇ:
• <code>{0}neon [text]</code> - ᴇꜰᴇᴋ ɴᴇᴏɴ
• <code>{0}neongalaxy [text]</code> - ᴇꜰᴇᴋ ɴᴇᴏɴ ɢᴀʟᴀxʏ
• <code>{0}neongreen [text]</code> - ᴇꜰᴇᴋ ɴᴇᴏɴ ɢʀᴇᴇɴ
• <code>{0}brokenglass [text]</code> - ᴇꜰᴇᴋ ʙʀᴏᴋᴇɴ ɢʟᴀss
• <code>{0}artpapper [text]</code> - ᴇꜰᴇᴋ ᴀʀᴛ ᴘᴀᴘᴘᴇʀ</b></blockquote>

<blockquote><b>🖼️ ᴜʙᴀʜ ᴛᴇxᴛ ᴍᴇɴᴊᴀᴅɪ ɪᴍᴀɢᴇ ᴅᴇɴɢᴀɴ ᴇꜰᴇᴋ ᴋᴇʀᴇɴ!</b></blockquote>
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
@PY.UBOT("neon")
async def eraser_command(client, message):
    api_url = "https://api.botcahx.eu.org/api/textpro/neon-light"
    await process_image_command(client, message, api_url, "neon-light")

@PY.UBOT("neongalaxy")
async def papercut_command(client, message):
    api_url = "https://api.botcahx.eu.org/api/textpro/neon-galaxy"
    await process_image_command(client, message, api_url, "neon-galaxy")

@PY.UBOT("neongreen")
async def papercut_command(client, message):
    api_url = "https://api.botcahx.eu.org/api/textpro/neon-green"
    await process_image_command(client, message, api_url, "neon-green")

@PY.UBOT("brokenglass")
async def papercut_command(client, message):
    api_url = "https://api.botcahx.eu.org/api/textpro/broken-glass"
    await process_image_command(client, message, api_url, "broken-glass")

@PY.UBOT("artpapper")
async def papercut_command(client, message):
    api_url = "https://api.botcahx.eu.org/api/textpro/art-papper"
    await process_image_command(client, message, api_url, "art-papper")