from collections import deque
from types import coroutine

friends=deque(('a','b','d','f'))
@coroutine
def friend_upper():
    while friends:
        friend=friends.popleft().upper()
        greeting=yield
        print(f'{greeting} {friend}')

async def greet(n):
   await n

greeter=greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
