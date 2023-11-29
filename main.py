# import telebot 
# from telebot import types
# from telebot.types import ReplyKeyboardMarkup
# from telebot.types import ForceReply 


# TOKEN =  '6715887878:AAGzEaCyOAc9KQCPU3JOP9E_6vtjqTwoz90' 

# bot = telebot.TeleBot(TOKEN) 

# @bot.message_handler(commands=['start'])
# def send_welcome(message): 
#     bot.send_message(message.chat.id, 'Bienvenid@')

# @bot.message_handler(content_types=['text'])
# def send_options(message): 
#     if message.text.startswith('/'): 
#         bot.send_message(message.chat.id, 'Comando no disponible')
#     else: 
#         markup = ReplyKeyboardMarkup(one_time_keyboard=True, input_field_placeholder='Pulsar opciones', resize_keyboard=True)
#         markup.add('Tecno', 'Info', 'Ayuda')
#         msg = bot.send_message(message.chat.id, '¿En que te podemos ayudar?', reply_markup=markup)
#         bot.register_next_step_handler(msg, guardar) 


# def tecnologia(message): 
#     bot.send_message(message.chat.id, 'esta parte habla sobre nuestra tecnologia  ')


# def informacion (message): 
#     bot.send_message(message.chat.id, 'esta parte nos da mas informacion sobre nosotros ')

# def ayuda(message): 
#     bot.send_message(message.chat.id, 'esta parte habl sobre la ayuda que te podemos brindar ') 


# def guardar(message): 
#         if message.text == 'Tecno': 
#             print('Tecno')
#             tecnologia(message)
#         elif message.text == 'Info': 
#             print('Info')
#             informacion(message)
#         elif message.text == 'Ayuda': 
#             print('Ayuda') 
#             ayuda(message)  


# if __name__ == '__main__': 
#     bot.infinity_polling() 


import telebot 
from telebot.types import InlineKeyboardButton
from telebot.types import InlineKeyboardMarkup 
import telegram.ext 


TOKEN =  '6715887878:AAGzEaCyOAc9KQCPU3JOP9E_6vtjqTwoz90' 
Updater = telegram.ext.Updater(TOKEN, update_queue=True) 

bot = telebot.TeleBot(TOKEN) 

@bot.message_handler(commands=['botones'])
def botones(message): 
    markup = InlineKeyboardMarkup(row_width=2)
    b1 = InlineKeyboardButton('Tecnologia', callback_data='tecno')
    b2 = InlineKeyboardButton('Info' , callback_data='info' )
    b3 = InlineKeyboardButton('Ayuda', callback_data='ayuda')  
    b4 = InlineKeyboardButton('Contacto', callback_data='contacto') 

    markup.add(b1,b2,b3,b4) 
    bot.send_message(message.chat.id, '¿En que te podemos ayudar?', reply_markup=markup) 


def tecno__info(menssage): 
    markup = InlineKeyboardMarkup(row_width=2)
    inf = InlineKeyboardButton('Informacion', callback_data='info_tecno') 
    precio =  InlineKeyboardButton('Precio', callback_data='precio') 

    markup.add(inf, precio)
    bot.send_message(message.chat.id, 'Mas informacion sobre tecnologia', reply_markup=markup) 
 
@bot.callback_query_handler(func=lambda call:True)   
def respuesta(call):  
    # cid = call.from_user.id
    # mid = call.message.id  
    if call.data == 'tecno':
        print('tecno') 
    elif call.data == 'info':  
        print('info')
    elif call.data == 'ayuda': 
        #hola 
        print('ayuda') 
    elif call.data =='contacto': 
        print('contacto')  
        #sdfjksbjkfbds


if __name__=='__main__': 
    bot.infinity_polling()  