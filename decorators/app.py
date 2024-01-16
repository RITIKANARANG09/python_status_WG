import functools

user={'username':'ritika', 'access_level':'user'}

def third_level(access_level):
    def user_has_permission(func):
        @functools.wraps(func)
        def secure_func():
            if user.get('access_level')=='user':
                return func()
        return secure_func
    return user_has_permission
@third_level("admin")
def my_function(panel):
    return f" Password for {panel} panel is 1234."
@third_level("admin")
def another():
    pass

print(my_function.__name__)
print(another.__name__)
#my_function=user_has_permission(my_function)
"""
user_has_permission=third_level(admin)
my_function=user_has_permission(my_function)
"""
my_function=third_level('admin')(my_function)
