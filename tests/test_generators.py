from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator
def test_empty_list(empty_transactions):
    assert filter_by_currency(empty_transactions, 'USD') == 'Список транзакция пуст'

def test_with_transaction(transactions_with_usd):
    result = [{
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": "USD"
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": "USD"
            }
        }
    ]
    assert filter_by_currency(transactions_with_usd, 'USD') == result

def test_without_transaction(transactions_without_usd):
    currency = 'USD'
    result == ValueError ('Транзакции с такой валютой нет')
    assert filter_by_currency(transactions_without_usd, currency) == result

def test_one_descriptions(single_descriptions):
    result = ["Перевод организации"]
    assert list(transaction_descriptions(single_descriptions)) == result

def test_multiple_descriptions(multiple_descriptions):
    result = ['Перевод организации', 'Перевод со счета на счет']
    assert list(transaction_descriptions(multiple_descriptions)) == result

def test_none_descriptions(empty_transactions):
    result = []
    assert list(transaction_descriptions(empty_transactions)) == result

def test_card_number_generator(setup_card_number_generator):
    start, end = setup_card_number_generator()
    generator = list(card_number_generator(start, end))
    result = ['0000 0000 0000 0001','0000 0000 0000 0002','0000 0000 0000 0003','0000 0000 0000 0004','0000 0000 0000 0005']
    assert result == generator

def test_one_number_generator(setup_card_number_generator):
    generator = card_number_generator(5, 5)
    result = list(generator)
    expected = ['0000000000000000005']
    assert result == expected

def test_wrong_number_generator(setup_card_number_generator):
    # Проверка неправильного диапозона
    generator = card_number_generator(5, 4)
    result = list(generator)
    expected = []
    assert result == expected

def test_format_number_generator(setup_card_number_generator):
    # Проверка корректности форматирования
    generated_numbers = list(card_number_generator(setup_card_number_generator))
    for number in generated_numbers:
        assert len(number) == 19, f"Номер карты '{number}' имеет неправильную длину"
        assert number.isdigit(), f"Номер карты '{number}' содержит недопустимые символы"

def test_end_number_generator(setup_card_number_generator):
    # Проверка крайних значений
    generated_numbers = list(card_number_generator(setup_card_number_generator))
    assert generated_numbers[0] == f"{start:016d}", "Первый номер карты неверен"
    assert generated_numbers[-1] == f"{end:016d}", "Последний номер карты неверен"

def test_ending_number_generator(setup_card_number_generator):
    # Проверка завершения генерации
    generated_numbers = list(card_number_generator(1,5))
    assert len(generated_numbers) == (end - start + 1), "Количество сгенерированных номеров неверно"


