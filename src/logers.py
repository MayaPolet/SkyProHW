# 1.	Создайте логеры для перечисленных модулей:
# o	 masks # ,# utils# .
# 2.	Реализуйте запись логов в файл. Логи должны записываться в папку
# logs#  в корне проекта. Файлы логов должны иметь расширение .log
# .
# 3.	Формат записи лога в файл должен включать метку времени, название модуля,
# уровень серьезности и сообщение, описывающее событие или ошибку, которые произошли.

# 4.	Лог должен должен перезаписываться при каждом запуске приложения

import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filemode='w')

log1 = logging.getLogger('utils')
log1.setLevel(logging.DEBUG)
log2 = logging.getLogger('masks')
log2.setLevel(logging.DEBUG)


handler1 = logging.FileHandler(r'..\logs\log_utils.log', encoding='utf-8', mode='w')
handler1.setFormatter(logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
log1.addHandler(handler1)

handler2 = logging.FileHandler(r'..\logs\log_masks.log', encoding='utf-8', mode='w')
handler2.setFormatter(logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
log2.addHandler(handler2)






