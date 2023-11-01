import requests
from bs4 import BeautifulSoup
import re
from googletrans import Translator
from const import PARAM_ORIGINAL_PREFIX, PARAM_TRANSLATION_PREFIX, PARAM_LANG, PARAM_LIMIT
from utils import Utils

class TextUtils:
    @staticmethod
    def get_all_text_from_page(url: str) -> str:
        """ Получить весь текст со странички """
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        return text

    @staticmethod
    def get_unique_words_and_count(text: str, cmd_params: dict) -> list:
        """ Получить словарь [слово: количество вхождений] """
        separate_words = re.findall(r'\b[а-яА-Яa-zA-Z]+\b', text)
        print('Всего на странице найдено слов: {}'.format(len(separate_words)))
        unique_words_dict = {}
        for word in separate_words:
            transformed_word = word.lower()
            unique_words_dict[transformed_word] = unique_words_dict.get(transformed_word, 0) + 1

        unique_words_dict = sorted(unique_words_dict.items(), key=lambda item: item[1], reverse=True)
        print('Уникальных слов: {}'.format(len(unique_words_dict)))
        if cmd_params[PARAM_LIMIT] and cmd_params[PARAM_LIMIT] <= len(unique_words_dict):
            print('Установлено ограничение! Будут переведены {} наиболее часто употребляющихся'
                  .format(cmd_params[PARAM_LIMIT]))
            unique_words_dict = list(unique_words_dict)[:cmd_params[PARAM_LIMIT]]
        print('Топ {} наиболее часто употребляющихся слов:'.format(10
                                                                   if cmd_params[PARAM_LIMIT] == 0 or cmd_params[PARAM_LIMIT] > 10
                                                                   else cmd_params[PARAM_LIMIT]))
        for word in unique_words_dict[:10]:
            print('{} ({})'.format(word[0], word[1]))

        return unique_words_dict

    @staticmethod
    def get_word_and_translation(words: list, cmd_params: dict) -> list:
        """ Получить список [{Оригинал: str, Перевод: str}] """
        translator = Translator()
        result = []
        for word_id, (word, _) in enumerate(words, start=1):
            translation = translator.translate(word, dest=cmd_params[PARAM_LANG])
            Utils.show_progress(word_id, len(words))
            result.append({
                    cmd_params[PARAM_ORIGINAL_PREFIX]: word,
                    cmd_params[PARAM_TRANSLATION_PREFIX]: translation.text
                })
        return result
