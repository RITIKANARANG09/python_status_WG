set_1={1,2,3,4,'a'}
set_2={'b','a','2','9'}
print(set_1)
set_1.add('d')
"""
set_1.add({'d','e'}) #error
"""
print(set_1)
set_1.remove(3)
print(set_1)
print(set_1 | set_2)
print(set_2 & set_1)
print (set_1 - set_2)
print(set_1>set_2)
print(set_1>=set_2)
print(set_1^set_2)

