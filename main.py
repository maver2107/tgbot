import requests
import time
from tokenbot import BOT_TOKEN


API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
API_FOX_URL = 'https://randomfox.ca/floof/'
ERROR_TEXT = 'Пишите fox или cat и вам выдасться картинка данного животного'

offset = -2
counter = 0
cat_response: requests.Response
fox_responce: requests.Response
cat_link: str


while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            text = result['message']['text']
            cat_response = requests.get(API_CATS_URL)
            fox_responce = requests.get(API_FOX_URL)
            if text == 'cat':
                if cat_response.status_code == 200:
                    cat_link = cat_response.json()[0]['url']
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            elif text == 'fox':
                if fox_responce.status_code == 200:
                    fox_link = fox_responce.json()['image']
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={fox_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1
