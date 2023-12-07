"""Employee pay calculator."""

class Employee:
    def __init__(self, basePay=0, hourlyWage=0, hoursWorked=0, bonus=0, contractsLanded=0, commissionRate=0):
        self.basePay = basePay
        self.hourlyWage = hourlyWage
        self.hoursWorked = hoursWorked
        self.bonus = bonus
        self.contractsLanded = contractsLanded
        self.commissionRate = commissionRate

    def calcContractPay(self):
        if self.contractType == "salary":
            return self.basePay
        elif self.contractType == "hourly":
            return self.hourlyWage * self.hoursWorked
        else:
            return 0  # or another suitable default value

    def calcCommission(self):
        commission = 0
        if self.commissionType == "bonus":
            commission += self.bonus
        elif self.commissionType == "contract":
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

        if self.commissionType == "bonus":
            payDescription += f" and receives a bonus commission of {self.bonus}."
        elif self.commissionType == "contract":
            payDescription += f" and receives a commission for {self.contractsLanded} contract(s) at {self.commissionRate}/contract."

        payDescription += f" Their total pay is {self.get_pay()}."
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
