from datetime import datetime, timedelta
import time
from pprint import pprint
from func_utils import format_number

# Place market order
def place_order_market(client, market, side, size, price, reduce_only):
    # Get position id
    account_response = client.private.get_account()
    position_id = account_response.data['account']['positionId']

    # Get expiration time
    server_time = client.public.get_time()
    expiration = datetime.fromisoformat(server_time.data['iso'].replace('Z', '')) + timedelta(seconds=70)

    # Place an order
    placed_order = client.private.create_order(
        position_id=position_id, # required for creating the order signature
        market=market,
        side=side,
        order_type='MARKET',
        post_only=False,
        size=size,
        price=price,
        limit_fee='0.015',
        expiration_epoch_seconds=expiration.timestamp(),
        time_in_force='FOK',
        reduce_only=reduce_only
    )

    # Return result
    return placed_order.data


# Abort all open positions
def abort_all_positions(client):

    # Cancel all orders
    client.private.cancel_all_orders()

    # Portect API
    time.sleep(0.5)

    # Get markets fro reference of tick size
    markets = client.public.get_markets().data

    # pprint(markets)

    # Portect API
    time.sleep(0.5)

    # Get all open positions
    positions = client.private.get_positions(status='OPEN')
    all_positions = positions.data['positions']

    pprint(all_positions)

    # Handle open positions
    close_orders = []
    if len(all_positions) > 0:

        # Loop thourgh each position
        for position in all_positions:

            # Determine Market
            market = position['market']

            # Determine Side
            side = 'BUY'
            if position['side'] == 'LONG':
                side = 'SELL'

            # Get price
            price = float(position['entryPrice'])
            accept_price = price * 1.7 if side == 'BUY' else price * 0.3
            tick_size = markets['markets'][market]['tickSize']
            accept_price = format_number(accept_price, tick_size)

            # Place order to close
            order = place_order_market(
                client=client,
                market=market,
                side=side,
                size=position['sumOpen'],
                price=accept_price,
                reduce_only=True
            )

            # Append result
            close_orders.append(order)

            # Portect API
            time.sleep(0.2)

        # Return closed orders
        return close_orders
