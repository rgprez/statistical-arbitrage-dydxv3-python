from dydx3 import Client
from web3 import Web3
from constants import (HOST, ADDRESS_ETHEREUM, PRIVATE_KEY_ETH, DYDX3_API_KEY, DYDX3_API_SECRET, DYDX3_API_PASSPHRASE, STARK_KEY_PRIVATE_KEY, RPC_URL_ETH, MODE)

def connect_dydxv3():
    # Create client connection
    client = Client(
        host=HOST,
        api_key_credentials={
            'key' : DYDX3_API_KEY,
            'secret':DYDX3_API_SECRET,
            'passphrase': DYDX3_API_PASSPHRASE
        },
        stark_private_key=STARK_KEY_PRIVATE_KEY,
        eth_private_key=PRIVATE_KEY_ETH,
        default_ethereum_address= ADDRESS_ETHEREUM,
        web3=Web3(Web3.HTTPProvider(RPC_URL_ETH))
    )

    # Check connection
    account = client.private.get_account()
    account_id = account.data['account']['id']
    account_balance = account.data['account']['quoteBalance']
    print('Connection success')
    print('Account ID: ', account_id)
    print(f'Account balance {account_balance}')

    return client