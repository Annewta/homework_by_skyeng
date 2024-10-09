from src.processing import filter_by_state
from src.processing import sort_by_date
import pytest

def test_filter_by_state_1(fix_filter_by_state):
    '''Тестирование фильтрации списка словарей по заданному статусу state'''
    result = filter_by_state(fix_filter_by_state, 'EXECUTED')
    assert result == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]

def test_filter_by_state_emty(fix_filter_by_state_emty):
    '''Проверка работы функции при отсутствии словарей с указанным
    статусом state в списке'''
    result = filter_by_state(fix_filter_by_state_emty, 'EXECUTED')
    assert result == ['Список пуст']

@pytest.mark.parametrize('result, state', [
    ([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}], 'EXECUTED'),
    ([{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], 'CANCELED',)])
def test_filter_by_state_parm(result, state):
    '''Параметризация тестов для различных возможных значений статуса state'''
    assert filter_by_state(result, state)


def test_sort_by_date_1(fix_sort_by_date):
    '''Тестирование сортировки списка словарей по датам
    в порядке убывания и возрастания'''
    result = sort_by_date(fix_sort_by_date, True)
    assert result == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

def test_sort_by_date_equal(fix_sort_by_date_equal):
    '''Проверка корректности сортировки при одинаковых датах'''
    result = sort_by_date(fix_sort_by_date_equal, True)
    assert result == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},{'id': 615064591, 'state': 'CANCELED', 'date': '2018-09-12T08:21:33.419441'},{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_sort_by_date_format(fix_sort_by_date_format):
    '''Тесты на работу функции с некорректными
    или нестандартными форматами дат'''
    result = sort_by_date(fix_sort_by_date_format)
    assert result == [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},{'id': 939719570, 'state': 'EXECUTED', 'date': '2018/06/30T02:08:58.425572'},{'id': 615064591, 'state': 'CANCELED', 'date': '12.10.2018'},{'id': 594226727, 'state': 'CANCELED', 'date': '12.09.2018T21:27:25.241689'}]

def test_sort_by_date_format(fix_sort_by_date):
    '''Тесты на работу функции c обратной сортировкой'''
    result = sort_by_date(fix_sort_by_date, False)
    assert result == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]