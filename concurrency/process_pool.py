import time
from concurrent.futures import ProcessPoolExecutor
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

#PROCESSES
start=time.time()
with ProcessPoolExecutor(max_workers=2) as pool:
     pool.submit(complex_calculation)
     pool.submit(ask_user)

print(f'Two process total time: {time.time()-start}')
