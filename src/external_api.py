# Если транзакция была в # USD или # EUR
# происходит обращение к внешнему API для получения текущего курса валют и конвертации суммы операции в рубли.
# Для конвертации валюты воспользуйтесь Exchange Rates Data API: https://apilayer.com/exchangerates_data-api.
# Функцию конвертации поместите в модуль # external_api

import json
import os
from typing import Any
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
#print(f'API_KEY= {API_KEY} ')
params = {"apikey": os.getenv("API_KEY")}


def currency_exchange_rate(currency: str) -> float:
    """Принимает название валюты и возвращает ее курс к рублю"""
    response = requests.get(
        f"https://api.apilayer.com/fixer/latest?base={currency.upper()}&symbols=RUB", params=params)

    return float(response.json()["rates"]["RUB"])

# rate = currency_exchange_rate('USD')
# print(f"Курс = {rate}")



def currency_conversion(currency: str, sum_transaction: float) -> Any:
    """Конвертирует  сумму в валюте по курсу с API и возвращает сумму в рублях в формате float"""

    url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}"
    #url = f"https://api.apilayer.com/fixer/latest?base={currency.upper()}&symbols=RUB"

    try:
        #response = requests.get(url, headers={"apikey": API_KEY})
        response = requests.get(url, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return 0.00


    #response_data = json.loads(response.text)
    response_data = response.json()

    print(response_data)
    rate = response_data["rates"]["RUB"]

    print(f"Курс = {rate}")
    result = round(sum_transaction * rate, 2)
    return  result

if __name__ == "__main__":
    #print(f"Курс = {currency_exchange_rate('USD')}")
    print(f"Конвертированная сумма = {currency_conversion('USD',  10)}")