import telebot
from config import TOKEN
from extensions import ConvertionException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    start = 'Приветствую. Данный бот конвертирует валюты, в следующем формате: \n <<имя валюты>> \
<<в какую переводим>> <<какое количество переводим>> \n Пример: USD BTC 100 \n доступные валюты - /values'
    bot.reply_to(message, start)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    values = 'Обозначение валют: \n BTC - биткоин \n ETH - эфириум \n USD - доллар \n EUR - евро \n RUB - рубль \n \n \
Пример: USD BTC 100'
    bot.reply_to(message, values)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split()
        if len(values) != 3:
            raise ConvertionException('Слишком много параметров! \n Пример написания запроса: USD BTC 100')
        quote, base, amount = values
        total = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя.  \n {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n {e}')
    else:
        text = f'Цена {amount} {quote} в {base} = {total}'
        bot.send_message(message.chat.id, text)


bot.polling()








