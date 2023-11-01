import argparse
from const import PARAM_URL, PARAM_LANG, PARAM_LIMIT


class CMDUtils:
    def __init__(self):
        parser = argparse.ArgumentParser()

        # Определение именованных аргументов
        parser.add_argument(PARAM_URL,
                            type=str,
                            help='Ссылка на страницу, с которой брать текст')
        parser.add_argument(PARAM_LANG,
                            type=str,
                            help='Язык, на котором будет перевод (сокращение локали, по-умолчанию "ru")')
        parser.add_argument(PARAM_LIMIT,
                            type=int,
                            help='Ограничение на количество слов. Если задано, будут выведены N наиболее'
                                 'часто встречающихся. По-умолчанию отсутствует')
        # Парсинг аргументов
        args = parser.parse_args()

        # Заполняем параметры
        self.params = {
            PARAM_URL: args.url if args.url else self.input_field('ссылку на страницу'),
            PARAM_LANG: args.lang if args.lang else 'ru',
            PARAM_LIMIT: args.limit if args.limit else 0
        }

    @staticmethod
    def input_field(field_name: str):
        return input('Введите, пожалуйста, ' + field_name + ': ')