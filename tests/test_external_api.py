import os
import json
from unittest.mock import MagicMock, Mock
from unittest.mock import patch

from dotenv import load_dotenv


from src.external_api import currency_conversion, params



load_dotenv()
headers = {"apikey": os.getenv("API_KEY")}

@patch("requests.get")
def test_currency_conversion(mock_get):
    mock_get.return_value.json.return_value = {
        "success": True,
        "timestamp": 1719382276,
        "base": "USD",
        "date": "2024-06-06",
        "rates": {"RUB": 88.503702},
    }
    assert currency_conversion("USD", 10) == 885.04

    mock_get.assert_called_once_with("https://api.apilayer.com/exchangerates_data/latest?base=USD", params=params)


