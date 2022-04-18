def shouldBuy(blunaBalance, lunaBalance, swapAmountBLuna, swapAmountLuna):
    pass    

def shouldSell(blunaBalance, lunaBalance, swapAmountBLuna, swapAmountLuna):
    pass

# for debug only 
def priceMilestonePair(milestones, price, defaultInterval):
    outOfRange = False
    for key in range(len(milestones)):
        if milestones[key] > price:
            break
        elif key == len(milestones)-1:
            outOfRange = True

    lowMs = milestones[key]
    if key == 0: # extremely low price
        print("low price")
        highMs = milestones[0]
        lowMs = highMs-defaultInterval
    elif outOfRange: # extremely high price
        print("high price")
        lowMs = milestones[key]
        highMs = lowMs+defaultInterval
    else: # normal price
        lowMs = milestones[key-1]
        highMs = milestones[key]

    return (lowMs, highMs)

def convertMilestonesToPairsArray(milestones):
    ret = []
    i = 0
    while i < len(milestones)-1:
        ret.append((milestones[i], milestones[i+1]))
        i+=1
    return ret

def wantedMilestonesCount(milestonesPairs, price):
    milestonesPairs.reverse()
    i = 0
    for pair in milestonesPairs:
        if pair[0] >= price:
            i+=1
        elif pair[0] < price < pair[1]:
            i+=1
            break
        
    return i