# 1 — Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>


import os
import glob

path = "./new_dir"
files = glob.glob(path + "/*")


for i, f in enumerate(files, 1):
    os.rename(
        f, os.path.join(path, "{0:03d}".format(i) + "_new_" + os.path.basename(f))
    )