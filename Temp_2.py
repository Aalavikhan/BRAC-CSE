# Task_3

x = input('Entah sumin: ')

tot = 0
bot = 0

for i in range(len(x)):
    if tot == 0:
        if 65 <= ord(x[i]) <= 90:
            tot += i
    else:
        if 65 <= ord(x[i]) <= 90:
            bot += i

for i in range(tot+1,bot):
    print(x[i],end='')