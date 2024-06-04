from banktasks.human import Human
from banktasks.bank import Bank

A_bank = Bank(1000, "A_bank")
B_bank = Bank(2000, "B_bank")
C_bank = Bank(3000, "C_bank")
D_bank = Bank(4000, "D_bank")
E_bank = Bank(5000, "E_bank")

all_banks = [A_bank, B_bank, C_bank, D_bank, E_bank]

glen = Human("Glen", "123456", all_banks)
glen.depositInBank("C_bank", 700)
glen.withdrawFromAnyBank(5001)
