import time
from threading import Thread
def ask_user():
    start=time.time()
    user_input=input('Enter your name: ')
    greet=f'Hello {user_input}'
    print(greet)
    print(f'ask_user, {time.time()-start}')
def complex_calculation():
    start=time.time()
    print('Start calculating....')
    [x**2 for x in range(2000000)]
    print(f'complex_calculation, {time.time()-start}')

start=time.time()
ask_user()
complex_calculation()
print(f'Single threaded total time: {time.time()-start}')

#using multithreading
thread1=Thread(target=ask_user)
thread2=Thread(target=complex_calculation)
thread3=Thread(target=complex_calculation)

start=time.time()

#thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()

print(f'Two thread total time: {time.time() - start}')
