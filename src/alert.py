# alerts.py
import os
import requests
from dotenv import load_dotenv

# load .env dulu supaya kebaca
load_dotenv()

# Ambil URL dari env (lebih aman)
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord(message: str):
    """Kirim pesan sederhana ke Discord channel"""
    if not WEBHOOK_URL:
        raise RuntimeError("❌ DISCORD_WEBHOOK_URL belum diset di environment")

    payload = {"content": message}
    r = requests.post(WEBHOOK_URL, json=payload)

    if r.status_code == 204:
        print("✅ Alert terkirim ke Discord")
    else:
        print(f"⚠️ Gagal kirim alert: {r.status_code} - {r.text}")
