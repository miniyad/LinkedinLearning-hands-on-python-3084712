greet = "Hello World"
extened_grt = "Hello World, " + "this is a long string"
print(greet)

print(extened_grt)
name = "John"

#opening/closing bracket with the "f" in front of the string is called interpolation
print("f('......{}....', 'is called string interpolation ... used to insert a variable')")
print("the strings with an 'f' in front are also called f-strings")
print("also look at string built-in helper methods like .upper(), .lower(), .replace()")

intrupution = f"Hello {name}"

greet_format = "Hello {}"

formatted = greet_format.format(name)

print(intrupution, formatted)

print(formatted.upper())
print(formatted.lower())
print(formatted.replace("John", "Paul"))
