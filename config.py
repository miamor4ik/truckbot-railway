import os

BOT_TOKEN = os.getenv("BOT_TOKEN")  # Telegram bot token
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # полный URL Cloudflare Worker (пример: https://truckbot.myworkers.dev/)
# Путь на Railway — для локального теста можно оставить пустым