from collections import deque

friends=deque(('a','b','d','f'))

def friend_upper():
    while friends:
        friend=friends.popleft().upper()
        greeting=yield
        print(f'{greeting} {friend}')

def greet(n):
    g.send(None)
    while True:
        greeting =yield
        g.send(greeting)

greeter=greet(friend_upper())
greeter.send(None)
greeter.send('hello')
greeter.send('how are you')