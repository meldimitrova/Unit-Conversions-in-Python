# @author Melina Dimitrova

# Using external package Axiompy to perform conversions
## Axiompy can convert @length, @time, @mass

from axiompy import Units
units = Units()

print(units.unit_convert(3 * units.metre, units.foot))
print(units.unit_convert(5 * units.year, units.decade))

### Length conversion
u1 = input("What length value would you like to convert?")
length = int(u1)
aL = input("What unit would you like to convert length from?")
bL = input("What unit would you like to convert length into?")

print(units.unit_convert(length * units.unit(aL), units.unit(bL)))


### Time conversion
u2 = input("What time value would you like to convert?")
time = int(u2)
aT = input("What unit would you like to convert time from?")
bT = input("What unit would you like to convert time into?")

print(units.unit_convert(time * units.unit(aT), units.unit(bT)))


### Time conversion
u3 = input("What mass value would you like to convert?")
mass = int(u3)
aM = input("What unit would you like to convert mass from?")
bM = input("What unit would you like to convert mass into?")

print(units.unit_convert(mass * units.unit(aM), units.unit(bM)))
