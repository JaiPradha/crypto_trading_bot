# Crypto Trading Bot (Binance Futures Testnet)

A simplified trading bot built using Python and Binance Futures Testnet.

## Features
- Market & Limit orders
- Buy & Sell support
- Binance Futures Testnet (USDT-M)
- Command Line Interface (CLI)
- Logging & error handling

## Setup Instructions

1. Clone repository
```bash
git clone https://github.com/your-username/crypto_trading_bot.git
cd crypto_trading_bot
📁 Project Structure

crypto_trading_bot/
│
├── bot.py # Core trading bot logic
├── cli.py # CLI interface for user input
├── config.example.py # Sample API configuration
├── logger.py # Logging configuration
├── test.py # API connectivity test
├── requirements.txt # Python dependencies
├── README.md # Project documentation
├── .gitignore # Ignored files (keys, venv, logs)
└── venv/ # Virtual environment (not committed)

Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

3️ . Install dependencies
pip install -r requirements.txt

▶ Running the Bot

Start the CLI interface:

python cli.py

Example CLI Flow:
Enter Symbol (e.g. BTCUSDT): BTCUSDT
Side (BUY / SELL): BUY
Order Type (MARKET / LIMIT): MARKET
Quantity: 0.001

Output:

Order ID

Execution status

Symbol, side, quantity

Error message (if any)
Test API Connectivity

To verify API access before placing orders:

python test.py


Expected result: Futures account information or exchange info JSON.

📜 Logging

All API requests, responses, and errors are logged

Log files are excluded from GitHub using .gitignore

Helps in debugging and audit trails

⚠️ Notes & Limitations

This bot is for educational and testnet use only

No real funds are involved

Advanced order types (Stop-Limit, OCO, Grid, etc.) can be added as extensions

🌱 Future Enhancements (Optional)

Stop-Limit / OCO orders

TWAP or Grid strategy

WebSocket price streaming

Lightweight web UI or enhanced CLI

👤 Author

Jai Pradha
Junior Python Developer
Crypto & API Enthusiast