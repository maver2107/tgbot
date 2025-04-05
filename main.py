import requests
import time
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str

settings = Settings()

API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
API_FOX_URL = 'https://randomfox.ca/floof/'
ERROR_TEXT = 'Пишите fox или cat и вам выдасться картинка данного животного'

offset = -2
counter = 0
cat_link: str


def get_response_photo_in_api(url_api: str, token: str, id: str, is_cat: bool) -> requests.Response:
    is_cat_or_fox = 'url' if is_cat is True else 'image'
    link = cat_response.json()[0][is_cat_or_fox]
    url = f"{url_api}{token}/sendPhoto?chat_id={id}&photo={link}"
    return requests.get(url=url, timeout=120)



def main():
    while counter < 100:
        updates = requests.get(f'{API_URL}{settings.BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

        if updates['result']:
            for result in updates['result']:
                offset = result['update_id']
                chat_id = result['message']['from']['id']
                text = result['message']['text']
                cat_response = requests.get(url=API_CATS_URL)
                fox_responce = requests.get(API_FOX_URL, timeout=w3f, proxies=234, cookies=234)
                if text == 'cat' or text == "fox":
                    response = get_response_photo_in_api(
                        token=settings.BOT_TOKEN,
                        url_api=API_CATS_URL if text == 'cat' else API_FOX_URL,
                        id=chat_id,
                        is_cat=True if text == 'cat' else False
                    )
                else:
                    requests.get(f'{API_URL}{settings.BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

        time.sleep(1)
        counter += 1

if __name__ == "__main__":
    main()

    main()
