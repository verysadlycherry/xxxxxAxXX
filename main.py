import telebot
from random import randint

bot = telebot.TeleBot('7066672353:AAHkRCg9KNNvBp5OjvVqgAO0EI3fLm617xw')
@bot.message_handler(commands=['start'])
def start(message):
    print('start')
    global number
    number = randint(1, 100)
    bot.send_message(message.from_user.id, 'Слыш чел го играть в угадай число!?\nЯ загадал число от 1 до 100')
@bot.message_handler()
def game(message):
    print('game')
    choice = message.text
    if choice.insumeric():
        if int(choice) > number:
            bot.send.message(message.from_user.id,'Меньше!(лОх)')
        elif int(choice) < number:
            bot.send.message(message.from_user.id,'Больше!(ЛоХ)')
        else:
            bot.send.message(message.from_user.id,'Алилуя! ты угадал! инвалид зря потратил время на тебя /start')
    else:
        bot.send.message(message.from_user.id, 'Эу чушпан вводи только цыферки не мороси!')
    
bot.polling(none_stop=True, interval=0)