class TaxCalculator:
    __STAN_DED = 12550
    __SELF_EMP_RATE = .153
    __SELF_EMP_DEDUCT = .0765
    __CHARITABLE_DEDUCT = 300 #Assumes max deduction available
    __LOW_BRACK = 9950
    __MED_BRACK = 40525
    __HIGH_BRACK = 86375

    __LOW_RATE = 0.10
    __MED_RATE = 0.12
    __HIGH_RATE = 0.22

    __revenue = 0
    __mileage = 0
    __profit = 0
    __selfEmployTax = 0
    __taxableIncome = 0
    __incomeTax = 0
    __tithing = 0
    __afterTaxIncome = 0
    __seperateOut = 0

    def __init__(self, *args):
        for arg in args:
            self.__revenue += arg

    def setMileage(self, mileage):
        self.__mileage = mileage

    def calculate(self):
        #Do not change order
        #Change order bad
        self.__profit = self.__calcProfit()
        
        if self.__profit <= 0:
            return

        self.__selfEmployTax = self.__calcSelfEmptTax()
        self.__taxableIncome = self.__calcTaxableIncome()
        self.__incomeTax = self.__calcIncomeTax()
        self.__tithing = self.__calcTithing()
        self.__afterTaxIncome = self.__calcAfterTaxIncome()
        self.__seperateOut = self.__calcSeperateOut()

    def __calcProfit(self):
            return self.__revenue - self.__mileage

    def __calcSelfEmptTax(self):
        taxable = self.__profit - (self.__profit * self. __SELF_EMP_DEDUCT)
        return taxable * self.__SELF_EMP_RATE

    def __calcTaxableIncome(self):
        ti = self.__profit - self.__STAN_DED
        ti -= self.__selfEmployTax / 2
        ti -= self.__CHARITABLE_DEDUCT

        if (ti < 0):
            return 0
        return ti

    def __calcIncomeTax(self):
            income = self.__taxableIncome

            if (income <= 0):
                return 0
            elif (income > 0 and income < self.__LOW_BRACK):
                return income * self.__LOW_RATE
            elif (income > self.__LOW_BRACK and income < self.__MED_BRACK):
                firstbracktax = 995
                income -= self.__LOW_BRACK
                secondbrack = income * self.__MED_RATE
                return firstbracktax + secondbrack
            else:
                raise Exception("How did you make this much")

    def __calcTithing(self):
        return (self.__profit - self.__selfEmployTax - self.__incomeTax) * .1

    def __calcAfterTaxIncome(self):
        return self.__profit - self.__selfEmployTax - self.__incomeTax - self.__tithing

    def __calcSeperateOut(self):
        return self.__profit - self.__afterTaxIncome

    def getProfit(self):
        return self.__profit

    def getSelfEmployTax(self):
        return self.__selfEmployTax

    def getTaxableIncome(self):
        return self.__taxableIncome

    def getIncomeTax(self):
        return self.__incomeTax

    def getTithing(self):
        return self.__tithing

    def getAfterTaxIncome(self):
        return self.__afterTaxIncome

    def getSeperateOut(self):
        return self.__seperateOut
