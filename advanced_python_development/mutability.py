# int,string,float,tuples are immutable
# list, dict are mutable
my_dict={
    'name':'R',
    'age':20
}
print(id(my_dict))
my_dict={
    'name':'R',
    'age':20
}
print(id(my_dict))