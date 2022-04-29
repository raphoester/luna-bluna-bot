from terra_sdk.core import Coin 
from terra_sdk.client.lcd import LCDClient

import const
import util
import balance
import simulation
import swap
import time
import milestone

def main():
    print(f"bot started")
    while True:
        print(f"iteration started")
        walletBalance = balance.getWalletBalance()
        virtualLunaBalance=walletBalance.luna+simulation.simulatebLunaToLunaSwap(walletBalance.bluna)

        print(f"balances : {walletBalance.bluna} bLuna, {walletBalance.luna} luna, {walletBalance.usd} usd")

        milestones = const.MILESTONES
        err = milestone.milestonesArrayConsistencyError(milestones)
        if err is not None:
            print("invalid milestones data : {err}")

        milestones.reverse()
        # calcul du prix moyen
        avgMsBudget = virtualLunaBalance/len(milestones)
        bLunaLunaPairAvgPrice = simulation.bLunaLunaPairAvgPrice(avgMsBudget)
        print(f"average price calculated : 1 bluna = {bLunaLunaPairAvgPrice} luna")

        # somme de coefficients
        coeffSum = milestone.milestonesArrayCoefficientsSum(milestones)
        bLunaExcess = walletBalance.bluna
        boughtMs = []
        notBoughtMs = []
        broke = False
        for ms in milestones:
            if broke:
                print(f"milestone is not bought : {ms}")
                notBoughtMs.append(ms)
                continue
        
            relativeWeight = ms.coefficient/coeffSum
            msLunaInvestment = virtualLunaBalance*relativeWeight
            if ms.isBought(bLunaExcess, msLunaInvestment):
                print(f"milestone is bought : {ms}")
                boughtMs.append(ms)
                bLunaExcess -= ms.bLunaReturnAmount(msLunaInvestment)
            else:
                print(f"milestone is not bought : {ms}")
                notBoughtMs.append(ms)
                broke = True

        investedLunaVariation = 0

        for ms in notBoughtMs:
            if ms.shouldBuy(bLunaLunaPairAvgPrice):
                print(f"buying milestone at price {bLunaLunaPairAvgPrice} : {ms}")
                investedLunaVariation += virtualLunaBalance*(ms.coefficient/coeffSum)

        for ms in boughtMs:
            if ms.shouldSell(bLunaLunaPairAvgPrice):
                print(f"selling milestone at price {bLunaLunaPairAvgPrice} : {ms}")
                investedLunaVariation -= virtualLunaBalance*(ms.coefficient/coeffSum)
        
        print(f"luna balance evolution : {investedLunaVariation}")

        if investedLunaVariation > 0:
            bLunaToBeBought = simulation.simulateLunaTobLunaSwap(investedLunaVariation)
            print(f"buying {bLunaToBeBought} bluna")
            swap.buybLuna(
                const.terra, 
                const.MNEMONIC, 
                const.WALLET_ADDRESS, 
                const.LUNA_BLUNA_SWAP_CONTRACT_ADDRESS, 
                const.BLUNA_CONTRACT_ADDRESS, 
                investedLunaVariation,
                bLunaToBeBought, 
                const.SLIPPAGE,
            )
        elif investedLunaVariation < 0:
            investedLunaVariation = -investedLunaVariation 
            print(f"selling bluna to get back {investedLunaVariation} luna")
            swap.buyLuna(
                const.terra,
                const.MNEMONIC,
                const.LUNA_BLUNA_SWAP_CONTRACT_ADDRESS,
                const.BLUNA_CONTRACT_ADDRESS,
                investedLunaVariation,
            )

        sleepTime = const.SLEEP
        print(f"sleeping for {sleepTime} seconds...")
        time.sleep(sleepTime)

if __name__ == "__main__":
    main()