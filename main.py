# Импортируем нужные функции и классы
from operator import itemgetter

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

# Убираем пустые словари из списка словарей
operations_list = []
for i in range(0, len(get_operations())):
    if get_operations()[i] == {}:
        continue
    else:
        operations_list.append(get_operations()[i])

# Сортируем список по убыванию по дате транзакции
operations_list_sorted = sorted(operations_list, key=itemgetter('date'), reverse=True)

operations_objects = []

# Создаем список объектов транзацкий с нужными параметрами
for i in range(len(operations_list_sorted)):
    date = get_date(i, operations_list_sorted)
    description = get_description(i, operations_list_sorted)
    where_from = get_where_from(i, operations_list_sorted)
    where_to = get_where_to(i, operations_list_sorted)
    summ = get_summ(i, operations_list_sorted)
    currency = get_currency(i, operations_list_sorted)
    status = get_status(i, operations_list_sorted)
    operation_i = Operation(date, description, where_from, where_to, summ, currency, status)
    operations_objects.append(operation_i)

# Выводим на экран последние 5 успешных транзакций
for i in range(0, 6):
    operation = operations_objects[i]
    if operation.status != "EXECUTED":
        continue
    else:
        print(operation.build_output())
