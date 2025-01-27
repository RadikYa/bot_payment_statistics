from flask import Flask, request
import requests
import os
import logging

# Создание Flask приложения
app = Flask(__name__)

# Получение переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")
SPREADSHEET_SCRIPT_URL = os.getenv("SPREADSHEET_SCRIPT_URL")

# Настройка логирования
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def home():
    return "Webhook is running!"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def telegram_webhook():
    try:
        data = request.json
        if not data:
            logging.error("No data received")
            return "No data received", 400

        # Проверка наличия текста в сообщении
        message = data.get("message", {}).get("text", "")
        if "to'lov:" in message:
            # Отправка сообщения в Google Apps Script
            requests.post(SPREADSHEET_SCRIPT_URL, json={"message": message})
        return "OK", 200
    except Exception as e:
        # Логирование ошибок
        logging.exception(f"An error occurred: {e}")
        return "Internal Server Error", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))


