# example
accounts={
    'checking':1234.0,
    'savings':23.0
}

def add_balance(amount:float,name:str='checking')->float:
    accounts[name]+=amount
    return accounts[name]

transactions=[
    (-1.0,'c'),
    (1.0,'s'),
    (51.0,'s'),
    (41.0,'s'),
    (31.0,'s')
]

#different methods to pass
for t in transactions:
    add_balance(t[0],t[1])
    add_balance(*t)
    add_balance(amount=t[0],name=t[1])
    amount,name=t
    add_balance(amount=amount,name=name)
    add_balance(name=t[0],amount=t[1])


class User:
    def __init__(self,username,password):
        self.username=username,
        self.password=password

    @classmethod
    def from_dict(cls,data):
        return cls(data['username'],data['password'])

users=[
    {'username':'r','password':'rr'},
    {'username':'s','password':'ss'}
]
user_objects=map(User.from_dict(),users)
user_objects=[User.from_dict(u) for u in users]
user_objects=[User(data['username'],data['password']) for data in users]
user_objects=[User(**data) for data in users]

#TUPLES
new_users=[
    (1,2),
    (3,4)
]
user_objects_new=[User(*data) for data in new_users]