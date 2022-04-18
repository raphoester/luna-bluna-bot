import const
import util

def simulateLunaTobLunaSwap(toBeTraded):
    toBeTraded = util.toMicroAmount(toBeTraded)
    simulation = const.terra.wasm.contract_query(
        const.LUNA_BLUNA_SWAP_CONTRACT_ADDRESS,
        {
            "simulation": {
                "offer_asset": {
                    "amount": str(toBeTraded),
                    "info": {
                        "native_token": {
                            "denom": "uluna"
                        }
                    }
                }
            }
        }   
    )

    return util.fromMicroAmount(simulation["return_amount"])
    
def simulatebLunaToLunaSwap(toBeTraded):
    toBeTraded = util.toMicroAmount(toBeTraded)
    simulation = const.terra.wasm.contract_query(
        const.LUNA_BLUNA_SWAP_CONTRACT_ADDRESS,
        {
            "simulation": {
                "offer_asset": {
                    "amount": str(toBeTraded),
                    "info": {
                        "token": {
                            "contract_addr": const.BLUNA_CONTRACT_ADDRESS
                        }
                    }
                }
            }
        }
    )

    return util.fromMicroAmount(simulation["return_amount"])


if __name__ == "__main__":
    toBeTraded = 0.1
    bLunaReturnAmount = simulateLunaTobLunaSwap(toBeTraded)
    price = util.price(toBeTraded, bLunaReturnAmount)
    print(price)