transactions = (
    [
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
        },
        {
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
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": "USD"
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": "RUB"

            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)
def filter_by_currency(transactions:dict, currency:str) -> dict:
    '''Функция, которая принимает список словарей и возвращает итератор'''
    for el in transactions:
        if el['operationAmount']['currency'] == currency:
            yield el

for el in filter_by_currency(transactions, 'USD'):
    print(el)


def transaction_descriptions(transactions:dict) -> str:
    '''Генератор, который принимает список словарей и возвращает описание каждой операции по очереди'''
    for transaction in transactions:
        yield transaction['description']

for description in transaction_descriptions(transactions):
    if transactions != []:
        print(description)
    else:
        print('[]')

def card_number_generator(start:int, end:int) -> str:
    ''' Генератор номеров банковских карт, который должен генерировать номера карт в формате XXXX XXXX XXXX XXXX'''
    if str(start).isalpha() and str(end).isalpha():
        yield 'Некорректные входные данные'
    elif start < 1 or end > 9999999999999999 or start > end:
        yield "Диапазон должен быть от 0000 0000 0000 0001 до 9999 9999 9999 9999"
    else:
        for i in range(int(start), int(end) + 1):
            formatted_card_number = f"{i:016}"
            formatted_card_number = f"{formatted_card_number[:4]} {formatted_card_number[4:8]} {formatted_card_number[8:12]} {formatted_card_number[12:]}"
            yield formatted_card_number

for card_num in card_number_generator('j', 'j'):
    print(card_num)
