class BankAccount:
    def __init__(self, bank_name: str, balance: int):
        self.bank_name = bank_name
        self.balance = balance

    def add_money(self, ammount):
        self.balance += ammount

    def withdraw_money(self, ammount):
        if ammount < self.balance:
            self.balance -= ammount
        else:
            print("you broke")


boa_acc = BankAccount("Bank Of America", 5000)

boa_acc.add_money(300)
boa_acc.withdraw_money(6000)

print(boa_acc.balance)
