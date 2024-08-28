# Учебный проект для Skypro

## Описание:
Данный учебный проект создается в рамках практических заданий от онлайн-школы Skypro. В нем содержатся решенные задачи, начиная с урока 9.1.
## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/username/myblog.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```

3. Создайте базу данных и выполните миграции:
```
python manage.py migrate
```

4. Запустите локальный сервер:
```
python manage.py runserver
```
## Структура проекта:
1. .venv/ - виртуальное окружение, которое содержит библиотеки и встроенные скрипты.
2. src/ - сожердит основные файлы с функциями для обработки данных о счетах/банковских картах. А также файл с документацией.
2. tests/ - сожержит файлы, где проводятся тесты в рамках проекта.

## Использование:
Файлы:
1. masks.py - сожердит функции для обработки данных о счетах/банковских картах. Возвращает маски их номеров.
2. widget.py - сожердит функции для обработки данных о счетах/банковских картах и дат. Одна функция возвращает маску номера, относительно входных данных. А другая выводит корректную дату.
3. processing.py - содержит функции для обработки списков словорей. Одна возвращает новый список нужных словарей, другая - отсортированный список по дате.

## Тестирование:
В директории tests/ представлены тесты для проверки качественной работы функций. Используется фреймворк pytest. Покрытие тестами составляет от 80%.

## Документация:

Дополнительную информацию о структуре проекта и API можно найти в [документации](docs/README.md).

## Лицензия:

Проект распространяется под [лицензией MIT](LICENSE).