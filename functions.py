
def doaction(action, *parameter): ## tworzy tupla
    print('action:', action)
    print('parameter:', parameter)
    for element in parameter:
        print('element is:', element)
    return

def doaction2(action, what, **parameter):
    print('action:', action)
    print('what:', what)
    print('parameter:', parameter)
    for element in parameter:
        print(element, '=', parameter[element])
    return

doaction('buy','shoes')
doaction2('buy', 'shoes', size=45, color='brown', type='sport')


def weekdayeng(daynumber):
    names = {
        0: 'monday',
        1: 'tuesday'
    }
    return names.get(daynumber, 'error')

print(weekdayeng(0))