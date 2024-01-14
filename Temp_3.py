# Task_5

x = input('Entah sumin boi: ')
y = input('Entah anothah shite: ')

dot = []
zot = []

bot = ''
hot = ''

for i in range(len(x)):
    for j in range(len(y)):
        if y[j] in x:
            if y[j] in bot and j not in dot:
                bot += y[j]
                dot.append(j)
            elif y[j] not in bot and j not in dot:
                bot += y[j]
                dot.append(j)
            else:
                pass

for i in range(len(y)):
    for j in range(len(x)):
        if x[j] in y:
            if x[j] in hot and j not in zot:
                hot += x[j]
                zot.append(j)
            elif x[j] not in hot and j not in zot:
                hot += x[j]
                zot.append(j)
            else:
                pass

print(str(hot)+str(bot))