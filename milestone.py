class milestone:
    def __init__(self, low, high, coefficient):
        if low >= high:
            raise ValueError("low can't be higher than high")
        self.low = low
        self.high = high
        self.coefficient = coefficient
        self.diff = round(number=(self.high-self.low), ndigits=4)
        self.delta = self.diff*0.05
    
    def includesPrice(self, price):
        if self.high >= price >= self.low:
            return True
        return False

    def shouldBuy(self, price):
        # on achète quand c'est moins cher que le low (ou -)
        if price <= self.low + self.delta:
            return True
        return False

    def shouldSell(self, price):
        # on vend quand c'est aussi cher que le high (ou +)
        if price >= self.high - self.delta:
            return True
        return False
    
    def isBought(self, bLunaExcess: float, msLunaBudget: float) -> bool:
        theoricalReturn = self.bLunaReturnAmount(msLunaBudget)
        if bLunaExcess * (1+self.delta) >= theoricalReturn:
            return True
        return False
    
    def bLunaReturnAmount(self, msLunaBudget) -> float:
        theoricalReturn = msLunaBudget*self.low
        return theoricalReturn


    def __str__(self):
        return f"Milestone object (low: {self.low}, high: {self.high}, coefficient: {self.coefficient}, diff: {self.diff})"


def milestonesArrayConsistencyError(milestonesArray: list[milestone]) -> str :
    length = len(milestonesArray)
    if length <= 1:
        return "not enough milestones ({length})"
    elif length <= 3:
        return None
        
    previous = milestonesArray[0]
    i = 1
    while i < len(milestonesArray)-1:
        if previous.low > milestonesArray[i].high:
            return f"wrong milestone order detected at rank {i}"
        elif milestonesArray[i].low >= milestonesArray[i].high:
            return f"high is lower than low at rank {i}"

        previous = milestonesArray[i]
        i += 1

    return None

def higherMilestonesThanPrice(milestones: list[milestone], price: float):
    retMsList = [] 
    for ms in milestones:
        if ms.high > price:
            retMsList.append(ms)
        elif ms.includesPrice(price):
            retMsList.append(ms)

    return retMsList

def milestonesArrayCoefficientsSum(milestonesArray: list[milestone]) -> float:
    ret = 0
    for ms in milestonesArray:
        ret += ms.coefficient
    return ret