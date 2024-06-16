# Если в процессе выполнения функции произошла ошибка,
# то в лог-файл будет записано сообщение в формате:
# my_function error: <тип ошибки>. Inputs: (1, 2), {}

import functools
from typing import Any, Callable, Optional

# В результате выполнения  будет возвращено значение # 3
# а в лог-файл # mylog.txt
#  будет записано сообщение в следующем формате:
# my_function ok


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор логирует вызов функции и ее результат"""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok. Result: {result}\n"
                if filename:
                    with open(filename, "at") as file:
                        file.write(message)
                else:
                    print(message)
                return result
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "at") as file:
                        file.write(message)
                else:
                    print(message)
                raise e

        return wrapper

    return decorator


# @log(filename="mylog.txt")
# #@log()
# def my_function(x: int, y: int) -> Any:
#     return x / y
# my_function(2, 0)
#
# if __name__ == "__main__":
#     print("PyCharm")
