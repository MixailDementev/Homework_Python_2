# 2 — Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами
import random
from random import choices, randint
from re import findall
import string
import os


# task_1
def fill_file(filename, num_rows):
    with open(filename, "a", encoding="utf-8") as file:
        for i in range(num_rows):
            num = random.randint(-1000, 1001)
            float_num = random.uniform(-1, 1)
            file.write(f"{num}|{float_num}\n")


# task_2
start, end = 4, 7


def task_2(file_name, line_num):
    count = 0
    with open(file_name, "w", encoding="utf-8") as f:
        while count < line_num:
            name = "".join(
                random.sample(string.ascii_lowercase, random.randint(start, end))
            )
            if len(findall("[aeiouyAEIOUY]", name)) > 0:
                f.write(f"{''.join(name).capitalize()}\n")
                count += 1


# task_3
def unit_files(file_nums, file_names, new_file):
    with (
        open(new_file, "w", encoding="utf-8") as res,
        open(file_nums, "r", encoding="utf-8") as f_1,
        open(file_names, "r", encoding="utf-8") as f_2,
    ):
        lst_prod = [int(line.split("|")[0]) * float(line.split("|")[1]) for line in f_1]
        for num, line_2 in zip(lst_prod, f_2):
            if num < 0:
                res.write(f"{line_2.lower().strip()}|{abs(num)}\n")
            else:
                res.write(f"{str(line_2).upper().strip()}|{int(num)}\n")


# task_4
def gen_file(ext, min_name_len=6, max_name_len=30, count=2):
    folder_name = "new_dir"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    for i in range(count):
        file_name = "".join(
            choices(string.ascii_lowercase, k=randint(min_name_len, max_name_len))
        )
        with open(f"{folder_name}/{file_name}.{ext}", "wb") as f:
            f.write(os.urandom(randint(min_name_len, max_name_len)))


# task_5
def create_files_updated(**kwargs):
    for k, v in kwargs.items():
        gen_file(ext=k, count=v)


# task_7
def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f"{folder_path}\\{folder}"):
            os.mkdir(f"{folder_path}\\{folder}")


def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    return subfolder_paths


def get_file_paths(folder_path) -> list:
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]

    return file_paths


def sort_files(folder_path):
    file_paths = get_file_paths(folder_path)
    ext_list = list(extensions.items())

    for file_path in file_paths:
        extension = file_path.split(".")[-1]
        file_name = file_path.split("\\")[-1]

        for dict_key_int in range(len(ext_list)):
            if extension in ext_list[dict_key_int][1]:
                print(f"Moving {file_name} in {ext_list[dict_key_int][0]} folder\n")
                os.rename(
                    file_path, f"{main_path}\\{ext_list[dict_key_int][0]}\\{file_name}"
                )


def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)

    for p in subfolder_paths:
        if not os.listdir(p):
            print("Deleting empty folder:", p.split("\\")[-1], "\n")
            os.rmdir(p)
