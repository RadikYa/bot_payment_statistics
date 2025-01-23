from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
SPREADSHEET_SCRIPT_URL = os.getenv("SPREADSHEET_SCRIPT_URL")

@app.route('/webhook', methods=['POST'])
def home():
    # Получаем данные из запроса
    data = request.json
    print(f"Received data: {data}")  # Лог для проверки
    return "OK", 200

# Главная страница для проверки работы сервера (опционально)
@app.route('/', methods=['GET'])
def home():
    return "Webhook server is running!", 200

    # Проверяем, содержит ли сообщение 'to'lov:'
    message = data.get("message", {}).get("text", "")
    if "to'lov:" in message:
        requests.post(SPREADSHEET_SCRIPT_URL, json={"message": message})
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
