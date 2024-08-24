import pytest

@pytest.fixture
def mask_card():
    return '7000792289606361', '7365410843013587', '70AB79228960DR61', '7365410843013587154132423122',''

@pytest.fixture
def mask_account():
    return '73654108430135874305', '73351653505463512596', '7365410843013587154132423122', '7335165350546351ADCV', '123', ''

@pytest.fixture
def mask_account_card_fix():
    return 'Счет 64686473678894779589','Visa Platinum 7000792289606361', 'Счет 35383033474447895560'

@pytest.fixture
def mask_account_card_fix_type():
    return 'Счет 64686473678894779589','Visa Platinum 7000792289606361', 'Maestro 7000792289606361', 'Maestro7000792289606361', 'MasterCard 7158300734726758', 'Счет 35383033474447895560'

@pytest.fixture
def mask_account_card_fix_error():
    return 'Счет 6468647','Visa Platinum 9606361', 'Mae9606361', '', 'gbfbg23565353653656..56', '5383033474447895560'

@pytest.fixture
def get_date_fix():
    return '2024-03-11T02:26:18.671407','2025-12-11T02:26:18.671407', '2024-03-11T02:2', '2024-03-11T0255555555:26:18.671407', '6651665', '', 'hgyjd462'
