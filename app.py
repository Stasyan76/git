import telebot
from config import TOKEN, valuta
from extensions import APIException, StaticValue


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['valuta'])
def get_money(message: telebot.types.Message):
    text = 'Примеры валют:\n'
    for i in valuta:
        text += f'\n{i}' + f' ({valuta.get(i)})'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['help', 'start'])
def get_info(message: telebot.types.Message):
    text = 'Чтобы узнать курс любой валюты, для этого вам нужно знать код валюты ISO 4217. ' \
           'Примеры таких кодов есть в /valuta\n\n' \
           'Пример ввода: RUB USD 1.\n\nСначала нужно вводить интересующую вас валюту, потом валюту ' \
           'в которую хотите перевести и в конце количество переводимой валюты.\n\n' \
           'Список команд: /start, /help, /valuta.'
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text'])
def get_values(message: telebot.types.Message):
    try:
        list_value = message.text.upper().split(' ')
        if len(list_value) != 3:
            raise APIException('Некорректное количество значений')
        base, quote, amount = list_value
        res = StaticValue.get_price(quote, base, amount)
    except APIException as e:
        bot.send_message(message.chat.id, f'Ошибка от пользователя\n{e}')
    except Exception as e:
        bot.send_message(message.chat.id, f'Ошибка программы\n{e}')
    else:
        bot.send_message(message.chat.id, f'Стоимость {amount} {base} равна '
                                          f'{res[quote] * float(amount)} {quote}')


if __name__ == '__main__':
    bot.infinity_polling()
