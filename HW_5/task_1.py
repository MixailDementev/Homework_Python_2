# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

def split_file_path(file_path):
    path, filename = os.path.split(file_path)
    name, extension = os.path.splitext(filename)
    extension = extension[1:]
    return path, name, extension


file_path = r"C:\games\World_of_Tanks_RU\mods\1.21.0.0\readme.txt"
print(split_file_path(file_path))





