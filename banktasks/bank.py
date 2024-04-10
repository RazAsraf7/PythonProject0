class Bank:
    def __init__(self, money : int, name : str):
        self.money = money
        self.name = name
        print(f"Bank account of {self.name} holds on to {self.money}$")
    def withdraw(self, amount : int):
        if amount <= self.money:
            self.money -= amount
            print(f"Your bank now has {self.money}$")
            return amount
        else:
            print(f"You can only withdraw {self.money}$")
            return 0
    def deposit(self, funds):
        self.money += funds
        print(f"Your bank now has {self.money}$")
    def introduce(self):
        print(self.name, self.money)

'''razbank = Bank(1000, "Raz")
razbank.withdraw(500)
razbank.deposit(700)'''