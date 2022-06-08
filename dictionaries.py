chanels = {'Google':1480, 'Email':300, 'Natural traffic':440, 'TV Spot':700}

print(chanels['Email'])

chanelsUpdate = {'Natural traffic':520, 'News':600}

chanels.update(chanelsUpdate)
print(chanels)
print(chanels.keys())
print(chanels.pop('Email'))
print(chanels)