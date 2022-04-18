class Cuenta:

    def __init__(self,accountNumber,balance):

        self.accountNumber = accountNumber
        self.balance = balance

    def consultBalance(self):
        print(self.balance)