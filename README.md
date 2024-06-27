# SkyPro
Для домашек в курсе Python.38.0

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/MayaPolet/SkyProHW.git
```
2. Установите зависимости:
```
poetry install
```
## Использование:

1. Откройте приложение в вашем веб-браузере.
2. Созданы модули:

- decorators:
  - Декоратор логирует вызов функции и ее результат
- external_api:
  - Содержит функцию обращение к внешнему API для получения 
    текущего курса валют и конвертации суммы операции в рубли
- generators:
  - Содержит функцию, которая принимает список словарей с банковскими операциями 
    и возвращает итератор, который выдает по очереди операции с заданной валютой
- logers:
  - Содержит логеры для модулей masks и utils
  - Логи записываются в папку logs
  - Логи перезаписываются при каждом запуске 
- masks:
  - Содержит функции, возвращающие маску карты и маску счета
- processing:
  - Содержит функцию, которая принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты 
- widget:
  - Содержит функцию, на входе строка с информацией — тип карты/счета и номер карты/счета,
    возвращает исходную строку с замаскированным номером карты/счета

## Документация:

Для получения дополнительной информации обратитесь к [документации](docs/README.md). (в разработке)

## Лицензия:

Этот проект не лицензирован по [лицензии MIT](LICENSE).

## Тестирование:

Код тестируется  при помощи pytest