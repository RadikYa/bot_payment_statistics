from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
SPREADSHEET_SCRIPT_URL = os.getenv("SPREADSHEET_SCRIPT_URL")

@app.route("/")
def home():
    return "Webhook is running!"

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def telegram_webhook():
    data = request.json
    if not data:
        return "No data received", 400

    # Проверяем, содержит ли сообщение 'to'lov:'
    message = data.get("message", {}).get("text", "")
    if "to'lov:" in message:
        requests.post(SPREADSHEET_SCRIPT_URL, json={"message": message})
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
