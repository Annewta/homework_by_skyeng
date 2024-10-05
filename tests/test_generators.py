from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator
def test_empty_list(empty_transactions):
    #Проверка пустово списка
    result = list(filter_by_currency(empty_transactions, 'USD'))
    assert  result == ['Список транзакций пуст']

def test_with_transaction(transactions_with_usd):
    #Проверка работы функции
    result_list = []
    while test_with_transaction:
        result = filter_by_currency(transactions_with_usd, 'USD')
        result_list.append(result)
    assert result_list == [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {'amount': '9824.07', 'currency': 'USD'}, 'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}, {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': 'USD'}}]

def test_without_transaction(transactions_without_usd):
    #Проверка отработки условия отсутсвия данных с нужной валютой
    currency = 'USD'
    result = list(filter_by_currency(transactions_without_usd, currency))
    assert result == ['Транзакций с такой валютой нет']

def test_one_descriptions(single_descriptions):
    #Проверка работы функции с одним элементом списка
    result = ["Перевод организации"]
    assert list(transaction_descriptions(single_descriptions)) == result

def test_multiple_descriptions(multiple_descriptions):
    #Проверка работы функции с несколькими элементами списка
    result = ['Перевод организации', 'Перевод со счета на счет']
    assert list(transaction_descriptions(multiple_descriptions)) == result

def test_none_descriptions(empty_transactions):
    #Проверка функции на отработку пустого списка
    result = []
    assert list(transaction_descriptions(empty_transactions)) == result

def test_card_number_generator():
    #Проверка правильной работы функции
    generator = list(card_number_generator(1, 5))
    result = ['0000 0000 0000 0001','0000 0000 0000 0002','0000 0000 0000 0003','0000 0000 0000 0004','0000 0000 0000 0005']
    assert result == generator

def test_one_number_generator():
    #Проверка функции на генерацию 1 номера
    result = list(card_number_generator(5, 5))
    expected = ['0000 0000 0000 0005']
    assert result == expected

def test_wrong_number_generator():
    # Проверка неправильного диапозона
    result = list(card_number_generator(5, 4))
    expected = ["Диапазон должен быть от 0000 0000 0000 0001 до 9999 9999 9999 9999"]
    assert result == expected

def test_format_number_generator():
    # Проверка корректности форматирования
    generated_numbers = list(card_number_generator(1,5))
    for number in generated_numbers:
        assert len(number) == 19, f"Номер карты '{number}' имеет неправильную длину"
    generated_numbers_ = list(card_number_generator('d', 'd'))
    for number in generated_numbers_:
        assert number.isalpha(), f"Номер карты '{number}' содержит недопустимые символы"

def test_end_number_generator():
    # Проверка крайних значений
    start = 1
    end = 5
    generated_numbers = list(card_number_generator(start,end))
    assert generated_numbers[0] == f"{start:016d}", "Первый номер карты неверен"
    assert generated_numbers[-1] == f"{end:016d}", "Последний номер карты неверен"

def test_ending_number_generator():
    # Проверка завершения генерации
    generated_numbers = list(card_number_generator(1,5))
    assert len(generated_numbers) == (end - start + 1), "Количество сгенерированных номеров неверно"


