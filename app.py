import telebot
import textwrap


TOKEN = '1790745719:AAGZLxODapseLEFX-tI0yorGS2GjIEEoccY'

bot = telebot.TeleBot(TOKEN)

currency = {
    'доллар,': 'USD',
    'евро,': 'EUR',
    'рубль': 'RUB'
}


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    sample_text = """
    Человек должен отправить сообщение боту в виде (два ключевых слова и число, через пробел):\n
    1) "Имя валюты, цену которой он хочет узнать".
    2) "Имя валюты, в которой надо узнать цену первой валюты".
    3) "Количество первой валюты".\n
    Например: "USD RUB 1500"\n
    При вводе команды /values выводиться информация о всех доступных валютах в читаемом виде.
    """
    text = textwrap.dedent(sample_text)
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    sample_text = """
    Доступные валюты:\n
    """
    text = textwrap.dedent(sample_text)

    for key in currency.keys():
        text = ' '.join((text, key, ))
    bot.reply_to(message, text)


bot.polling()
