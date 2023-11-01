import csv
from const import PARAM_ORIGINAL_PREFIX, PARAM_TRANSLATION_PREFIX
import sys

class Utils:
    @staticmethod
    def write_to_file(data: list, url: str, params: dict) -> None:
        if data is None or len(data) == 0:
            return

        file_name = (url.replace("http://", "")
                     .replace("https://", "")
                     .replace("/", "_"))
        file_name += '.csv'

        # Запись в файл CSV
        with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
            fieldnames = [params[PARAM_ORIGINAL_PREFIX], params[PARAM_TRANSLATION_PREFIX]]
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            # Запись заголовка (имен полей)
            csv_writer.writeheader()
            # Запись данных из словаря в файл CSV
            csv_writer.writerows(data)

        print(f"Данные были успешно записаны в файл '{file_name}'")

    @staticmethod
    def show_progress(current: int, maximum: int) -> None:
        progress = current / maximum * 100
        sys.stdout.write(
            "\rПрогресс выполнения: [{:<50}] {:.0f}% (переведено {} из {})"
            .format("━" * int((current / maximum) * 50), progress, current, maximum))
        sys.stdout.flush()
        if current == maximum:
            print('\n')
