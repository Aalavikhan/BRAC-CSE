bot = {'a': 100, 'b': 100, 'c': 200, 'd': 300}
tot = {'a': 300, 'b': 200, 'c': 400, 'e': 200}

for i in bot.keys():
    for j in tot.keys():
        if j == i:
            bot[i] = bot.get(i)+tot.get(j)

for i in tot.keys():
    if i not in bot:
        bot[i] = tot[i]

print(bot)