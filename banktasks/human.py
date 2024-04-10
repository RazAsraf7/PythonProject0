#from bank import Bank


class Human:
    def __init__(self, name, id, banks_array):
        self.name = name
        self.id = id
        self.banks_array = banks_array
        print(f"You are {self.name} and your ID is: {self.id}")

    def depositInBank(self, bank_name, amount):
        if amount <= 0:
            return print("You can\'t deposit a negative number of money.")
        for bank in self.banks_array:
            if bank_name == bank.name:
                bank.money += amount
                print(f"You have now successfuly deposited {bank.money}$ into {bank.name}")
                break
    def withdrawFromAnyBank(self, how_much : int):
        if how_much > 5000:
            return print(f"You don\'t have enough money in all your banks in order to withdraw {how_much}$")
        for bank in self.banks_array:
            if how_much <= bank.money:
                bank.money -= how_much
                print(f"Your money now is {bank.money}$ in {bank.name}")
                break





'''A_bank = Bank(1000, "A_bank")
B_bank = Bank(2000, "B_bank")
C_bank = Bank(3000, "C_bank")
D_bank = Bank(4000, "D_bank")
E_bank = Bank(5000, "E_bank")

all_banks = [A_bank, B_bank, C_bank, D_bank, E_bank]

glen = Human("Glen", "123456", all_banks)
glen.depositInBank(C_bank, 700)
glen.withdrawFromAnyBank(3050)'''