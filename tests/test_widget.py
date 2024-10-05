from src.widget import mask_account_card
from src.widget import get_date

def test_mask_account_card(fix_mask_account_card):
    '''Тесты для проверки, что функция корректно распознает
    и применяет нужный тип маскировки в зависимости от типа входных данных
    (карта или счет)'''
    mask_account =[]
    for el in fix_mask_account_card:
        if el != '' and len(el) <= 31 and len(el) >= 22:
            account_masks = mask_account_card(el)
        else:
            account_masks = 'Неверный номер карты'
        mask_account.append(account_masks)
    assert mask_account == (['Счет **9589', 'Visa Platinum 7000 79** **** 6361', 'Счет **5560'])

def test_mask_account_card_type(fix_mask_account_card_type):
    '''Параметризованные тесты с разными типами карт и счетов
    для проверки универсальности функции'''
    mask_account = []
    for el in fix_mask_account_card_type:
        if el != '' and len(el) <= 31 and len(el) >= 22:
            account_masks = mask_account_card(el)
        else:
            account_masks = 'Неверный номер карты'
        mask_account.append(account_masks)
    assert mask_account == (['Счет **9589', 'Visa Platinum 7000 79** **** 6361', 'Maestro 7000 79** **** 6361', 'MasterCard 7158 30** **** 6758', 'Счет **5560'])

def test_mask_account_card_error(fix_mask_account_card_error):
    '''Тестирование функции на обработку некорректных входных данных
    и проверка ее устойчивости к ошибкам'''
    mask_account = []
    for el in fix_mask_account_card_error:
        if el != '' and len(el) <= 31 and len(el) >= 22:
            account_masks = mask_account_card(el)
        else:
            account_masks = 'Неверный номер карты'
        mask_account.append(account_masks)
    assert mask_account == (['Неверный номер карты','Неверный номер карты','Неверный номер карты','Неверный номер карты','Неверный номер карты','Неверный номер карты'])

def test_get_date(fix_get_date):
    '''Тестирование правильности преобразования даты'''
    result = []
    for el in fix_get_date:
        result_fix = get_date(fix_get_date)
        result.append(result_fix)
    assert result == (['11.03.2024','11.12.2025', '11.03.2024', '11.03.2024', 'Некорректные данные. Введите дату в формате: ГГГГ-ММ-ДД', '', 'Некорректные данные. Введите дату в формате: ГГГГ-ММ-ДД'])