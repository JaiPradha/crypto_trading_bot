from binance.client import Client
from logger import logger


class BasicBot:
    def __init__(self, api_key, api_secret):
        # Initialize client
        self.client = Client(api_key, api_secret)

        # Force Futures Testnet endpoints (VERY IMPORTANT)
        self.client.API_URL = "https://testnet.binancefuture.com"
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logger.info(f"Market Order: {order}")
            return order
        except Exception as e:
            logger.error(f"Market Order Error: {str(e)}")
            return {"error": str(e)}

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=quantity,
                price=price
            )
            logger.info(f"Limit Order: {order}")
            return order
        except Exception as e:
            logger.error(f"Limit Order Error: {str(e)}")
            return {"error": str(e)}

    # BONUS: Stop-Limit Order
    def place_stop_limit_order(self, symbol, side, quantity, stop_price, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                stopPrice=stop_price,
                price=price,
                timeInForce="GTC"
            )
            logger.info(f"Stop-Limit Order: {order}")
            return order
        except Exception as e:
            logger.error(f"Stop-Limit Error: {str(e)}")
            return {"error": str(e)}

    # Utility: Check account connection
    def check_account(self):
        try:
            account = self.client.futures_account()
            logger.info("Futures account accessed successfully")
            return account
        except Exception as e:
            logger.error(f"Account Error: {str(e)}")
            return {"error": str(e)}
