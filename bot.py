import telebot
import parser
import logging

#main variables

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    print(message)
    bot.send_message(message.chat.id, 'Hi! I am ready for requests...')

@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "/translate":
        bot.send_message(chat_id, 'Please, enter text for translation...')
    elif text.startswith("/translate"):
        txt = text[11:]
        bot.send_message(chat_id, 'translation for <' + txt + '>: ...in progress...')
    else:
        bot.send_message(chat_id, '...<translation>...')


bot.polling()
