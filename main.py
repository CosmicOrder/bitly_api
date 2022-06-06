from bitly_api import BitlyAPI

if __name__ == '__main__':
    bitly = BitlyAPI()
    print(bitly.is_bitlink(input('Введите ссылку: ')))
