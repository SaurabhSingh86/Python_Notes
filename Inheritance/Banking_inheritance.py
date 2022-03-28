class Bank_account:
    interest_rate = 0.04

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.e_passbook = []
        self.e_passbook.append(f'Initial amount deposited Rs {balance} ')

    def deposit(self, deposit_amount):
        if deposit_amount < 0:
            raise ValueError("Amount should be greater than zero")
        self.balance += deposit_amount
        self.e_passbook.append(f"Amount deposited Rs {deposit_amount}")

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            raise ValueError("Insufficient fund")
        self.balance -= withdraw_amount
        self.e_passbook.append(f'Amount withdrawn Rs {withdraw_amount}')
        return f"Kindly collect the cash Rs {withdraw_amount}"

    def transfer(self, to_account_number, transfer_amount):
        if self.transfer_amount > self.balance:
            raise ValueError("Insufficient fund")
        to_account_number.deposit(transfer_amount)
        self.balance -= transfer_amount

    def statement(self):
        for transaction in self.e_passbook:
            print(transaction)
        print()
        print("*" * 20)
        print(f'Available Balance is {self.balance}')

    def roi(self):
        interest_amount = self.balance * Bank_account.interest_rate
        self.balance += interest_amount
        self.e_passbook.append(f'Interest Amount credited Rs {interest_amount}')

c1 = Bank_account("Ss", 1000)
c2 = Bank_account("Ps", 2000)
c3 = Bank_account("Gs", 3000)


# Refer class 2 file name