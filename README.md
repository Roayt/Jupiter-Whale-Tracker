# Jupiter Whale Tracker Script 

A Python script that monitors large swaps on Solana's Decentralized Exchange Jupiter in real time and sends instant alerts on Telegram when a trade crosses a threshold.

## What it does

- Extract recent Jupiter transactions through the Helius RPC API
- Filters Failed Transactions and ones already seen
- Calculates each swap's USD value using live prices from the Jupiter Api 
- Sends clean structured Telegram alerts 

## Project's Structure

- `main.py` - entry point runs the scan loop continously 

- `config.py` - loads secret from .`env` and defines all important data

- `helius.py` - extracts transaction data from Helius 

- `jupiter.py` - extracts live token price from Jupiter API

- `notifyer.py` - sends alert to Telegram

- `tracker.py` - core logic;detects whale trades and triggers alert

## Setup

1. Clone This repository
2. Install dependencies:`pip install -r requirements.txt`
3. Copy .env.example to .env and fill in your own keys
4. Run the bot: python3 main.py

## Environment Variables

These go in your .env file (see `.env.example`)

- `Helius_Api_Key` - your Helius RPC API key
- `Telegram_Bot_Token` - your Telegram bot token from BotFather 
- `Telegram_Chat_Id`- the chat ID where alerts are sent 

## Built With 

Python •Helius RPC •Jupiter API •Telegram Bot API