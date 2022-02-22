import telebot
import random

bot = telebot.TeleBot('TOKEN')
keyboard1 = telebot.types.ReplyKeyboardMarkup()

keyboard1.row('roll','d3','d4','d6', 'd8','d10','d12','d90')



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, какой кубик мне кинуть? /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'd4' or message.text.lower()==  'в4' or message.text.lower()==  'д4':
        itog= random.randint(1,4)
        bot.send_message(message.chat.id, itog)
    elif message.text.lower() == 'd6' or message.text.lower()==  'в6' or message.text.lower()==  'д6':
        itog2= random.randint(1,6)
        bot.send_message(message.chat.id, itog2)
    elif message.text.lower() == 'd8' or message.text.lower()==  'в8' or message.text.lower()==  'д8':
        itog3= random.randint(1,8)
        bot.send_message(message.chat.id, itog3)
    elif message.text.lower() == 'd10' or message.text.lower()==  'в10' or message.text.lower()==  'д10':
        itog4= random.randint(1,10)
        bot.send_message(message.chat.id, itog4)
    elif message.text.lower() == 'd12' or message.text.lower()==  'в12' or message.text.lower()==  'д12':
        itog5= random.randint(1,12)
        bot.send_message(message.chat.id, itog5)
    elif message.text.lower() == 'd90' or message.text.lower()==  'в90' or message.text.lower()==  'д90':
       itog6= random.choice([0,10,20,30,40,50,60,70,80,90])
       bot.send_message(message.chat.id, itog6)
    elif message.text.lower() == 'roll' or message.text.lower()==  'ролл' or message.text.lower()==  'рол' or message.text.lower()==  'rol':
       itog6= random.randint(0,9)
       itog7= random.choice([0,10,20,30,40,50,60,70,80,90])
       itog8= itog6+itog7
       #itog8= 'ТЕБЕ ПИЗДА'
       bot.send_message(message.chat.id, itog8)
    elif message.text.lower() == 'd3' or message.text.lower()==  'в3' or message.text.lower()==  'д3':
        itog9= random.randint(1,3)
        bot.send_message(message.chat.id, itog9)


bot.polling()