import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

DEVS = list(map(int, os.getenv("DEVS", "1950085460").split()))

API_ID = int(os.getenv("API_ID", "20702296"))

API_HASH = os.getenv("API_HASH", "ae201c7defe82c2fe787f519849c902e")

BOT_TOKEN = os.getenv("BOT_TOKEN", "8331124355:AAHS1E-sW9YdvA9zAQl2uRbet2rcQFEZ2y0")

OWNER_ID = int(os.getenv("OWNER_ID", "1950085460"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002044997044 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "MA2sUZ4HdAfBegL36HiG4BUG")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://fizzpamell:fizzpamell@cluster0.9nmhi5m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-4628173231"))

OWNER_NAME = os.getenv("OWNER_NAME", "Xennpy")
OWNER_LINK = os.getenv("OWNER_LINK", "t.me/deakvy")

BOT_FOOTER = os.getenv("BOT_FOOTER", "Xennpy-Ubot")

API_ATLANTIC = os.getenv("API_ATLANTIC", "your_api_key")
FEE_TRANSAKSI = int(os.getenv("FEE_TRANSAKSI", 1000))
