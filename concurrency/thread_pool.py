import time
from concurrent.futures import  ThreadPoolExecutor
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

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(ask_user)
    #pool.shutdown() (no need and it is blocking operation)

print(f'Two thread total timr: {time.time()-start}')
