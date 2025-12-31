from bot import BasicBot
from config import API_KEY, API_SECRET

bot = BasicBot(API_KEY, API_SECRET)

print("---- Binance Futures Testnet Trading Bot ----")

symbol = input("Enter Symbol (e.g. BTCUSDT): ").upper()
side = input("Side (BUY / SELL): ").upper()
order_type = input("Order Type (MARKET / LIMIT / STOP): ").upper()
quantity = float(input("Quantity: "))

if order_type == "MARKET":
    result = bot.place_market_order(symbol, side, quantity)

elif order_type == "LIMIT":
    price = float(input("Limit Price: "))
    result = bot.place_limit_order(symbol, side, quantity, price)

elif order_type == "STOP":
    stop_price = float(input("Stop Price: "))
    price = float(input("Limit Price: "))
    result = bot.place_stop_limit(symbol, side, quantity, stop_price, price)

else:
    result = {"error": "Invalid order type"}

print("\nOrder Response:")
print(result)
