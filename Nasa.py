from Fubar import Fubar

foobar = Fubar("Hi",3,True,"Janitor","5.5")
foobar.setName("hi")
print(foobar.getName())
Fubar.setName(foobar,"bye")
print(foobar.getName())

foobar2 = Fubar("second fubar",4)

print(foobar2.getName())
