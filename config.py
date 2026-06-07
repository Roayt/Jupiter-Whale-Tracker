"""Configuration file loads secrets from .env and defines all constants."""

import os 
from dotenv import load_dotenv

load_dotenv()

Helius_api_key=os.getenv("Helius_Api_Key")
print(f"DEBUG key loaded: {Helius_api_key is not None}, length: {len(Helius_api_key) if Helius_api_key else 0}")
Telegram_bot_token=os.getenv("Telegram_Bot_Token")
Telegram_chat_id=os.getenv("Telegram_Chat_Id")

Jupiter_Program="JUP6LkbZbjS1jKKwapdHNy74zcZ3tLUZoi5QNyVTaV4"
Wsol_Mint="So11111111111111111111111111111111111111112"
Usdc_Mint="EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"
Usdt_Mint="Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB"

Whale_Threshold=100
Scan_Interval_Seconds=10

Rpc_Url=f"https://mainnet.helius-rpc.com/?api-key={Helius_api_key}"
Enhanced_url=f"https://api.helius.xyz/v0/transactions/?api-key={Helius_api_key}"