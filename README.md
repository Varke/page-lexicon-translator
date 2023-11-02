# page-lexicon-translator
PageLexiconTranslator — программа, которая ищет все уникальные слова по указанному URL-адресу, сортирует их в порядке убывания частоты встречаемости и предоставляет их переводы. Результат работы записывается в файл.

## Как пользоваться
1. Установить библиотеки, необходимые для работы программы `pip install -r requirements.txt`
2. Запустить через консоль `py main.py`, указывая необходимые параметры. Пример: `py main.py --url=https://py-googletrans.readthedocs.io/en/latest/# --limit 20`

## Параметры командной строки
- **-h, --help** Посмотреть справку
- **--url URL** Ссылка на страницу, с которой брать текст
- **--lang [LANG]** Язык, на котором будет перевод (сокращение локали, по-умолчанию "ru")
- **--limit [LIMIT]** Ограничение на количество слов. Если задано, будут выведены N наиболее часто встречающихся. По-умолчанию отсутствует
- **--o_prefix [O_PREFIX]** Название столбца с оригинальными словами (по-умолчанию "Оригинал")
- **--t_prefix [T_PREFIX]** Название столбца с переводом (по-умолчанию "Перевод")
- **--min_len [MIN_LEN]** Минимальная длина слова (по-умолчанию 0)
