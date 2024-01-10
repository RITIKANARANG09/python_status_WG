class  Student:
    def __init__(self,name):
        self.name=name



Movies=['a','b']
print(Movies.__class__)
print('hi'.__class__)
print(len(Movies))

class Garage:
    def __init__(self):
        self.cars=[]

    def __len__(self):
        return len(self.cars)

    def __getitem__(self,i):
        return self.cars[i]

    def __repr__(self):
        return f'Garage{self.cars}'

    def __str__(self):
        return f'Garage with {len(self)} cars.'

ford=Garage()
ford.cars.append(('a'))
ford.cars.append(('b'))
print(len(ford))
print(ford[0])  #Garage.__getitem__(ford,0)

for car in ford:
    print(car)


