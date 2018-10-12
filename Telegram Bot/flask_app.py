#!/usr/bin/python3.6
from flask import Flask, request
import telepot
import urllib3

proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

bot = telepot.Bot('645239619:AAFXXcAJqknENkilDRY7aK_qUlt84A3PqY0')
secret = "c152878e-fa90-438f-9a88-72783ce95375"
bot.setWebhook("https://jordenseet.pythonanywhere.com/{}".format(secret), max_connections=1)

app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"]) 
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        text = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]
        if text == "/start":
            bot.sendMessage(chat_id, "Hi! What is your Employer Id?")
        elif text == "123456":
            bot.sendMessage(chat_id, "Which of your employees would you like to give feedback on?")
        elif text == "Paul":
            bot.sendMessage(chat_id, "What is your feedback on Paul?")
        elif text == "Paul has been doing great work!":
            bot.sendMessage(chat_id, "Thank you for your feedback! Would you like to rate Paul's service?")
        elif text == "Yes":
            bot.sendMessage(chat_id, "How much would you rate Paul out of 10?")
        else: 
            bot.sendMessage(chat_id, "Thank you so much for your rating! We hope you continue to support MINDS")
    return "OK"
    
