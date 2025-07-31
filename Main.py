import telebot
import os
from flask import Flask, request

API_TOKEN = '8084299106:AAFMsIv0zTXaALyKQAByATMfHkC3hMIqV5A'
bot = telebot.TeleBot(API_TOKEN)
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_msg(message):
    bot.send_message(message.chat.id, "👋 Welcome to *GUARDIAN ASCENSION FLIP AI*.\n\n🚀 Flip your account from $10 to $10,000+\nUse /help to learn how to begin.", parse_mode="Markdown")

@bot.message_handler(commands=['help'])
def help_msg(message):
    bot.send_message(message.chat.id, "📘 *Help Guide:*\n\n- `/start` — Welcome message\n- `/pay` — Payment info\n- `/results` — Trading results\n\nNeed help? Contact support.", parse_mode="Markdown")

@bot.message_handler(commands=['pay'])
def pay_msg(message):
    bot.send_message(message.chat.id, "💳 *Payment Instructions:*\n\nSend activation fee to: `+1234567890` via [M-Pesa or BTC Wallet]\nThen send proof here.", parse_mode="Markdown")

@bot.message_handler(commands=['results'])
def results_msg(message):
    bot.send_message(message.chat.id, "📈 *Latest Results:*\n\n- XAUUSD: +540 pips 🔥\n- BTCUSD: +13% in 2 days 💰\n- NAS100: +820 points 🚀\n\nYour flip starts now!", parse_mode="Markdown")

@server.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_messages([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "OK", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://your-app-name.onrender.com/' + API_TOKEN)
    return "Bot deployed", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
