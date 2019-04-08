import json
import requests
import user_date
from bbs_news import get_news

token_telegram = user_date.user_token
URL_TELEGRAM = 'http://api.telegram.org/bot' + token_telegram + '/'

global last_update_id
last_update_id = 0

def get_updates():
    url = URL_TELEGRAM + 'getupdates'
    answer = requests.get(url)
    return answer.json()

def get_message():
    date = get_updates()

    last_object = date['result'][-1]
    current_update_id = last_object['update_id']
    print(current_update_id)

    global last_update_id

    if last_update_id != current_update_id:

        last_update_id = current_update_id
        main_part_json = date['result'][-1]['message']
        chat_id = main_part_json['chat']['id']
        text_message = main_part_json['text']

        message = {'chat_id': chat_id,
                   'text': text_message}

        return message
    return None

def send_message(chat_id, text='Wait...'):
    url = URL_TELEGRAM + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():

    d = get_updates()
    with open('upd.json', 'w') as file:
        json.dump(d, file, indent=2, ensure_ascii=False)

    while True:
        answer = get_message()

        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']

            if text == '/btc':
                for i in get_news():
                    send_message(chat_id, i)
                    if len(get_news()) == 9:
                        break
                else:
                    continue
        else:
            continue

if __name__ == '__main__':
    main()
