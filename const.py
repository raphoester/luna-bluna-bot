import os
import milestone
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

SLIPPAGE = 0.5

SLEEP = 3600

MILESTONES = [
    milestone.milestone(0.980, 0.985, 25),
    milestone.milestone(0.985, 0.990, 25),
    milestone.milestone(0.990, 0.995, 25),
    milestone.milestone(0.995, 1.000, 25),
]

