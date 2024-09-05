name = "Merhab"
id = 43
# old style string formattting
message = "Hello, %s. Your id is: %s"%(name, id)

# str.format() method 
# uses type 1
message = "Hi, {}. Your id is: {}".format(name, id) 
message = "Hi, {name}. Your is: {id}".format(name="Ope",id=24)


# f-string 
message = f'Hi {name}. Your id is {id}'

# Template string 
from string import Template
template = Template("Hi, $name, Id: $id")
message = template.substitute(name=name,id=id)

# Concatanation
message = "Hi, " + name + ". You id is " + str(id)
print(message)
