# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
import logging
from collections import namedtuple

FORMAT = "{asctime} - {levelname}: {msg}"
logging.basicConfig(
    filename="log.txt", filemode="w", format=FORMAT, style="{", level=logging.NOTSET
)
logger = logging.getLogger()

FileSystemObject = namedtuple(
    "FileSystemObject", ["name", "extension", "is_directory", "parent_directory"]
)


def get_directory_content(dir_path):
    try:
        items = os.listdir(dir_path)
        for item in items:
            item_path = os.path.join(dir_path, item)
            name, extension = os.path.splitext(item)
            is_directory = os.path.isdir(item_path)
            parent_directory = os.path.basename(dir_path)

            fs_object = FileSystemObject(
                name, extension, is_directory, parent_directory
            )
            logger.info(fs_object)
            if is_directory:
                get_directory_content(item_path)
    except OSError as e:
        logger.error(f"Error accessing directory: {e}")


dir_path = input("Введите путь до директории: ")

if not os.path.isdir(dir_path):
    print("Указанный путь не является директорией.")
else:
    get_directory_content(dir_path)
    print("Информация сохранена в log.txt")
