# -*- coding: utf-8 -*-
import json


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    print('Введите ПОЛНЫЙ путь к файлу')
    filepath = input()
    pretty_print_json(load_data(filepath))
