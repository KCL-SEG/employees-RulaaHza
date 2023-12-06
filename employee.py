"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contractType=None, basePay=None, hourlyWage=None, hoursWorked=None,
                 commissionType=None, commissionRate=None, bonus=None, contractsLanded=None):
        self.name = name
        self.contractType = contractType
        self.basePay = basePay
        self.hourlyWage = hourlyWage
        self.hoursWorked = hoursWorked
        self.commissionType = commissionType
        self.commissionRate = commissionRate
        self.bonus = bonus
        self.contractsLanded = contractsLanded

    def calcContractPay(self):
        if self.contractType == "salary":
            return self.basePay
        elif self.contractType == "hourly":
            return self.hourlyWage * self.hoursWorked
    
    def calcCommission(self):
        commission = 0
        if self.commissionType == "bonus":
            commission += self.bonus
        if self.commissionType == "contract":
            commission += self.contractsLanded * self.commissionRate
        return commission

    def get_pay(self):
        totalPay = self.calcContractPay() + self.calcCommission()
        return totalPay

    def __str__(self):
        payDescription = f"{self.name} works on a {self.contractType} contract"
        if self.contractType == "salary":
            payDescription += f" of {self.basePay}"
        elif self.contractType == "hourly":
            payDescription += f" of {self.hoursWorked} hours at {self.hourlyWage}/hour"
        payDescription += f". Their total pay is {self.get_pay()}."
        return payDescription


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
