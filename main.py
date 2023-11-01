from text_utils import TextUtils
from cmd_utils import CMDUtils
from utils import Utils
from const import PARAM_URL


def main():
    cmd_utils = CMDUtils()
    url = cmd_utils.params[PARAM_URL]
    page_text = TextUtils.get_all_text_from_page(url)
    words = TextUtils.get_unique_words_and_count(page_text, cmd_utils.params)
    translations = TextUtils.get_word_and_translation(words, cmd_utils.params)
    Utils.write_to_file(translations, url, cmd_utils.params)


if __name__ == '__main__':
    main()
