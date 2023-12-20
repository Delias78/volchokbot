import random
import telebot
import webbrowser
from telebot import types


bot = telebot.TeleBot('5902304259:AAGFClyODpGPoB4qjk4IhDo3iujlksIljaI')

answers = ['Я не понял, что ты хочешь сказать.', 'Извини, я тебя не понимаю.', 'Я не знаю такой команды.']


@bot.message_handler(commands=['start'])
def welcome(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('👜 Товары')
    button2 = types.KeyboardButton('⚠️ Настройки')
    button3 = types.KeyboardButton('🎄Розыгрыш🎄')
    
    markup.row(button1)
    markup.row(button2, button3)

    if message.text == '/start':
        
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nУ меня ты сможешь купить некоторые товары!\nКонтакт моего разработчика: https://t.me/Delias78', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Перекинул тебя в главном меню! Выбирай!', reply_markup=markup)


@bot.message_handler(content_types='photo')
def get_photo(message):
    bot.send_message(message.chat.id, 'У меня нет возможности просматривать фото :(')


@bot.message_handler()
def info(message):
    if message.text == '👜 Товары':
        goodsChapter(message)
    elif message.text == '⚠️ Настройки':
        settingsChapter(message)
    elif message.text == '🎄Розыгрыш🎄':
        infoChapter(message)
    elif message.text == '🔥 AWP':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '🧊AWP | Lightning Strike (Factory New)🧊 Цена - 150💲:https://steamuserimages-a.akamaihd.net/ugc/1676989625779831505/E187DA060F4F03EA5A8BCF178395ADF8B54F20E5/: ⬇Определился с заказом? Жми Купить⬇', reply_markup=markup)
    elif message.text == '🔥 AK-47':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '🧊AK-47 | Vulcan (Factory New)🧊 Цена - 185💲:https://steamuserimages-a.akamaihd.net/ugc/842587655434020411/97876671CC8DA4354E90665F1B0E35FE77DB4968/?imw=512&amp;imh=288&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true: ⬇Определился с заказом? Жми Купить⬇', reply_markup=markup)
    elif message.text == '🔥 M4A4':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '🧊M4A4 | Temukau (Factory New)🧊 Цена - 80💲:https://sun9-32.userapi.com/impg/tOsiTXo0XyhhMmOtS_EbLpNr1bFCAaxmBHlAcA/47e8HYdsf64.jpg?size=807x454&quality=95&sign=afa9b57b59293b0461279560a8e9e3f8&c_uniq_tag=d0ji7WaQJR18MlWif2bzvgOnsEi9whnKAFpDf55Xf1U&type=album: ⬇Определился с заказом? Жми Купить⬇', reply_markup=markup)
    elif message.text == '🔥 KNIFE':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '🧊Karambit | Fade (Factory New)🧊 Цена - 455💲:https://steamuserimages-a.akamaihd.net/ugc/619592442071810451/2F0666C24DA7A77E17E038626FDA552538E711F7/?imw=512&amp;imh=384&amp;ima=fit&amp;impolicy=Letterbox&amp;imcolor=%23000000&amp;letterbox=true: ⬇Определился с заказом? Жми Купить⬇', reply_markup=markup)
    elif message.text == '👑 Создатель':
        
        bot.send_message(message.chat.id, '🦸🏻‍♂️Создатель магазина - Ярослав Волчок🦸🏻‍♂️')
    elif message.text == '🚨 Поддержка':
        
        bot.send_message(message.chat.id, '🌏Друг если ты нам хочешь продать скины или у тебя выбивает неизвестную ошибку пиши🌏: https://t.me/Delias78')
    elif message.text == '💳 Купить' or message.text == '💳Купить':
        bot.send_message(message.chat.id, 'https://t.me/Delias78')
    
    elif message.text == '💳 Купить' or message.text == '🎄Нажми что бы участвовать🎄':
        bot.send_message(message.chat.id, '🌌Первый скин AK-47 BLOOD SPORT🌌 - https://avatars.dzeninfra.ru/get-zen_doc/242954/pub_5bf59056d238aa00aac52988_5bf82b76bbe96600a90c9f74/scale_1200')
        bot.send_message(message.chat.id, '🌌Второй скин MP9 BULLDOZER🌌 - https://gocsgo.net/wp-content/uploads/2019/06/mp9-buldozer-7600.jpg')
        bot.send_message(message.chat.id, '🌌Третье оружие DESERT EAGLE CODE RED🌌 - https://avatars.mds.yandex.net/i?id=f8702195b3d33c859a0604c429ebe7dc28e2ff71-5329285-images-thumbs&n=13')
    elif message.text == '↩️ Назад':
        goodsChapter(message)
    elif message.text == '↩️ Назад в меню':
        welcome(message)
    else:
        bot.send_message(message.chat.id, answers[random.randint(0, 3)])


def goodsChapter(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    x = ['🔥 AWP','🔥 AK-47','🔥 M4A4','🔥 KNIFE']
    for i in x:
        markup.row( types.KeyboardButton(i))

    button5 = types.KeyboardButton('↩️ Назад в меню')  
    markup.row(button5)

    
    bot.send_message(message.chat.id, 'Вот все товары, которые сейчас находятся в продаже:', reply_markup=markup)


def settingsChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('👑 Создатель')
    button2 = types.KeyboardButton('🚨 Поддержка')
    button3 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3)
    bot.send_message(message.chat.id, 'Раздел настроек.\nВыбери один из вариантов:', reply_markup=markup)


def infoChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🎄Нажми что бы участвовать🎄')
    button2 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    bot.send_message(message.chat.id, 'Розыгрыш.\nЗдесь ты можешь выиграть классные скины, что бы участвовать подпишись на мой YouTube - https://www.youtube.com/channel/UCWJwDsOD02p5gXWjTDfaFCQ', reply_markup=markup)


bot.polling(none_stop=True)