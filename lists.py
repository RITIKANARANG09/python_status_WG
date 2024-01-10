# empty list
lists=[]
#list from 0 to 9
lists=list(range(10))
print(lists)
lists.append("a")
print(lists)
lists.pop(10)
print(lists)
lists.pop()
print(lists)
"""
error
lists.pop(13) 
"""

lists.remove(2)
print(lists)
print(sum(lists))
print(max(lists))
print(min(lists))

# ZIP FUNCTION
list_1=['a','b','c','d']
list_2=[1,2,3,4]
print(list(zip(list_1,list_2)))
print(list(zip(list_1,list_2,{4,5})))

#ENUMERATE FUNCTION
for i,(val_1,val_2) in list(enumerate(zip(list_1,list_2))):
    print(i,val_1,val_2)

#list slicing
print(list_1) # a,b,c,d
print(list_1[:]) #a,b,c,d
print(list_1[2:]) #c,d
print(list_1[:2]) #a,b
print(list_1[-2:]) #c,d
print(list_1[:-2]) #a,b
print(list_1[2:4]) #c,d no error
print(list_1[-1:-1]) # empty list
print(list_1[-1:-3]) # empty list
# make a new list having multiple of 5 from the old list
def function_1():
    numbers=[0,2,4,6,8]
    new_numbers=[number*5 for number in numbers]
    print(numbers)
    print(new_numbers)
def print_hi():
    # 1st method
    friends=['A','B','C','D']
    guests=['b','d','e','f']
    friends_lower=set([friend.lower() for friend in friends])
    friends_lower_2 = [friend.lower() for friend in friends]
    guests_lower=set([guest.lower() for guest in guests])
    party_guests=friends_lower.intersection((guests_lower))
    print(party_guests)
    # 2nd method
    party_guests_2=[guest.title().lower() for guest in guests if guest in friends_lower_2]
    print(party_guests_2)


if __name__ == '__main__':
    print_hi()
    function_1()