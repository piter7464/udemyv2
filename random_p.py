import random

min = 1
max = 6

dice = random.randint(min, max)

if dice == 1:
    print('1:\n\no\n\n')
elif dice == 2:
    print('2:\n\to\n\no')
elif dice == 3:
    print('3:\n\t\to\n\to\no')
elif dice == 4:
    print('4:\noo\noo')
elif dice == 5:
    print('5:' + '\noo''\n''o\noo')
elif dice == 6:
    print('6:\noo\noo\noo')

dices = []

for i in range(5):
    dices.append(random.randint(min, max))

dices.sort()
print(dices)
