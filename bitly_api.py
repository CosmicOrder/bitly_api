import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv
from requests import HTTPError

load_dotenv()


class BitlyAPI:
    HEADERS = {
        "Authorization": f"Bearer {os.getenv('TOKEN')}"
    }

    def is_bitlink(self, url):
        netloc_path = urlparse(url).netloc + urlparse(url).path
        endpoint = f'https://api-ssl.bitly.com/v4/bitlinks/{netloc_path}'

        response = requests.get(endpoint, headers=self.HEADERS)
        if response.ok:
            return self.count_clicks(netloc_path)
        else:
            return self.shorten_link(netloc_path)

    def shorten_link(self, url):
        endpoint = 'https://api-ssl.bitly.com/v4/shorten'
        payload = {"long_url": f"http://{url}"}

        try:
            response = requests.post(endpoint, json=payload,
                                     headers=self.HEADERS)
            response.raise_for_status()
            bitlink = response.json()["link"]
            return f'Битлинк: {bitlink}'
        except HTTPError:
            return 'Проверьте правильность написания ссылки'

    def count_clicks(self, bitlink):
        endpoint = f'https://api-ssl.bitly.com/v4/bitlinks/' \
                   f'{bitlink}/clicks/summary'

        try:
            response = requests.get(endpoint, headers=self.HEADERS)
            response.raise_for_status()
            clicks_count = response.json()['total_clicks']
            return f'По вашей ссылке прошли {clicks_count} раз(а)'
        except HTTPError:
            return 'Проверьте правильность написания битлинка'
