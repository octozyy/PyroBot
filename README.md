# PyroUbot Premium - Userbot Telegram Terbaik

Userbot Telegram premium dengan fitur lengkap, UI modern, dan performa tinggi. Dibangun dengan Pyrogram untuk pengalaman terbaik.

## Fitur Utama

### Bot Management
- **Multi-Userbot**: Support hingga 100 userbot
- **Auto Join**: Otomatis join channel tertentu
- **Premium System**: Sistem pembelian premium dengan QRIS otomatis
- **Restart & Control**: Kontrol penuh userbot

### UI & UX
- **Start Menu**: Gambar dan tombol interaktif
- **Inline Menus**: Navigasi dengan emoji dan pagination
- **OTP Input**: Input kode OTP via tombol (bukan typing)
- **Responsive Design**: UI yang stylish dan mudah digunakan

### Modul Lengkap
- **Admin Tools**: Ban, mute, kick, dll
- **Media Tools**: Download YouTube, TikTok, Instagram
- **Fun & Games**: Quotes, games, animasi
- **Utilities**: Weather, calculator, translate
- **Security**: Anti-spam, blacklist
- **Dan banyak lagi**: 150+ modul tersedia

### Payment System
- **Manual Payment**: Transfer Dana dengan konfirmasi
- **Auto QRIS**: Generate QRIS otomatis via API Atlantic
- **Premium Management**: Expired date, status check

## Instalasi & Setup

### Persyaratan Sistem
- Python 3.10+
- Node.js 20+
- FFmpeg
- VPS/Cloud dengan RAM 1GB+

### Setup Otomatis
```bash
# Update sistem
apt update && apt upgrade -y

# Install dependencies
apt install ffmpeg python3.10-venv -y
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt-get install -y nodejs

# Clone repository
git clone https://github.com/IbraDecode/PyroUbot.git
cd PyroUbot

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python packages
pip install -r requirements.txt
```

### Konfigurasi
```bash
# Copy sample config
cp sample.env .env

# Edit config
nano .env
```

**Isi .env dengan:**
```env
API_ID=your_api_id          # Dari https://my.telegram.org
API_HASH=your_api_hash      # Dari https://my.telegram.org
BOT_TOKEN=your_bot_token    # Dari @BotFather
OWNER_ID=your_telegram_id   # ID Telegram Anda
OWNER_NAME=Your Name        # Nama Anda
OWNER_LINK=t.me/yourusername # Link Telegram Anda
BOT_FOOTER=🛠️ PyroUbot 🛠️ # Footer bot
API_ATLANTIC=your_api_key   # Untuk QRIS (opsional)
FEE_TRANSAKSI=1000          # Fee transaksi
LOGS_MAKER_UBOT=-1001234567890 # Channel logs
```

### Menjalankan Bot
```bash
# Jalankan bot
python3 -m PyroUbot

# Atau dengan screen
screen -S PyroUbot
python3 -m PyroUbot
```

### Restart Bot
```bash
# Jika bot mati
cd PyroUbot
source venv/bin/activate
screen -S PyroUbot
python3 -m PyroUbot
```

## Struktur Project

```
PyroUbot/
├── PyroUbot/              # Source code utama
│   ├── __main__.py       # Entry point
│   ├── config.py         # Konfigurasi
│   ├── core/             # Core functions
│   │   ├── helpers/      # Helper functions
│   │   ├── database/     # Database handlers
│   │   └── function/     # Utility functions
│   └── modules/          # Bot modules (150+)
├── PyroUbot_enc/         # Versi obfuscated (protected)
├── venv/                 # Virtual environment
├── .env                  # Config file
├── requirements.txt      # Python dependencies
├── start.sh             # Start script
└── README.md            # This file
```

## Versi Obfuscated

Untuk keamanan ekstra, gunakan versi obfuscated:
```bash
python3 PyroUbot_enc/__main__.py
```

## Troubleshooting

### Error Speedtest
Sudah diperbaiki - pastikan `speedtest-cli` terinstall

### Error UVLoop
Sudah diperbaiki - otomatis install

### Bot Tidak Respon
- Cek API credentials
- Restart bot
- Cek logs untuk error

### OTP Tidak Masuk
- Pastikan nomor valid
- Cek spam folder
- Gunakan input tombol untuk memasukkan kode

## Support & Community

- **Channel**: [Ibra Channel](t.me/ibradecodee)
- **Group Support**: [Decode Community](t.me/decode_gb)
- **Developer**: [Ibra Decode](t.me/ibradecode)

## 📝 Lisensi

This project is licensed under the MIT License - see the LICENSE file for details.

---

**⚠️ Disclaimer**: Gunakan bot ini dengan bijak. Owner tidak bertanggung jawab atas penyalahgunaan.

**❤️ Thanks to**: Ibra Decode, Pyrogram, Telegram, dan semua kontributor.
