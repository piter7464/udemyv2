helloMessage = "Hello %s!"
print(helloMessage % ('Kris'))
helloMessage2 = "Hello {0:s}!"
print(helloMessage2.format('Kris'))
message = "%s has %d %s"
print(message % ('Kate', 1, 'animal'))
helloMessage3 = "{0:s} has {1:d} {2:s}"
print(helloMessage3.format('Kate', 1, 'animal'))

line = '{0:20s} {1:6s} {2:s} {3:s}'
print(line.format('ICE CREAM', 'costs', '3', '€'))

name = 'Piotr'
age = 26
daysinyear = 365

message4 = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message4.format(name, age, age * daysinyear))
