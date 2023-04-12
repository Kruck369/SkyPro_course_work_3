import json
import os
from datetime import datetime
from operator import itemgetter

n = os.path.abspath('../SkyPro_course_work_3')


def get_operations():
    """получает информацию из файла"""
    with open(os.path.join(n, 'operations.json'), 'r', encoding='utf-8') as file:
        return json.load(file)


def get_date(i, operations):
    """получает дату, форматирует в нужный формат"""
    operation_date = datetime.strptime(operations[i]['date'], "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = operation_date.strftime('%d.%m.%Y')
    return formatted_date


def get_description(i, operations):
    """получает описание транзакции"""
    description = operations[i]['description']
    return description


def get_where_from(i, operations):
    """получает информацию откуда транзакция, форматирует в нужный формат"""
    try:
        where_from = operations[i]['from'].split()
        if where_from[0] == "Счет":
            where_from_numbers = where_from[1]
            where_from_hidden = "**" + where_from_numbers[-4:]
            return f"{where_from[0]} {where_from_hidden}"
        elif len(where_from) < 3:
            where_from_numbers = ' '.join([where_from[1][i:i + 4] for i in range(0, len(where_from[1]), 4)])
            where_from_hidden = where_from_numbers[:7] + "** ****" + where_from_numbers[14:]
            return f"{where_from[0]} {where_from_hidden}"
        else:
            where_from_numbers = ' '.join([where_from[-1][i:i + 4] for i in range(0, len(where_from[-1]), 4)])
            where_from_hidden = where_from_numbers[:7] + "** ****" + where_from_numbers[14:]
            return f"{' '.join(where_from[0:len(where_from)-1])} {where_from_hidden}"
    except KeyError:
        return "Отсутствует"


def get_where_to(i, operations):
    """получает информацию куда транзакция, форматирует в нужный формат"""
    try:
        where_to = operations[i]['to'].split()
        if where_to[0] == "Счет":
            where_to_numbers = where_to[1]
            where_to_hidden = "**" + where_to_numbers[-4:]
            return f"{where_to[0]} {where_to_hidden}"
        elif len(where_to) < 3:
            where_to_numbers = ' '.join([where_to[1][i:i + 4] for i in range(0, len(where_to[1]), 4)])
            where_to_hidden = where_to_numbers[:7] + "** ****" + where_to_numbers[14:]
            return f"{where_to[0]} {where_to_hidden}"
        else:
            where_to_numbers = ' '.join([where_to[-1][i:i + 4] for i in range(0, len(where_to[-1]), 4)])
            where_to_hidden = where_to_numbers[:7] + "** ****" + where_to_numbers[14:]
            return f"{' '.join(where_to[0:len(where_to)-1])} {where_to_hidden}"
    except KeyError:
        return "Отсутствует"


def get_summ(i, operations):
    """получает информацию о сумме транзакции"""
    try:
        return operations[i]['operationAmount']['amount']
    except KeyError:
        return "Отсутствует"


def get_currency(i, operations):
    """получает информацию о валюте транзакции"""
    try:
        return operations[i]['operationAmount']['currency']['name']
    except KeyError:
        return "Отсутствует"


def get_status(i, operations):
    """получает информацию о статусе транзакции"""
    try:
        return operations[i]['state']
    except KeyError:
        return "Отсутствует"
