import json
from string import ascii_lowercase, digits

import random

import time

import os
from dotenv import load_dotenv
from pathlib import Path


def get_creds(file='.env'):
    # повертає дані з .env файлу
    dotenv_path = Path(file)
    load_dotenv()

    return os.environ.get('LOGIN'), os.environ.get('PASSWORD')


def random_string(n=10):
    # створює та повертає символьну строку з маленьких символів та чисел
    num_list = []
    while len(num_list) < n:
        num_list.append(random.choice(list(ascii_lowercase+digits)))
    return ''.join(num_list)


def json_to_file(jstring, filename, mode="x+"):
    """
    Пише json у вигляді стрічки у файл
    :param jstring:
    :return: нічого
    """
    with open(filename, mode) as outfile:
        json.dump(jstring, outfile)


def read_from_json(filename):
    """
    Відкриває файл зазначений файл
    :param filename:
    :return: повертає словник даних
    """
    # return dict
    filename = f'{return_abspath_from_file(filename)}'
    with open(filename) as json_file:
        j_data = json_file.read()
    return json.loads(j_data)


def read_from_txt(filename):
    filename = f'{return_abspath_from_file(filename)}'
    with open(filename, encoding="utf-8") as infile:
        return infile.readlines()


def calc_symbol_in_strint(income_string: str, symbol="letter"):
    """
    :param income_string: строка яка буде піддаватися прорахунку
    :param symbol: "letter" якщо рахуем символи, "number" якщо рахуем десяткові числа
    :return: повертає кількість символів чи чисел з строки
    """
    lst = list(income_string)
    count = 0
    if symbol == "letter":
        for item in lst:
            if item.isalpha():
                count += 1
    elif symbol == "number":
        for item in lst:
            if item.isdigit():
                count += 1
    else:
        print("ПОМИЛКА!!! Невизначений символ")
    return count


def return_char_with_delay(string):
    # повертає символ з затримкою від 0 до 1 сек
    delay = random.randrange(0, 1)
    time.sleep(delay)
    return string


def fill_input_with_delay(word, locator):
    # заповнення поля для вводу за допомогою функції return_char_with_delay
    l = list(word)
    for i in range(len(l)):
        locator.send_keys(return_char_with_delay(l[i]))


def delete_file(file):
    #  видаляє файл по обсолютному шляху
    path = return_abspath_from_file(file)
    try:
        os.remove(path)
        print(f"File {path} is deleted")
    except Exception as _ex:
        print(f"\nERROR!!!{'='*50}")
        print(_ex)


def return_abspath_from_file(file):
    # повертає абсолютний шлях файлу
    # якщо такого файлу не існує, то створює його
    file_abs_path = os.path.abspath(file)
    if os.path.exists(file_abs_path):
        return os.path.abspath(file)
    else:
        with open(file_abs_path, "x") as new_file:
            pass
        return os.path.abspath(file)


if __name__ == '__main__':
    s = random_string(10)
    print(s)

    d = {
        'one': 1,
        'two': 2,
        'three': 3
    }

    # json_to_file(d)
    print(f"{50 * '='}")

