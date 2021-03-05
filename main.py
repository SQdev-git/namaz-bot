import telebot
import function as func
from config import *
from keyboard import *
import urllib

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Здравствуйте я простой бот который указывает время намаза в указанном месте\n Чтобы узнать время молитвы напишите имя Государства')
    bot.register_next_step_handler(message, get_country)
    
    
@bot.message_handler(content_types="text")
def get_country(message):
    try:
        for num in range(1,5):
            bot.delete_message(message.chat.id, message.message_id-num)
    except Exception as e:
        pass
    if message.text:
        checker = func.get_dic_country(message.text.lower())
        if not (func.get_dic_country(message.text.lower())) is False:
            bot.send_message(message.chat.id, '\t😊 Государства найдено.\n ⏬Используйте клавиши для навигации⏬', reply_markup= generate_key('reg', func.get_api_reg(checker[1])))
        elif checker is False:
            bot.send_message(message.chat.id, '🤷🏻‍♂️ Государства не найдено пишите правильно.')
            bot.register_next_step_handler(message, get_country)
@bot.callback_query_handler(func=lambda c:True)
def main(c):
    datas = c.data.split("()")
    if len(datas)>1:
        if datas[0]=='reg':
            bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id,text= 'Шаҳри дар ин вилоятбударо интихоб кунед', reply_markup=generate_key('city', func.get_api_city(datas[1])))
        elif datas[0]=='city':
            bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text= 'Интизор шавед...')
            bot.edit_message_text(chat_id=c.message.chat.id, message_id=c.message.message_id, text=func.get_api_time(datas[1]))
    elif c.data=='exit':
        bot.delete_message(c.message.chat.id, c.message.message_id)
        try:
            for num in range(1, 5):
                bot.delete_message(c.message.chat.id, c.message.message_id-num)
        except:
            pass

    


bot.polling(none_stop=False)