#pip install bs4
#pip install telebot
#pip install requests

from bs4 import BeautifulSoup
import requests
import telebot
from telebot import types


url = "https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%A7%D0%B5%D1%80%D0%B5%D0%BF%D0%BE%D0%B2%D1%86%D0%B5"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

temp = soup.find('span', style = 'display: block;').text



bot = telebot.TeleBot("6448903614:AAG9PhcM3DBvEGO2WKSJNUNicT3dRFDah2g")



@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}") 


@bot.message_handler(commands=["weather"])
def main(message):
    bot.send_message(message.chat.id, {temp})
    

@bot.message_handler(commands=["anecdote1"])
def main(message):
    bot.send_message(message.chat.id, "Внимание, анекдот! Колобок повесился")


@bot.message_handler(commands=["anecdote2"])
def main(message):
    bot.send_message(message.chat.id, "Внимание, анекдот! Буратино утонул")


@bot.message_handler(commands=["anecdote3"])
def main(message):
    bot.send_message(message.chat.id, "Внимание, анекдот! Что говорила Чуковскому мама, когда он просил конфеты до обеда? Корней нет")



bot.polling(none_stop=True)