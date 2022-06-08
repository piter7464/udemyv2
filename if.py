minlikes = 500
minshares = 100

num_likes = 400
num_shares = 120

if num_likes >= minlikes and num_shares >= minshares:
    print('Sale -10%!')
else:
    print('Not enough likes and shares')


isPizzaOrdered = False
isBigDrinkOrdered = True
isWeekend = True

if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print('You got ticket')
else:
    print('Sorry')

diskSize = 256
diskSizeUsed = 174
fileSize = 100

if diskSizeUsed + fileSize < diskSize:
    print('File can be downloaded')
else:
    print('Not enough space on disk')


#####

if num_likes >= minlikes and num_shares >= minshares:
    print('Sale -10%!')
elif num_likes < minlikes and num_shares > minshares:
    print('Not enough likes')
elif num_shares < minshares and num_likes > minlikes:
    print('Not enough shares')

if not isWeekend and (isPizzaOrdered or isBigDrinkOrdered):
    print('You got ticket')
elif not isWeekend and (not isPizzaOrdered and not isBigDrinkOrdered):
    print('You didn\'t buy pizza or big drink')
elif isWeekend:
    print('Bonus only available in week')

