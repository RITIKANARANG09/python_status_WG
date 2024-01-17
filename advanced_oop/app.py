from admin import Admin
from database import Database

a=Admin('ritika','1234',4)
a.save()
print(Database.find(lambda x: x['username']=='ritika'))