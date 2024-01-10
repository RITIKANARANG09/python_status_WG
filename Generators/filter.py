friends=['Ritika','Vaishali','Akshat','Rajat']
def my_custom_filter(func,iterable):
    for i in iterable:
        if func(i):
            yield i
starts_with_r=my_custom_filter(lambda friend:friend.startswith('R'),friends)
another_starts_with_r=(f for f in friends if f.startswith('R'))

