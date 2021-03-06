# Обрезка ссылок с помощью Битли

Данные скрипт сокращает введённую ссылку, делая из них битлинк. Если ввести
билтинк, то скрипт покажет количество переходов по этому битлинку.

## Запуск

Скачайте код.

Создайте виртуальное окружение:

```
python3 -m venv venv
```

Активируйте виртуальное окружение:

- для Windows:
    ```
    venv\Scripts\activate 
    ```
- для Linux:
    ```
    source venv/bin/activate 
    ```

Установите зависимости командой:

```
pip install -r requirements.txt
```

Чтобы запустить скрипт, введите в терминале:

```
python main.py 'требуемый url'
```

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить,
создайте файл `.env` в корне проекта и запишите туда данные в таком
формате: `ПЕРЕМЕННАЯ=значение`.

Доступны следующие переменные:

- `BITLY_TOKEN` — токен, который необходим для авторизации на сервисе
  [bitly.com](https://app.bitly.com) с помощью OAuth 2

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для
веб-разработчиков [dvmn.org](https://dvmn.org/).