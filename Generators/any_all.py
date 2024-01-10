friends=[
    {
        'name':'a',
        'location':'aa'
    },
    {
        'name':'b',
        'location':'bb'
    }
]
your_location=input("Enter your location")
friends_nearby=(friend for friend in friends if friend['location']==your_location)
if any(friends_nearby):
    print("friends are nearby")

print(all([1,2]))
print(all([0,1]))