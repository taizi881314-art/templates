import os
from flask import Flask, request
import requests

app = Flask(__name__)
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8611596544:AAFNmpNMKYiGb1rwVvbxOF5tDycfViJtIWM")

def send_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": chat_id, "text": text})

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"].get("text", "")
        if text == "/start":
            send_message(chat_id, "机器人已启动！发送 /today")
        elif text == "/today":
            send_message(chat_id, "今日暂无数据")
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
