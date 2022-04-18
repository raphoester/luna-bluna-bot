import const 
import util

class uWalletBalance:
    def __init__(self, uusd, uluna, ubluna):
        self.uusd = uusd
        self.uluna = uluna
        self.ubluna = ubluna

class walletBalance:
    def __init__(self, usd, luna, bluna):
        self.usd = usd
        self.luna = luna
        self.bluna = bluna


def getWalletBalance():
    balance = const.terra.bank.balance(const.WALLET_ADDRESS)
    uLunaCoin = balance[0].get("uluna")
    if uLunaCoin is None:
        uLunaCoin = util.emptyCoin()
    uUsdCoin = balance[0].get("uusd")
    if uUsdCoin is None: 
        uUsdCoin = util.emptyCoin()

    res = const.terra.wasm.contract_query(
        const.BLUNA_CONTRACT_ADDRESS,
        {
            "balance": 
            {
                "address": const.WALLET_ADDRESS
            }
        } # query msg
    )

    return walletBalance(
        usd=util.fromMicroAmount(uUsdCoin.amount), 
        luna=util.fromMicroAmount(uLunaCoin.amount), 
        bluna=util.fromMicroAmount(res["balance"])
    )
