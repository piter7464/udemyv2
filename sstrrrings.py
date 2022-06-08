print('TVP1','TVP2','TVN','Polsat','BBC','HBO','MTV', sep=';')

print('I like computers ','TVP1','TVP2','TVN','Polsat','BBC','HBO','MTV', sep=' but better is ')

ProgramName = 'BBC'
Item = 'News'
Time = '18:00'

print('I like watching ', Item, 'at ', Time, 'on ', ProgramName, '.', sep='')

quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'

print(quote.upper()) ## upper letters
print(quote.lower()) ## lower letters
print(quote.endswith('street'))
print(quote.isupper())
print(quote.upper().isupper())
print(quote.find('one'))
print(quote.replace('one', '1').replace('both', '2'))
print(quote.split(' '))
print(quote.isdigit())
print(quote.isdecimal())
print(quote.isalpha())
print(quote.isalnum())


firstName = 'Kasia'
famillyName = 'Sowa'
lastName = 'Mrugała'

print(firstName + ' ' + famillyName + ' ' + lastName)

music = '"Universal Fanfare" Jerry Goldsmith \n "Happy Together" Garry Bonner \n "I\'m a Man" Steve Winwood '
print(music)

