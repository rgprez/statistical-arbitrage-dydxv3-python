# Imports | Testnet
import os
from dydx3.constants import API_HOST_SEPOLIA, API_HOST_MAINNET
from dotenv import load_dotenv

load_dotenv()

MODE = "DEVELOPMENT"

# Close all open positions nad orders
ABORT_ALL_POSTIONS = False

# Find Cointegrated Pairs
FIND_COINTEGRATED = True

# Place trades
PLACE_TRADES = True

# Resolution
RESOLUTION = '1HOUR'

# Stats window
WINDOW = 21

# Thersholds - Opening
MAX_HALF_LIFE = 24
ZSCORE_THRESH = 1.5
USD_PER_TRADE = 50
USD_MIN_COLLATERAL = 1880

# Threshold - Closing
CLOS_AT_ZSCORE_CROSS = True

# Ethereum Address
ADDRESS_ETHEREUM = os.getenv('ADDRESS_ETHEREUM')
PRIVATE_KEY_ETH = os.getenv('PRIVATE_KEY_ETH')

#Keys - Testnet
STARK_KEY_PRIVATE_KEY_TESTNET = os.getenv('STARK_KEY_PRIVATE_KEY_TESTNET')
DYDX3_API_KEY_TESTNET = os.getenv('DYDX3_API_KEY_TESTNET')
DYDX3_API_SECRET_TESTNET = os.getenv('DYDX3_API_SECRET_TESTNET')
DYDX3_API_PASSPHRASE_TESTNET = os.getenv('DYDX3_API_PASSPHRASE_TESTNET')

#Keys - Mainnet
STARK_KEY_PRIVATE_KEY_MAINNET = os.getenv('STARK_KEY_PRIVATE_KEY_MAINNET')
DYDX3_API_KEY_MAINNET = os.getenv('DYDX3_API_KEY_MAINNET')
DYDX3_API_SECRET_MAINNET = os.getenv('DYDX3_API_SECRET_MAINNET')
DYDX3_API_PASSPHRASE_MAINNET = os.getenv('DYDX3_API_PASSPHRASE_MAINNET')

# Keys - Export
STARK_KEY_PRIVATE_KEY = STARK_KEY_PRIVATE_KEY_MAINNET if MODE == 'PRODUCTION' else STARK_KEY_PRIVATE_KEY_TESTNET
DYDX3_API_KEY = DYDX3_API_KEY_MAINNET if MODE == 'PRODUCTION' else DYDX3_API_KEY_TESTNET
DYDX3_API_SECRET = DYDX3_API_SECRET_MAINNET if MODE == 'PRODUCTION' else DYDX3_API_SECRET_TESTNET
DYDX3_API_PASSPHRASE = DYDX3_API_PASSPHRASE_MAINNET if MODE == 'PRODUCTION' else DYDX3_API_PASSPHRASE_TESTNET

# Host - Export
HOST = API_HOST_MAINNET if MODE == 'PRODUCTION' else API_HOST_SEPOLIA

# Provider - Export
RPC_URL_ETH_MAINNET=os.getenv('RPC_URL_ETH_MAINNET')
RPC_URL_ETH_TESTNET=os.getenv('RPC_URL_ETH_TESTNET')
RPC_URL_ETH = RPC_URL_ETH_MAINNET if MODE == 'PRODUCTION' else RPC_URL_ETH_TESTNET