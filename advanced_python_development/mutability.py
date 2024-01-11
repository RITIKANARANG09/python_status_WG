# int,string,float,tuples are immutable
# list, dict are mutable
my_dict={
    'name':'R',
    'age':20
}
print(id(my_dict))

my_dict={
    'name':'R',
    'age':20
}
print(id(my_dict))

my_dict['name']='RR' #my_dict.__setitem__(self,'RR')
print(id(my_dict))

my_int=5
print(id(my_int))

my_int=my_int+1      # my_int.__add__(self,1): self.value+=1
print(id(my_int))

my_int+=1
print(id(my_int))

friends=['r','v']
print(id(friends))

friends.append('rr')
print(id(friends))

print("\nARGUMENT MUTABILITY")
friends_last_seen={
    'R':20,
    'S':40
}
def see_friend(friend,name):
    print(id(friend)) # same dict is passed
    print(friend is friends_last_seen) # is checks id
    friend[name]=0 #integers are immutable

print(id(friends_last_seen))
print(id(friends_last_seen['R']))
see_friend(friends_last_seen,'R')
print(id(friends_last_seen))
print(id(friends_last_seen['R']))

age=20
def increase_age(current_age):
    current_age=current_age+1

print(f'id is {id(age)}')
increase_age(age)
print(f'id of updated age is :{id(age)}')

primes=[2,3,4]
print(id(primes))
primes+=[7,11] # primes=primes.__iadd([7,11])
print(id(primes))
primes=primes+[9,00] #primes=primes.__add__([9,00])
print(id(primes))
primes=[33]+[89]
print(id(primes))
