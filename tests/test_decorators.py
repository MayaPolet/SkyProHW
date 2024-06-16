# Напишите декоратор  log
# , который будет логировать вызов функции и ее результат в файл или в консоль.
# Декоратор # log   принимает один необязательный аргумент # filename
# , который определяет путь к файлу, в который будут записываться логи.
# Если # filename не задан, то логи будут выводиться в консоль.
# Если вызов функции закончился ошибкой, то записывается сообщение об ошибке и входные параметры функции.
# Пример использования:
#
# @log(filename="mylog.txt")
# def my_function(x, y):
#     return x + y
#
# my_function(1, 2)
# В результате выполнения функции # my_function(1, 2)
#  будет возвращено значение # 3
# , а в лог-файл # mylog.txt
#  будет записано сообщение в следующем формате:
#
# my_function ok
# Если в процессе выполнения функции произошла ошибка, то в лог-файл будет записано сообщение в формате:
#
# my_function error: <тип ошибки>. Inputs: (1, 2), {}

from typing import Union

# import os.path
import pytest

from src.decorators import log


def test_log_file() -> None:
    """Тест записи в файл если нет ошибки"""

    @log("mylog.txt")
    def example_function(x: int, y: int) -> Union[int, float]:
        return x / y

    result = example_function(2, 2)
    with open("mylog.txt", "rt") as file:
        for line in file:
            message = line
    assert message == "example_function ok. Result: 1.0\n"
    assert result == 1.0


# def test_log_console(capsys: pytest.CaptureFixture[str]) -> None:
def test_log_console(capsys) -> None:
    """Тест вывода в консоль если нет ошибки и не указано имя лог-файла"""

    @log()
    def example_function(x: int, y: int) -> Union[int, float]:
        return x / y

    result = example_function(2, 2)
    captured = capsys.readouterr()
    print(captured)
    assert captured.out == "example_function ok. Result: 1.0\n\n"
    assert result == 1.0


def test_log_err_file() -> None:
    """Тест вывода в файл если ошибка"""

    @log("mylog.txt")
    def example_function(x: int, y: int) -> Union[int, float]:
        raise ValueError()

    with pytest.raises(ValueError):
        example_function(2, 2)
    with open("mylog.txt", "rt") as file:
        for line in file:
            message = line
    assert message == "example_function error: ValueError. Inputs: (2, 2), {}\n"


def test_log_err_console(capsys) -> None:
    """Тест вывода в консоль если ошибка и не указано имя лог-файла"""

    @log()
    def example_function(x: int, y: int) -> Union[int, float]:
        raise ValueError()

    with pytest.raises(ValueError):
        example_function(2, 2)
    captured = capsys.readouterr()
    assert captured.out == "example_function error: ValueError. Inputs: (2, 2), {}\n\n"


#
