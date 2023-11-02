import argparse
from const import PARAM_URL, PARAM_LANG, PARAM_LIMIT, PARAM_ORIGINAL_PREFIX, PARAM_TRANSLATION_PREFIX, PARAM_MIN_LEN


class CMDUtils:
    def __init__(self):
        self.params = self.parse_arguments()

    def parse_arguments(self) -> dict:
        parser = argparse.ArgumentParser(description='Программа ищет все уникальные слова по указанному URL-адресу,'
                                                     ' сортирует их в порядке убывания частоты встречаемости'
                                                     ' и предоставляет их переводы.'
                                                     ' Результат работы записывается в файл.',
                                         epilog='Добриков Алексей, 2023')

        # Определение именованных аргументов
        parser.add_argument(PARAM_URL,
                            type=str,
                            help='Ссылка на страницу, с которой брать текст')
        parser.add_argument(PARAM_LANG,
                            type=str,
                            help='Язык, на котором будет перевод (сокращение локали, по-умолчанию "ru")',
                            nargs='?',
                            default='ru')
        parser.add_argument(PARAM_LIMIT,
                            type=int,
                            help='Ограничение на количество слов. Если задано, будут выведены N наиболее'
                                 ' часто встречающихся. По-умолчанию отсутствует',
                            nargs='?',
                            default=0)
        parser.add_argument(PARAM_ORIGINAL_PREFIX,
                            type=str,
                            help='Название столбца с оригинальными словами (по-умолчанию "Оригинал")',
                            nargs='?',
                            default='Оригинал')
        parser.add_argument(PARAM_TRANSLATION_PREFIX,
                            type=str,
                            help='Название столбца с переводом (по-умолчанию "Перевод")',
                            nargs='?',
                            default='Перевод')
        parser.add_argument(PARAM_MIN_LEN,
                            type=int,
                            help='Минимальная длина слова (по-умолчанию 0 символов)',
                            nargs='?',
                            default=0)
        # Парсинг аргументов
        args = parser.parse_args()

        # Заполняем параметры
        params = {
            PARAM_URL: args.url if args.url else self.input_field('ссылку на страницу'),
            PARAM_LANG: args.lang,
            PARAM_LIMIT: args.limit,
            PARAM_ORIGINAL_PREFIX: args.o_prefix,
            PARAM_TRANSLATION_PREFIX: args.t_prefix,
            PARAM_MIN_LEN: args.min_len
        }
        return params

    @staticmethod
    def input_field(field_name: str):
        """Ввести с консоли обязательное поле"""
        return input('Введите, пожалуйста, ' + field_name + ': ')
