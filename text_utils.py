import requests
from bs4 import BeautifulSoup
import re
from googletrans import Translator


class TextUtils:
    @staticmethod
    def get_all_text_from_page(url: str) -> str:
        """ Получить весь текст со странички """
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        return text

    @staticmethod
    def get_unique_words_and_count(text: str) -> dict:
        """ Получить словарь [слово: количество вхождений] """
        separate_words = re.findall(r'\b[а-яА-Яa-zA-Z]+\b', text)
        unique_words_dict = {}
        for word in separate_words:
            transformed_word = word.lower()
            unique_words_dict[transformed_word] = unique_words_dict.get(transformed_word, 0) + 1
        return unique_words_dict

    @staticmethod
    def get_word_and_translation(words: dict, destination_lang: str = 'ru') -> dict:
        """ Получить словарь [слово: перевод] """
        translator = Translator()
        result = {}
        for word in words.keys():
            translation = translator.translate(word, dest=destination_lang)
            result[word] = translation.text
        return result
