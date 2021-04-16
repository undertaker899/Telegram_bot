import telebot
import textwrap
from config import currency, TOKEN
from extensions import ConvertException, CurrencyConverter


bot = telebot.TeleBot(TOKEN)


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


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        user_input = message.text.split(' ')

        if len(user_input) != 3:
            raise ConvertException('Неправильное количество параметров')

        quote, base, amount = user_input
        sample = CurrencyConverter.get_price(quote, base, amount)

    except ConvertException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать комманду\n{e}')

    else:
        text = f'Цена {amount} {quote} в {base} - {sample}'
        bot.send_message(message.chat.id, text)


bot.polling()
