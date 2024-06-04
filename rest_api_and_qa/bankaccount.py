from pydantic import BaseModel


class BankAccount(BaseModel):
    
    id: int
    first_name:str
    last_name:str
    balance:int

    def withdraw(self,amount:int):
        if amount*1.1 > self.balance:
            return f"You can't withdraw {amount}$ when you have only {self.balance}$."
        else:
            ten_percent = amount * 1.1
            self.balance -= ten_percent
            return f"Successfully withdrawn {amount}$ from your balance. Due to 10% taxes your account balance now has {self.balance}$."
        
    def deposit(self,amount:int):
        ten_percent = amount * 0.9
        self.balance += ten_percent
        return f"Successfully deposited {amount}$ into your balance. Due to 10% taxes your account balance now has {self.balance}$."
    
    def transfer(self,amount:int,account):
        ten_percent = amount * 0.9
        if self.balance >= amount:
            self.withdraw(amount)
            account.deposit(amount)
            return f"Successfully transfered {amount}$ to {account}. Due to 10% taxes {account} received {ten_percent}$."




# '123441' = BankAccount(id=123441,first_name='Raz',last_name='Asraf',balance=2134124)
# '342749' = BankAccount(id=342749,first_name="Adi",last_name='Hadad',balance=319341)
# '123441'.transfer(50,342749)