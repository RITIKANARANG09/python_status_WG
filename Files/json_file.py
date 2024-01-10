import json
file=open("json_data.txt",'r')
file_contents=json.load(file) # loads file and convert it into dictionary
file.close()
print(file_contents["friends"][0])

cars=[
    {'name':'a','model':'aa'},
    {'name':'b','model':'bb'}
]
file=open("json_data.txt",'w')
json.dump(cars,file)
file.close()

my_json_string='[{"name":"r","released":2001}]'
incorrect_car=json.loads(my_json_string)
print(incorrect_car[0]['name'])
