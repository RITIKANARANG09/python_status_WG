from collections import Counter

device_temp=[13.5,14.0,14.0,14.5,14.51,14.5,15.0,16.0]
temp_counter=Counter(device_temp)
print(temp_counter[14.0])

print(Counter({'hello':1,'hy':2})['hy'])

#DEFAULT DICTIONARY
from collections import defaultdict
my_company='WG'
coworkers=['Ritika','Vaishali','Akshat','Ayush']
other_coworkers=[('Smriti','Thales'),('Anoushka','HCL')]

coworker_companies=defaultdict(lambda:my_company)

for person,place in other_coworkers:
    coworker_companies[person]=place

print(coworker_companies[coworkers[0]])
print(coworker_companies['Anoushka'])

#ORDER DICT
from collections import OrderedDict
