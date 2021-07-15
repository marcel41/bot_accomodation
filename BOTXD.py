import credentials
import telebot
import time
API_KEY = credentials.TELEGRAMAPI
bot = telebot.TeleBot(API_KEY)
@bot.message_handler(commands=['hello'])
def hello(message):
  print(message.chat.id)
  bot.send_message(message.chat.id, "Hello!")


while(True):
    time.sleep(10)
    bot.send_message(credentials.msg_ID, "Hello!")
