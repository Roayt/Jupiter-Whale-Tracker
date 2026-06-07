"""Helius API & RPC call:  fetch transaction signatures and parsed transaction """

import requests

from config import Rpc_Url,Enhanced_url,Jupiter_Program

def get_signatures(limit):
    payload={"jsonrpc":"2.0",
             "id":"1",
             "method":"getSignaturesForAddress",
             "params":[Jupiter_Program,{"limit":limit}]
             }
    
    try:
        response=requests.post(Rpc_Url,json=payload)
        response.raise_for_status()
        return response.json().get("result",[])

    except Exception as e:
        print("❌ Error while fetching signatures:{e}")
        return []
    
def get_parsed_transaction(signatures):
    if not signatures:
        return []
    
    try:
        response=requests.post(Enhanced_url,json={"transactions":signatures},timeout=20)
        return response.json()
    except Exception as e:
        print("Error while Parsing transaction:{e}")
        return []