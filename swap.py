from terra_sdk.core.wasm.msgs import MsgExecuteContract
from terra_sdk.key.mnemonic import MnemonicKey
from terra_sdk.client.lcd.api.tx import CreateTxOptions
from terra_sdk.core.bank import MsgSend
from terra_sdk.core.coins import Coins
from terra_sdk.core.coins import Coin

import util
import json
import base64

def buybLuna(terra, mnemonic, walletAddress, swapContract, blunaContract, lunaBudget, expectedbLunaAmount, slippage):
    key = MnemonicKey(mnemonic)
    wallet = terra.wallet(key)
    
    executeIncreaseAllowance = MsgExecuteContract(
        wallet.key.acc_address,
        blunaContract,
        {
            "increase_allowance": {
                "amount": str(util.toMicroAmount(lunaBudget)), # dans le snippet original, expectedLunaAmount (?)
                "spender": swapContract,
            }
        }
    )

    executeSwap = MsgExecuteContract(
        wallet.key.acc_address,
        swapContract, 
        {
            "swap": {
                "offer_asset": {
                    "amount": str(util.toMicroAmount(lunaBudget)),
                    "info": {
                        "native_token": {
                            "denom": "uluna"
                        }
                    }
                },
                "sender": walletAddress,    
                "belief_price": str(lunaBudget/expectedbLunaAmount),
                "max_spread": str(slippage/100) # jsp pourquoi on divise par 100
            },
        }, {
            "uluna": str(util.toMicroAmount(lunaBudget)),
        }
    )
    
    transaction = wallet.create_and_sign_tx(CreateTxOptions(msgs=[executeIncreaseAllowance, executeSwap]))

    return terra.tx.broadcast(transaction)

def buyLuna(terra, mnemonic, swapContract, bLunaContract, bLunaBudget):
    key = MnemonicKey(mnemonic)
    wallet = terra.wallet(key)

    swapMsg = {
        "swap": {
            "max_spread": "0.05"
        }
    }

    encodedSwapMsg = base64.b64encode(json.dumps(swapMsg).encode("ascii")).decode("ascii")

    executeSwap = MsgExecuteContract(
        sender=wallet.key.acc_address,
        contract=bLunaContract,
        execute_msg={
            "send": {
                "contract": swapContract,
                "amount": str(util.toMicroAmount(bLunaBudget)),
                "msg": encodedSwapMsg,
            }
        },
        coins=Coins()
    )

    transaction = wallet.create_and_sign_tx(CreateTxOptions(msgs=[executeSwap]))
    return terra.tx.broadcast(transaction)


if __name__ == "__main__":
    pass
    # print(buybLuna(0.001, 0.001))
    # print(buyLuna(0.001))