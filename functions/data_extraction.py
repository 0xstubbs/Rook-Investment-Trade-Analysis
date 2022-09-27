import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()
ALCHEMY_ROOK_API_KEY = os.getenv('ALCHEMY_ROOK_API_KEY')

def get_tokenTransfersByTokenContract(token_address, wallet_address):
    # ALCHEMY_ROOK_API_KEY = os.getenv('ALCHEMY_ROOK_API_KEY')
    print(f'Running get_tokenTransfersbyContract.\nInput contract: {token_address}\nWallet Address: {wallet_address}')
    print('This function uses the Alchemy API to get transfers')

    url = f"https://eth-mainnet.alchemyapi.io/v2/{ALCHEMY_ROOK_API_KEY}"
    print(url)
    to_payload = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "alchemy_getAssetTransfers",
            "params": [
                {
                    "fromBlock": "0x0",
                    "toBlock": "latest",
                    "contractAddresses": ["0xeb4c2781e4eba804ce9a9803c67d0893436bb27d"],
                    "category": ["erc20"],
                    "withMetadata": True,
                    "excludeZeroValue": False,
                    "maxCount": "0x3e8",
                    "toAddress": "0x9a67f1940164d0318612b497e8e6038f902a00a4",
                    "order": "asc"
                }
            ]
        }
    from_payload = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "alchemy_getAssetTransfers",
            "params": [
                {
                    "fromBlock": "0x0",
                    "toBlock": "latest",
                    "contractAddresses": ["0xeb4c2781e4eba804ce9a9803c67d0893436bb27d"],
                    "category": ["erc20"],
                    "withMetadata": True,
                    "excludeZeroValue": False,
                    "maxCount": "0x3e8",
                    "fromAddress": "0x9a67f1940164d0318612b497e8e6038f902a00a4",
                    "order": "asc"
                }
            ]
        }
    
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    
    df = pd.DataFrame()
    for payload in [from_payload, to_payload]:
        first_response = True
        
        response = requests.post(url, json=payload, headers=headers).json()['result']
        print(response.keys())
        
        
        while True:
            page_key = response.get('pageKey', False)
            print(page_key)
            if first_response is True:
                print('first response')
                transfers = response['transfers']
                df_temp = pd.json_normalize(transfers).drop(['erc721TokenId', 'erc1155Metadata', 'tokenId', 'category', 'rawContract.value'], axis = 1)
                df_temp['rawContract.decimal'] = df_temp.loc[:, 'rawContract.decimal'].apply(int, base = 16)
                
                df = pd.concat([df, df_temp], axis = 0)
                first_response = False
                
            elif first_response is False and page_key is not False:
                print(f'page_key: {page_key}')
                to_payload_pk = {
                            "id": 1,
                            "jsonrpc": "2.0",
                            "method": "alchemy_getAssetTransfers",
                            "params": [
                                {
                                    "fromBlock": "0x0",
                                    "toBlock": "latest",
                                    "contractAddresses": ["0xeb4c2781e4eba804ce9a9803c67d0893436bb27d"],
                                    "category": ["erc20"],
                                    "withMetadata": True,
                                    "excludeZeroValue": False,
                                    "maxCount": "0x3e8",
                                    "toAddress": "0x9a67f1940164d0318612b497e8e6038f902a00a4",
                                    "order": "asc",
                                    "pageKey": page_key
                                }
                            ]
                        }
                response = requests.post(url, json=to_payload_pk, headers=headers).json()['result']
                df_temp = pd.json_normalize(response['transfers']).drop(['erc721TokenId', 'erc1155Metadata', 'tokenId', 'category', 'rawContract.value'], axis = 1)
                df_temp['rawContract.decimal'] = df_temp.loc[:, 'rawContract.decimal'].apply(int, base = 16)
                
                df = pd.concat([df, df_temp], axis=0)
            else:
                print('No page_key')
                break
    
    return df
    
    
def get_treasuryBalanceByDate(date, wallet_address):
    print(f'Running get_treasuryBalanceByDate.\nInput Date: {date}\nWallet Address: {wallet_address}')