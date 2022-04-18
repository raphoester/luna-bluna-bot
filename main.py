from terra_sdk.core import Coin 
from terra_sdk.client.lcd import LCDClient
import const
import util
import balance
import simulation
import swap
import decision



def main():

    walletBalance = balance.getWalletBalance()
    virtualLunaBalance=walletBalance.luna+simulation.simulatebLunaToLunaSwap(walletBalance.bluna)

    cellsCount = len(const.MILESTONES)-1
    cellBudget = virtualLunaBalance/cellsCount

    tobLunaPrice = util.price(cellBudget, simulation.simulateLunaTobLunaSwap(cellBudget))
    toLunaPrice = util.price(simulation.simulatebLunaToLunaSwap(cellBudget), cellBudget)

    avgPrice = (tobLunaPrice+toLunaPrice)/2

    milestones = const.MILESTONES
    defaultInterval = const.MILESTONE_DEFAULT_INTERVAL

    milestonePairs = decision.convertMilestonesToPairsArray(milestones)
    wanted = decision.wantedMilestonesCount(milestonePairs, avgPrice)
    print(f"wanted milestones = {wanted}")

    investedProportion = wanted/len(milestonePairs)
    wantedInvest = investedProportion*virtualLunaBalance

    print(wantedInvest)

    # lunaToBeTraded = min(const.MAX_TRADE_AMOUNT_LUNA, walletBalance.luna)
    # bLunaToBeTraded = min(const.MAX_TRADE_AMOUNT_BLUNA, walletBalance.bluna)

    # bLunaReturnAmount = simulation.simulateLunaTobLunaSwap(lunaToBeTraded)
    # lunaReturnAmount = simulation.simulatebLunaToLunaSwap(bLunaToBeTraded)

    
    # print(f"it is possible to trade {bLunaToBeTraded} bLuna for {lunaReturnAmount} Luna, resulting a gain of {lunaGain}%")
    # print(f"it is possible to trade {lunaToBeTraded} Luna for {bLunaReturnAmount} bLuna, resulting a gain of {bLunaGain}%")

    # price = util.price(toBeTraded, bLunaReturnAmount)
    # print(f"luna to bLuna price : {}")

    # if bLunaGain > const.BUY_PERCENTAGE:
    #     swap.buybLuna(const.terra, const.MNEMONIC, const.WALLET_ADDRESS, const.LUNA_BLUNA_SWAP_CONTRACT_ADDRESS, const.BLUNA_CONTRACT_ADDRESS, const.TRADE_AMOUNT_LUNA, bLunaReturnAmount, const.SLIPPAGE)
    # elif lunaGain > const.SELL_PERCENTAGE:
    #     swap.buyLuna(const.terra, const.MNEMONIC, const.LUNA_BLUNA_SWAP_CONTRACT_ADDRESS, const.BLUNA_CONTRACT_ADDRESS, const.TRADE_AMOUNT_BLUNA)
    # return 

if __name__ == "__main__":
    main()