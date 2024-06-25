import requests  # Импорт библиотеки для выполнения HTTP-запросов
from bs4 import BeautifulSoup  # Импорт библиотеки для парсинга HTML и XML документов
import time  # Импорт библиотеки для работы с временем
import datetime  # Импорт библиотеки для работы с датами и временем
all_news = []  # Инициализация списка для хранения новостей

# Функция для записи лога в файл
def log_to_file(file_name, data):
    with open(file_name, 'a', encoding='utf-8') as file:  # Открытие файла для добавления данных в конец
        file.write(data + '\n')  # Запись данных в файл

# Функция для получения первой новости с веб-страницы
def first_new(url):
    try:
        # Заголовки запроса для имитации запроса от браузера
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Encoding": "*",
            "Connection": "keep-alive"
        }

        response = requests.get(url, headers=headers)  # Выполнение GET-запроса к URL
        response.raise_for_status()  # Проверка на ошибки HTTP
        soup = BeautifulSoup(response.text, 'html.parser')  # Парсинг HTML-кода страницы

        # Найти все элементы 'article' на странице
        articles = soup.find_all('article')
        for article in articles:
            # Добавление заголовка статьи в список новостей, если он найден
            all_news.insert(0, article.find('h3').text.strip()) if article.find('h3') else 'No title'

    # Обработка возможных исключений при запросе
    except requests.HTTPError as http_err:
        error_message = f"HTTP error occurred: {http_err}"  # Сообщение об ошибке HTTP
        print(error_message)
        # log_to_file(log_file, error_message)  # Запись ошибки в лог-файл
    except Exception as err:
        error_message = f"An error occurred: {err}"  # Сообщение о других ошибках
        print(error_message)
        # log_to_file(log_file, error_message)  # Запись ошибки в лог-файл

# Функция для извлечения новостей с ключевыми словами
def fetch_news(url, keywords, log_file):
    try:
        # Аналогичные заголовки запроса, как и в функции first_new
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Encoding": "*",
            "Connection": "keep-alive"
        }

        response = requests.get(url, headers=headers)  # Аналогичный GET-запрос
        response.raise_for_status()  # Аналогичная проверка на ошибки HTTP
        soup = BeautifulSoup(response.text, 'html.parser')  # Аналогичный парсинг HTML

        # Аналогичный поиск элементов 'article'
        articles = soup.find_all('article')
        for article in articles:
            # Извлечение заголовка, аннотации и автора статьи, если они найдены
            title = article.find('h3').text.strip() if article.find('h3') else 'No title'
            summary = article.find('p').text.strip() if article.find('p') else 'No summary'
            authors = article.find('span').text.strip() if article.find('span') else 'No Author'

            # Проверка наличия ключевых слов в тексте статьи и отсутствие заголовка в списке новостей
            if any(keyword in article.text for keyword in keywords) and not any(title in new for new in all_news):
                log_entry = f"Заголовок: {title}\nАннотация: {summary}\nАвтор: {authors}\n"  # Формирование записи для лога
                print(log_entry)
                all_news.insert(0, title)  # Добавление заголовка в список новостей
                # log_to_file(log_file, log_entry)  # Запись в лог-файл

    # Аналогичная обработка исключений, как и в функции first_new
    except requests.HTTPError as http_err:
        error_message = f"HTTP error occurred: {http_err}"
        print(error_message)
        # log_to_file(log_file, error_message)
    except Exception as err:
        error_message = f"An error occurred: {err}"
        print(error_message)
        # log_to_file(log_file, error_message)

# URL новостного агентства и ключевые слова для поиска
news_url = 'https://www.nytimes.com/international/section/world'
keywords = ['Russia','U.S.','Israeli','Ukraine','China','Germany']
log_file_name = 'news_log.txt'  # Имя файла лога
first_new(news_url)  # Вызов функции для получения первой новости

# Запуск скрипта на 4 часа
end_time = datetime.datetime.now() + datetime.timedelta(hours=4)  # Установка времени окончания работы скрипта
while datetime.datetime.now() < end_time:  # Цикл до достижения времени окончания
    fetch_news(news_url, keywords, log_file_name)  # Вызов функции для извлечения новостей
    time.sleep(120)  # Пауза на 2 минуты
