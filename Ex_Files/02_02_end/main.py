greet = "Hello World"
extened_grt = "Hello World, " + "this is a long string"

name = "John"

#opening/closing bracket with the "f" in front of the string is called interpolation
print("f('......{}....', 'is called interpolation to insert a variable')")
intrupution = f"Hello {name}"

greet_format = "Hello {}"

formatted = greet_format.format(name)

print(intrupution, formatted)

print(formatted.upper())
print(formatted.lower())
print(formatted.replace("John", "Paul"))
