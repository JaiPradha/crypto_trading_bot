from binance.client import Client

client = Client()
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

print(client.futures_exchange_info())
