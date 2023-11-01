from text_utils import TextUtils


if __name__ == '__main__':
    url = 'https://en.wikipedia.org/wiki/Australentulus_orientalis'
    page_text = TextUtils.get_all_text_from_page(url)
    words = TextUtils.get_unique_words_and_count(page_text)
    print(words)
    tr = TextUtils.get_word_and_translation(words)
    print(tr)
