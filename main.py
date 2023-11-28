import telebot

bot = telebot.TeleBot('6939690891:AAHNepDaXO_iCdoOLgsS5zyLTCjirEr-FWk')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Закажите такси через телеграмм!', parse_mode='Markdown')


@bot.message_handler(commands=['order'])
def main(message):
    bot.send_message(message.chat.id,
                     'Введите полный адрес отправления, включая город, улицу, дом и квартиру. Укажите также ваше имя и номер телефона для связи.',
                     parse_mode='Markdown')


@bot.message_handler(commands=['cancel'])
def main(message):
    bot.send_message(message.chat.id, 'Ваш заказ в такси был отменён!', parse_mode='Markdown')


@bot.message_handler(commands=['tariffs'])
def main(message):
    bot.send_message(message.chat.id, '''Такси в нашем сервисе предлагает 5 классов комфорта:

Стандарт - самый экономичный вариант. Подходит для коротких поездок по городу. Средняя стоимость: 200-300 рублей.
Эконом - оптимальное сочетание цены и комфорта. Подходит для большинства поездок. Средняя стоимость: 300-450 рублей.
Комфорт - повышенный уровень комфорта и удобства. Идеально подходит для длительных поездок и поездок с детьми. Средняя стоимость: 500-700 рублей.
Бизнес - максимальный уровень комфорта и безопасности. Идеально для деловых поездок и встреч. Средняя стоимость: 800-1200 рублей.
VIP - элитный класс с индивидуальным подходом к каждому клиенту. Для самых взыскательных пассажиров. Средняя стоимость: от 1500 рублей и выше.''',
                     parse_mode='Markdown')


bot.infinity_polling()