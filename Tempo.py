#ZIPPPPP FUNCTION AEEEEEEEE



drivers = ["Hamilton", "Verstappen", "Vettel"]
championship = (7, 3, 4)
wins = (103, 54, 53)

pajn = str(championship)
print(pajn)

drives = zip(drivers, championship, wins)

for i in drives:
    print(i)

hoga = dict(zip(drivers,pajn))

print(type(hoga))

for key,value in hoga.items():
    print(key+" : "+value)