import pytest

# Фикстуры для файла masks--------------------------------------
@pytest.fixture
def fix_mask_card():
    return ['7000792289606361', '7365410843013587', '70AB79228960DR61', '7365410843013587154132423122','']

@pytest.fixture
def fix_mask_account():
    return ['73654108430135874305', '73351653505463512596', '7365410843013587154132423122', '7335165350546351ADCV', '123', '']


# Фикстуры для файла widget---------------------------------------
@pytest.fixture
def fix_mask_account_card():
    return ['Счет 64686473678894779589','Visa Platinum 7000792289606361', 'Счет 35383033474447895560']

@pytest.fixture
def fix_mask_account_card_type():
    return ['Счет 64686473678894779589','Visa Platinum 7000792289606361', 'Maestro 7000792289606361', 'MasterCard 7158300734726758', 'Счет 35383033474447895560']

@pytest.fixture
def fix_mask_account_card_error():
    return ['Счет 6468647','Visa Platinum 9606361', 'Mae9606361', '', 'gbfbg2356535365365656', '5383033474447895560']

@pytest.fixture
def fix_get_date():
    return ['2024-03-11T02:26:18.671407','2025-12-11T02:26:18.671407', '2024-03-11T02:2', '2024-03-11T0255555555:26:18.671407', '6651665', '', 'hgyjd462']


# Фикстуры для файла generators-----------------------------------------
@pytest.fixture()
def empty_transactions():
    return []

@pytest.fixture()
def transactions_with_usd():
    transactions = [{
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
    return transactions

@pytest.fixture()
def transactions_without_usd():
    transactions = [{
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": "RUB"
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    ]
    return transactions

@pytest.fixture()
def single_descriptions():
    transaction = [
        {
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
        }]
    return transaction

@pytest.fixture()
def multiple_descriptions():
    transactions =  [{
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
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ]
    return transactions
@pytest.fixture()
def setup_card_number_generator():
    start = 0
    end = 5
    return start, end