import os
from dotenv import load_dotenv
from terra_sdk.client.lcd import LCDClient

load_dotenv()

0# TERRASWAP
# LUNA_BLUNA_SWAP_CONTRACT_ADDRESS="terra1jxazgm67et0ce260kvrpfv50acuushpjsz2y0p"
# ASTROPORT
LUNA_BLUNA_SWAP_CONTRACT_ADDRESS="terra1j66jatn3k50hjtg2xemnjm8s7y8dws9xqa5y8w"
BLUNA_CONTRACT_ADDRESS ="terra1kc87mu460fwkqte29rquh4hc20m54fxwtsx7gp"

terra = LCDClient(chain_id="columbus-5", url="https://lcd.terra.dev") # mainnet
# terra = LCDClient(chain_id="bombay-12", url="https://lcd.terra.dev") # testnet

MNEMONIC = os.getenv('MNEMONIC')
WALLET_ADDRESS = os.getenv('WALLET_ADDRESS')

BUY_PERCENTAGE = 1 # buy bLuna if the net gain is above 1%
SELL_PERCENTAGE = 2 # sell bluna if the net gain is above 2%

TRADE_AMOUNT_LUNA = 0.1
TRADE_AMOUNT_BLUNA = 0.1

SLIPPAGE = 0.5

MILESTONES = [
    0.955,
    0.96,
    0.965,
    0.97,
    0.975,
    0.98,
    0.985,
    0.99,
    0.995,
    1,
    # 1.005,
    # 1.01,
]

MILESTONE_DEFAULT_INTERVAL = 0.005