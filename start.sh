#!/bin/bash
# PyroUbot Auto Installer + ENV Generator + Runner

clear
echo "========================================="
echo "     PyroUbot Auto Setup Environment"
echo "========================================="
echo ""

### =====================================
### 1. Copy sample.env -> .env
### =====================================

if [ ! -f "sample.env" ]; then
    echo "❌ sample.env tidak ditemukan! Buat dulu file sample.env!"
    exit 1
fi

cp sample.env .env
echo "📁 File .env berhasil dibuat dari sample.env"
echo ""


### =====================================
### 2. INPUT MANUAL USER
### =====================================

echo "Silakan isi data berikut:"
echo ""

read -p "Masukkan BOT_TOKEN: " BOT_TOKEN
read -p "Masukkan API_ID (dari https://my.telegram.org): " API_ID
read -p "Masukkan API_HASH (dari https://my.telegram.org): " API_HASH
read -p "Masukkan OWNER_ID: " OWNER_ID
read -p "Masukkan OWNER_NAME: " OWNER_NAME
read -p "Masukkan OWNER_LINK (contoh: t.me/username): " OWNER_LINK


### =====================================
### 3. AUTO VALUE
### =====================================

FEE_TRANSAKSI=200
API_ATLANTIC="2aOJDZWsUg3u1eMxIYmd9nFGNE2EXtOboJ8OiR1EcIFji9bpLrs8WuSypqiPa3ieMpBiZAkgoLUoh2zBPgafmZPP5FTYANxxoaJa"
BLACKLIST_CHAT="-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283"
RMBG_API="MA2sUZ4HdAfBegL36HiG4BUG"
MONGO_URL="mongodb+srv://fizzpamell:fizzpamell@cluster0.9nmhi5m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
LOGS_MAKER_UBOT="-4628173231"


### =====================================
### 4. TULIS ULANG .env DENGAN NILAI TERISI
### =====================================

cat > .env <<EOF
API_ID=$API_ID
API_HASH=$API_HASH
BOT_TOKEN=$BOT_TOKEN
OWNER_ID=$OWNER_ID
OWNER_NAME=$OWNER_NAME
OWNER_LINK=$OWNER_LINK

FEE_TRANSAKSI=$FEE_TRANSAKSI
API_ATLANTIC=$API_ATLANTIC
BLACKLIST_CHAT=$BLACKLIST_CHAT
RMBG_API=$RMBG_API
MONGO_URL=$MONGO_URL
LOGS_MAKER_UBOT=$LOGS_MAKER_UBOT

BOT_FOOTER=🛠️ Ibra Decode Userbot 🛠️
EOF

echo ""
echo "✅ ENV berhasil dibuat dan diisi!"
echo ""


### =====================================
### 5. INSTALL DEPENDENCIES
### =====================================

echo "=== UPDATE SISTEM ==="
apt update && apt upgrade -y

echo "=== INSTALL DEPENDENCIES ==="
apt install -y ffmpeg python3.10-venv curl
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt install -y nodejs
npm install -g uglify-js


### =====================================
### 6. SETUP VENV
### =====================================

if [ ! -d "venv" ]; then
    echo "Membuat virtual environment..."
    python3 -m venv venv
fi

echo "Aktifkan venv..."
source venv/bin/activate

echo "Install requirements..."
pip install --upgrade pip
pip install -r requirements.txt


### =====================================
### 7. RUN BOT
### =====================================

echo ""
echo "======================================="
echo "   SEMUA SELESAI! MENJALANKAN BOT..."
echo "======================================="
echo ""

python3 -m PyroUbot
