file_open=open('data.txt','r')
file=file_open.read()
file_open.close()
print(file)

username=input('Enter username')
file_open=open('data.txt','w')
file_open.write(username)
file_open.close()

# friends nearby
friends=input("Enter 3 friends seperated by comma").split()
people=open('people.txt','r')
people_nearby=[line.strip() for line in people.readlines()]
people.close()

friends_set=set(friends)
people_nearby_set=set(people_nearby)
friends_nearby=friends_set.intersection(people_nearby_set)

nearby_friends=open('friends.txt','w')

for friend in friends_nearby:
    print(f'{friend} is nearby')
    nearby_friends.write(f'{friend}')

nearby_friends.close()
