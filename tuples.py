tuple_1='a',
tuple_2=('b','c')
print(type(tuple_1))
print(tuple_1)
print(tuple_1+tuple_2)
tuple_3=tuple_1+tuple_2
print(tuple_3)
tuple_4=(('a',1),(2,'b'))
for one,two in tuple_4:
    print(one,two)
for value in tuple_4:
    print(value)