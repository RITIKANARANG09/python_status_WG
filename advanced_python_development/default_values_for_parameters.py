accounts={
    'checking':1234.0,
    'savings':23.0
}

def add_balance(amount:float,name:str='checking')->float:
    accounts[name]+=amount
    return accounts[name]

add_balance(500)
print(accounts['checking'])

print("\nMUTABLE DEFAULT ARGUMENTS")
def create_account(name:str,holder:str,account_holders:list=[]):
    account_holders.append(holder)

    return {
        'name':name,
        'main_account_holder':holder,
        'account_holders':account_holders
    }

a1=create_account('checking','Rolf')
a2=create_account('savings','Ritika')
print(a2)

"""REMEDIES"""
"""
1)
def create_account(name:str,holder:str,account_holders:list):
a1=create_account('checking','Rolf',[])

2)def create_account(name:str,holder:str,account_holders=None):
if not account_holders:
account_holders=[] ya args me bi pass kr skte ek list
"""