# TASK_5

given_tuple = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
blob = 0

x = int(input('Entah a number boi: '))

for i in given_tuple:
    if i == x:
        blob += 1
    else:
        pass

if blob == 0:
    print("Numbeh not in 'ere mate")
else:
    print("Number in 'ere "+str(blob)+" times mate")