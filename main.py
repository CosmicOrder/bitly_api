import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv
from requests import HTTPError


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Ссылка')

    return parser


def is_bitlink(link, header):
    endpoint = f'https://api-ssl.bitly.com/v4/bitlinks/{link}'

    response = requests.get(endpoint, headers=header)
    return response.ok


def shorten_link(link, header):
    endpoint = 'https://api-ssl.bitly.com/v4/shorten'
    payload = {"long_url": f"http://{link}"}

    response = requests.post(endpoint, json=payload,
                             headers=header)
    response.raise_for_status()
    bitlink = response.json()["link"]
    return f'Битлинк: {bitlink}'


def count_clicks(bitlink, header):
    endpoint = f'https://api-ssl.bitly.com/v4/bitlinks/' \
               f'{bitlink}/clicks/summary'

    response = requests.get(endpoint, headers=header)
    response.raise_for_status()
    clicks_count = response.json()['total_clicks']
    return f'По вашей ссылке прошли {clicks_count} раз(а)'


if __name__ == '__main__':
    load_dotenv()

    token = os.getenv('BITLY_TOKEN')
    header = {
        "Authorization": f"Bearer {token}"
    }

    parser = create_parser()
    args = parser.parse_args()

    url = args.url.strip()
    scheme, *no_scheme_url = urlparse(url)
    no_scheme_url = ''.join(no_scheme_url)

    try:
        if is_bitlink(no_scheme_url, header):
            print(count_clicks(no_scheme_url, header))
        else:
            print(shorten_link(no_scheme_url, header))
    except HTTPError:
        print('Проверьте правильность написания ссылки')
