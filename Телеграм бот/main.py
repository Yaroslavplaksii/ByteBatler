import telebot
from telebot import types
chat_id=873937071
bot = telebot.TeleBot('6512681040:AAFq8PpyxSn8vb5mlnwIeVVHWmsPYMDtuKA')
@bot.message_handler(commands=['start'])
def start_command(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
    btn1 = types.KeyboardButton('Так')
   # btn2 = types.KeyboardButton('Ще не вирішив')
    btn3 = types.KeyboardButton('Ні')

    markup.add(btn1,btn3)
    
    bot.send_message(message.chat.id, "Привіт,😀" + message.from_user.first_name + "!\n".format(message.from_user, bot.get_me()),parse_mode='html')
    
    bot.send_message(message.chat.id,'Вітаємо у нашому інформаційному чат-боті! Ми завжди тут, щоб допомогти вам захистити себе від шахраїв і зберегти вашу безпеку.')
    
    send_mess = f"<b> {message.from_user.first_name} </b>!\nТи готовий до співпраці? "
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()
    if get_message_bot=='ні':
        final='Бувай'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
        btn1 = types.KeyboardButton('Вихід')
        markup.add(btn1)
    elif get_message_bot=='так':
        final='Чудово \n '
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
      #  btn1 = types.InlineKeyboardButton("Перевірка телефону", url='http://surl.li/gnxzp')
        btn1 = types.KeyboardButton('Перевірка телефону')
        btn2 = types.KeyboardButton('Перевірка сайту')
        btn3 = types.KeyboardButton('види шахрайств')
        btn4 = types.KeyboardButton('зорові обмеження')
       #btn5 = types.KeyboardButton('Головне меню')

        markup.add(btn1,btn2,btn3,btn4)

    elif get_message_bot=='перевірка телефону':

        final='https://web.getcontact.com/'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
    
        btn1=types.KeyboardButton('Головне меню')
        btn2=types.KeyboardButton('Повернутися назад')
        markup.add(btn1,btn2)
    elif get_message_bot=='перевірка сайту':

        final='https://transparencyreport.google.com/safe-browsing/search'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
    
        btn1=types.KeyboardButton('Головне меню')
        btn2=types.KeyboardButton('Повернутися назад')

        
        markup.add(btn1,btn2)
    elif get_message_bot=='види шахрайств':
        final='https://www.pravda.com.ua/podcasts/60b4f1001f5b2/2021/06/2/7295526/'
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
    
        btn1=types.KeyboardButton('Головне меню')
        btn2=types.KeyboardButton('Повернутися назад')
        markup.add(btn1,btn2)
    elif get_message_bot=='зорові обмеження':
        final='https://hromadske.radio/podcasts/drive-time/yak-vberehtysia-vid-shakhrays-kykh-kredytiv-iaki-vy-ne-braly'

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
    bot.send_message(message.chat.id,final,parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True)
