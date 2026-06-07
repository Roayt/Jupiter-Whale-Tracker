""" Core logic: detect whale trades and triggers alerts"""

from config import Whale_Threshold
from helius import get_signatures,get_parsed_transaction
from jupiter import get_token_price
from notifyer import send_telegram_alert

seen_signatures=set()

def calculate_trade(tx,prices):
    max_usd_value=0

    for transfer in tx.get("tokenTransfers",[]):
        mint=transfer.get("mint")
        amount=float(transfer.get("tokenAmount",0))

        if mint in prices:
            usd_size=amount*prices[mint]
            if usd_size>max_usd_value:
                max_usd_value=usd_size
    return max_usd_value


def scan_once():
    print("Scanning Solana BlockChain For whale activity")
    rwa_sig=get_signatures(50)
    if not rwa_sig:
        print("No Transaction Found")
        return

    successful=[tx["signature"] for tx in rwa_sig if tx.get("err") is None]

    new_sig=[sig for sig in successful if sig not in seen_signatures]
    if not new_sig:
        print("No signatures found")
        return

    parsd_txs=get_parsed_transaction(new_sig)
    current_price=get_token_price()
    whale_count=0

    for tx in parsd_txs:
        sig=tx.get("signature")
        seen_signatures.add(sig)

        if tx.get("type") in ["SWAP","UNKNOWN"]:
            Usd_size=calculate_trade(tx,current_price)
            if Usd_size>=Whale_Threshold:
                whale_count+=1
                raw_desc=tx.get("description") or "No details"
                safe_desc=str(raw_desc).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")

                tg_message=(
                    f"🚨<b>WHALE ALERT</b>🚨\n"
                    f"<b>Value:</b>${Usd_size:,.2f}\n"
                    f"<b>Wallet:</b><code>{tx.get('feePayer')}</code>\n"
                    f"<b>Details:</b>{safe_desc}\n"

                )

                send_telegram_alert(tg_message)

                print(f"[WHALE ALERT--Trade>={Whale_Threshold:,}]")
                print(f"Value:                {Usd_size:,.2f}")
                print(f"Wallet:               {tx.get('feePayer')}")
                print(f"Description:          {tx.get('description')}")
                print(f"Signature:            {sig}")
                print("_"*50)

    
    if whale_count==0:
        print(f"Scan finished:Evaluated {len(new_sig)} transactions.No whales found")
