import pytest

@pytest.fixture
def fix_mask_card():
    return ['7000792289606361', '7365410843013587', '70AB79228960DR61']

@pytest.fixture
def fix_mask_account():
    return ['73654108430135874305', '73351653505463512596', '7335165350546351ADCV']

@pytest.fixture
def fix_mask_account_card():
    return ['Счет 64686473678894779589','Visa Platinum 7000792289606361', 'Счет 35383033474447895560']

@pytest.fixture
def fix_mask_account_card_type():
    return ['Счет 64686473678894779589','Visa Platinum 7000792289606361', 'Maestro 7000792289606361', 'MasterCard 7158300734726758', 'Счет 35383033474447895560']

@pytest.fixture
def fix_mask_empty():
    return ''

@pytest.fixture
def fix_mask_error():
    return ['112','asdasd', '1234567891015']

@pytest.fixture
def fix_mask_account_card_error():
    return ['Счет 6468647','Visa Platinum 9606361', 'Mae9606361', '', 'gbfbg2356535365365656', '5383033474447895560']

@pytest.fixture
def fix_get_date():
    return ['2024-03-11T02:26:18.671407','2025-12-11T02:26:18.671407', '2024-03-11T02:2', '2024-03-11T0255555555:26:18.671407', '6651665', '', 'hgyjd462']

@pytest.fixture
def fix_filter_by_state():
    return [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
@pytest.fixture
def fix_filter_by_state_emty():
    return []


@pytest.fixture
def fix_filter_by_state_parm():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
        ]

@pytest.fixture
def fix_sort_by_date():
    return [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]

@pytest.fixture
def fix_sort_by_date_equal():
    return [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-09-12T08:21:33.419441"},
        ]

@pytest.fixture
def fix_sort_by_date_format():
    return [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018/06/30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "12.09.2018T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "12.10.2018"},
        ]