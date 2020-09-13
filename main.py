from botHandler import BotHandler
from datetime import datetime

from mock import MOCK

now = datetime.now()
greet_bot = BotHandler('1395793468:AAEsQ9pSg0SWRwoOd9tN77zATvI7Jz-gsj4')


# Приветствие
def get_hello(user_name):
    today = now.day
    hour = now.hour
    if today == now.day and 5 <= hour < 10:
        today += 1
        msg = 'Доброе утро, {}'.format(user_name)

    elif today == now.day and 10 <= hour < 17:
        today += 1
        msg = 'Добрый день, {}'.format(user_name)

    elif today == now.day and 17 <= hour < 22:
        today += 1
        msg = 'Добрый вечер, {}'.format(user_name)
    else:
        today += 1
        msg = 'Доброй ночи, {}'.format(user_name)

    return msg


# Ответ на запрос
def get_answers(user_text):
    countInset = -1
    currentService = []
    for i in MOCK:
        try:
            if i['name'].index(user_text.lower()) != ValueError:
                countInset += 1

        except ValueError:
            continue

        currentService = i['print_docs']
    print(countInset)
    if countInset > 1:
        return 'Найдено {} варианта, уточните вопрос'.format(countInset)
    elif countInset == -1:
        return 'Ничего не найдено. Уточните запрос'
    else:
        return 'Вам необходимо собрать следующие документы: \n\n{}'.format('\n\n- '.join(currentService))


# Основная функция
def main():
    new_offset = None

    while True:
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()

        if len(last_update) > 0:
            last_update_id = last_update['update_id']
            user_text = last_update['message']['text']
            chat_id = last_update['message']['chat']['id']
            user_name = last_update['message']['chat']['first_name']

            if user_text == '/start':
                greet_bot.send_message(chat_id, get_hello(user_name))
            else:
                greet_bot.send_message(chat_id, get_answers(user_text))

            new_offset = last_update_id + 1


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
