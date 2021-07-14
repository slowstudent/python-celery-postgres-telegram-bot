from tasks import checkURLinDB
from tasks import getQuantityFromDB
from tasks import insertToDB
from tasks import parse
import telebot

TOKEN = '1793627630:AAExeGEASC7pdXR-8rz2thHhlGGY6pTabZI' 

#to run bot.py    
# python3 ./proj/bot.py

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Пожалуйста отправьте ссылку на сайт чтобы ")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, "Получена ссылка: " + message.text )
    bot.send_message(message.chat.id, "Ссылка обрабатывается, подождите")
    
    if (checkURLinDB(message.text)==True):
        bot.send_message(message.chat.id, "Количество тегов: " + str(getQuantityFromDB(message.text)))
    else:
        try:
            parsedHtmlstagsquantity = parse(message.text)
            insertToDB(message.text, parsedHtmlstagsquantity)
            bot.send_message(message.chat.id, "Количество тегов: " + str(parsedHtmlstagsquantity))
        except:
            bot.send_message(message.chat.id, "Ошибка! Введите ссылку правильно на пример https://www.google.com/")



bot.polling()