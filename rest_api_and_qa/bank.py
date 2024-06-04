from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import json
from bankaccount import BankAccount

with open(r"rest_api_and_qa\accounts.json","r") as account:
    my_account_dict = json.load(account)



bank_accounts ={}
for key,val in my_account_dict.items():
    bank_accounts[int(key)]=BankAccount(**val)




# a =bank_accounts[123456].deposit(100)
# bank_accounts[123456].transfer(30,bank_accounts[643829])
# print(bank_accounts)

app = FastAPI()

@app.get("/accounts")
async def get_accounts():
    return bank_accounts

@app.get("/account/{account_id}")
async def get_account(account_id):
    return bank_accounts.get(int(account_id), '{"meesage":"did not find"}')

@app.post("/account/{account_id}/deposit")
async def depositor(account_id:int,amount:int):
    bank_accounts[int(account_id)].deposit(int(amount))
    return bank_accounts.get(int(account_id),'account wasn\'t found')

@app.post("/account/{account_id}/withdraw")
async def withdrawer(account_id:int,amount:int):
    if int(account_id) in bank_accounts.keys():
        bank_accounts[int(account_id)].withdraw(int(amount))
        if int(amount) * 1.1 > bank_accounts[int(account_id)].balance:
            return f"You can\'t withdraw {int(amount)}$ when you only have {bank_accounts[int(account_id)].balance}$."
    else:
        return bank_accounts.get(int(account_id),'account wasn\'t found')

@app.post("/account/{account_id}/transfer")
async def transferer(account_id:int,amount:int,account_for_delivery:int):
    if int(account_id) in bank_accounts.keys() and int(account_for_delivery) in bank_accounts.keys():
        if bank_accounts[int(account_id)].balance >= 1.1 * amount:
            bank_accounts[int(account_id)].transfer(int(amount),bank_accounts[int(account_for_delivery)])
            return [bank_accounts[int(account_id)],bank_accounts[int(account_for_delivery)]]
        else:
            return f'there is not enough money in {bank_accounts[int(account_id)].id}'
    else:
        return "one of the accounts was not found"







if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=5000)