
x = input('Entah the dragon: ')

bot = 0
hot = 0
zot = 0
kot = 0

for i in range(len(x)):
    if 65 <= ord(x[i]) <= 90:
        bot += 1
    if 97 <= ord(x[i]) <= 122:
        hot += 1
    if 48 <= ord(x[i]) <= 57:
        zot += 1
    if ord(x[i]) == 64 or 35 <= ord(x[i]) <= 36:
        kot += 1

if bot == 0:
    print('Missin caps')
if hot == 0:
    print('aint lo way')
if zot == 0:
    print('Where numbah')
if kot == 0:
    print('No special case, no?')
else:
    print('okah')