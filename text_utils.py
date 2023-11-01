import requests
from bs4 import BeautifulSoup
import re
from googletrans import Translator
from const import PARAM_ORIGINAL_PREFIX, PARAM_TRANSLATION_PREFIX, PARAM_LANG, PARAM_LIMIT


class TextUtils:
    @staticmethod
    def get_all_text_from_page(url: str) -> str:
        """ Получить весь текст со странички """
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        return text

    @staticmethod
    def get_unique_words_and_count(text: str, cmd_params: dict) -> dict:
        """ Получить словарь [слово: количество вхождений] """
        separate_words = re.findall(r'\b[а-яА-Яa-zA-Z]+\b', text)
        unique_words_dict = {}
        for word in separate_words:
            transformed_word = word.lower()
            unique_words_dict[transformed_word] = unique_words_dict.get(transformed_word, 0) + 1

        if cmd_params[PARAM_LIMIT]:
            unique_words_dict = dict(sorted(unique_words_dict.items(), key=lambda item: item[1], reverse=True))
            unique_words_dict = dict(list(unique_words_dict.items())[:cmd_params[PARAM_LIMIT]])
        print(unique_words_dict)
        return unique_words_dict

    @staticmethod
    def get_word_and_translation(words: dict, cmd_params: dict) -> list:
        """ Получить список [{Оригинал: str, Перевод: str}] """
        translator = Translator()
        result = []
        for word in words.keys():
            translation = translator.translate(word, dest=cmd_params[PARAM_LANG])
            result.append({
                    cmd_params[PARAM_ORIGINAL_PREFIX]: word,
                    cmd_params[PARAM_TRANSLATION_PREFIX]: translation.text
                })
        return result
