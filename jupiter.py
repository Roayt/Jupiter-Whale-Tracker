"""Jupiter API: fetch current USD prices for trcked tokens"""

import requests

from config import Wsol_Mint,Usdc_Mint,Usdt_Mint

def get_token_price():
    mints=f"{Wsol_Mint},{Usdc_Mint},{Usdt_Mint}"
    price_url=f"https://lite-api.jup.ag/price/v3?ids={mints}"

    try:
        headers={"User-Agent":"WhaleTrackerBot/1.0"}
        response=requests.get(price_url,headers=headers,timeout=20)
        response.raise_for_status()
        data=response.json()

        sol_price=float(data.get(Wsol_Mint,{}).get("usdPrice",69.0))
        usdc_price=float(data.get(Usdc_Mint,{}).get("usdPrice",1.0))
        usdt_price=float(data.get(Usdt_Mint,{}).get("usdPrice",1.0))

        return {Wsol_Mint:sol_price,Usdc_Mint:usdc_price,Usdt_Mint:usdt_price}
    
    except Exception as e:
        print("Error while generating price:{e}: using fallback prices")
        return {Wsol_Mint:69.0,Usdc_Mint:1.0,Usdt_Mint:1.0}


