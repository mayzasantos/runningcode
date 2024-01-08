import requests
from datetime import datetime

request = requests.get(
    "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
)

request_dic = request.json()
quote_dolar = request_dic["USDBRL"]["bid"]
quote_euro = request_dic["EURBRL"]["bid"]
quote_btc = request_dic["BTCBRL"]["bid"]

print(
    f"Updated quote: {datetime.now()} \nDólar: R${quote_dolar}\nEuro: R${quote_euro}\nBTC: R${quote_btc}"
)
