# Task_3

hox = []
dox = []
lot = []

x = int(input('Entah no of elements: '))
for i in range(x):
    y = int(input('Entah elemental: '))
    hox.append(y)

l = int(input('Entah no of elements: '))
for i in range(l):
    m = int(input('Entah elemental: '))
    dox.append(m)

for i in hox:
    for j in dox:
        bot = i*j
        lot.append(bot)

print(lot)