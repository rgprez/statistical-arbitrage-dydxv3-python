from constants import ABORT_ALL_POSTIONS, FIND_COINTEGRATED
from func_connections import connect_dydxv3
from func_private import abort_all_positions
from func_public import construct_market_prices

if __name__ == '__main__':
    try:
        print('Connecting to client...')
        client = connect_dydxv3()

    except Exception as e:
        print(f'Error connecting to client: {e}')
        exit(1)

    if ABORT_ALL_POSTIONS:
        try:
            print('Closing all positions...')
            close_orders = abort_all_positions(client)
        except Exception as e:
            print(f'Error closing all positions: {e}')
            exit(1)

    # Find Cointegrated Pairs
    if FIND_COINTEGRATED:

        # Construct Market Prices
        try:
            print('Fetching market prices, please allow 3 mins...')
            df_market_prices = construct_market_prices(client)
        except Exception as e:
            print(f'Error constructing market prices: {e}')
            exit(1)
