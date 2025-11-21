import requests
import wget
import os
from pyrogram import Client
from PyroUbot import *

__MODULE__ = "ʟʏʀɪᴄꜱ"
__HELP__ = """
<b>🎵 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟʏʀɪᴄs 🎵</b>

<blockquote><b>🎤 ᴄᴀʀɪ ʟʏʀɪᴄs:
• <code>{0}lyrics [judul]</code> - ᴄᴀʀɪ ʟʏʀɪᴄs ʟᴀɢᴜ</b></blockquote>

<blockquote><b>🎶 ᴛᴇᴍᴜᴋᴀɴ ᴋᴀᴛᴀ ʟᴀɢᴜ ꜰᴀᴠᴏʀɪᴛᴍᴜ!</b></blockquote>
"""

@PY.UBOT("lyrics")
async def lyrics(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    
    jalan = await message.reply(f"{prs} Processing...")
    
    if len(message.command) != 2:
        return await jalan.edit(f"{ggl} Please use the command `lyrics` judul music.")
    
    lyrics = message.command[1]
    chat_id = message.chat.id
    url = f"https://widipe.com/lirik?text={lyrics}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            hasil = data['result']
            lyrics = hasil['lyrics']
            photoUrl = f"https://cdn.vectorstock.com/i/1000v/71/92/music-lyrics-logo-mark-for-concert-vector-35117192.jpg"
            caption = f"""
<b><emoji id=5841235769728962577>⭐</emoji>{lyrics}</b>
"""
            photo_path = wget.download(photoUrl)
            await client.send_photo(chat_id, caption=caption, photo=photo_path)
            if os.path.exists(photo_path):
                os.remove(photo_path)
            
            await jalan.delete()
        else:
            await jalan.edit(f"{ggl} No 'result' key found in the response.")
    
    except requests.exceptions.RequestException as e:
        await jalan.edit(f"{ggl} Request failed: {e}")
    
    except Exception as e:
        await jalan.edit(f"{ggl} An error occurred: {e}")
