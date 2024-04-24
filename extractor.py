import os
import requests

def get_transactions(wallet_address):
    """Fetch the transaction list of an Ethereum wallet from Etherscan using the provided API key from environment variables."""
    api_key = os.getenv('api_key')  
    if not api_key:
        raise ValueError("No API key provided. Please set the 'api_key' environment variable.")

    url = "https://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'txlist',
        'address': wallet_address,
        'startblock': 0,
        'endblock': 99999999,
        'sort': 'asc',
        'apikey': api_key
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        transactions = response.json()
        return transactions
    else:
        raise Exception(f"Failed to fetch transactions: {response.status_code} {response.text}")

# Example Usage
wallet_address = '0x99fd1378ca799ed6772fe7bcdc9b30b389518962'
try:
    transactions = get_transactions(wallet_address)
    print(transactions)
except Exception as e:
    print(e)
