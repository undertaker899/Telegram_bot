import telebot
import textwrap
from config import currency, TOKEN
from extensions import APIException, CurrencyConverter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    sample_text = """
    User required to message bot in format (2 keywords and a number, with whitespace between each):\n
    1) "Name of currency, price of which user wants to know".
    2) "Name of currency, price in which user wants to know".
    3) "Amount of first currency to convert".\n
    For example: "Dollar Ruble 1500"\n
    If user enters command /values info about all available currencies is shown in readable format.
    """
    text = textwrap.dedent(sample_text)
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    sample_text = """
    Available currency for conversion:\n
    """
    text = textwrap.dedent(sample_text)

    for key in currency.keys():
        text = text + key + '\n'
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        user_input = message.text.split(' ')

        if len(user_input) != 3:
            raise APIException('Wrong number of parameters')

        quote, base, amount = user_input
        sample = CurrencyConverter.get_price(quote, base, amount)

    except APIException as e:
        bot.reply_to(message, f'User error:\n{e}')

    except Exception as e:
        bot.reply_to(message, f"Can't get response to command:\n{e}")

    else:
        text = f'Price of {amount} {quote} in {base} = {sample}'
        bot.send_message(message.chat.id, text)


bot.polling()
