# Old style formatting
name = "Merhab"
age = 25
greetings = "1.Hello %s!, your age is %s" % (name, age)
print(greetings)

# str.format() method
greetings = "2.Hello {}!, your age is {}".format(name, age)
print(greetings)

# >> with named placeholder
greetings = "2.1 Hello {name}!, your age is {age}".format(name='Zoti', age=25)
print(greetings)


# F-sting
x = 10
y = 2
msg = f"3.Sum of {x} + {y} is {x+y}"
print(msg)

# Template string
from string import Template as T 

template = T('4.Hello $name, Your age is $age')
greetings = template.substitute(name="Mehrab", age = age)
print(greetings)

# Concatanation
greetings = "5.Hello " + str(name) + "!, Your age is " + str(age)
print(greetings)