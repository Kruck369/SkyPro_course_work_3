import json
import os
from utils.operations import (
    get_operations,
    get_summ,
    get_currency,
    get_date,
    get_description,
    get_where_from,
    get_where_to,
    get_status
)
from utils.operation import Operation

operations = get_operations()


def test_get_summ():
    assert get_summ(0, operations) == "31957.58"
    assert get_summ(5, {}) == "Отсутствует"


def test_get_currency():
    assert get_currency(1, operations) == "USD"
    assert get_currency(1, {}) == "Отсутствует"


def test_get_date():
    assert get_date(2, operations) == "30.06.2018"


def test_get_description():
    assert get_description(2, operations) == "Перевод организации"


def test_get_where_from():
    assert get_where_from(2, operations) == "Счет **6952"
    assert get_where_from(8, operations) == "Visa Classic 6831 98** **** 7658"
    assert get_where_from(0, operations) == "Maestro 1596 83** **** 5199"
    assert get_where_from(0, {}) == "Отсутствует"


def test_get_where_to():
    assert get_where_to(2, operations) == "Счет **6702"
    assert get_where_to(8, operations) == "Visa Platinum 8990 92** **** 5229"
    assert get_where_to(20, operations) == "Maestro 3806 65** **** 3662"
    assert get_where_to(0, {}) == "Отсутствует"


def test_get_status():
    assert get_status(0, operations) == "EXECUTED"
    assert get_status(13, operations) == "CANCELED"
    assert get_status(0, {}) == "Отсутствует"


def test_operation():
    operation = Operation("26.08.2019", "Перевод организации", "Maestro 1596837868705199", "Счет 64686473678894779589", "31957.58", "руб.", "EXECUTED")
    assert operation.date == "26.08.2019"
    assert operation.status == "EXECUTED"
    assert operation.summ == "31957.58"
    assert operation.where_from == "Maestro 1596837868705199"
    assert operation.where_to == "Счет 64686473678894779589"
    assert operation.description == "Перевод организации"
    assert operation.currency == "руб."
    assert operation.build_output() == "26.08.2019 Перевод организации\nMaestro 1596837868705199 -> Счет 64686473678894779589\n31957.58 руб.\n"
