import telebot 
from telebot import types
from telebot.types import ReplyKeyboardMarkup
from telebot.types import ForceReply 


TOKEN =  '6715887878:AAGzEaCyOAc9KQCPU3JOP9E_6vtjqTwoz90' 

bot = telebot.TeleBot(TOKEN) 

@bot.message_handler(commands=['start'])
def send_welcome(message): 
    bot.send_message(message.chat.id, 'Bienvenid@')

@bot.message_handler(content_types=['text'])
def send_options(message): 
    if message.text.startswith('/'): 
        bot.send_message(message.chat.id, 'Comando no disponible')
    else: 
        markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder='Pulsar opciones', resize_keyboard=True)
        markup.add('Tecno', 'Info', 'Ayuda')
        msg = bot.send_message(message.chat.id, '¿En que te podemos ayudar?', reply_markup=markup)
        bot.register_next_step_handler(msg, guardar) 

def tecnologia(message): 
    bot.send_message(message.chat.id, 'esta parte habla sobre nuestra tecnologia  ')


def informacion (message): 
    bot.send_message(message.chat.id, 'esta parte nos da mas informacion sobre nosotros ')

def ayuda(message): 
    bot.send_message(message.chat.id, 'esta parte habl sobre la ayuda que te podemos brindar ') 


def guardar(message): 
    if message.text !='Tecno' and message.text != 'Info' and message.text != 'Ayuda':  
        send_options(message) 
    else: 
        if message.text == 'Tecno': 
            print('Tecno')
            tecnologia(message)
        elif message.text == 'Info': 
            print('Info')
            informacion(message)
        elif message.text == 'Ayuda': 
            print('Ayuda') 
            ayuda(message)  


if __name__ == '__main__': 
    bot.infinity_polling() 
