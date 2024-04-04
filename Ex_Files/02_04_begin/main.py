NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]

print("list, NAMES", NAMES)
print("list, AGES", AGES)
print("various forms for the for-in loop and the while loop")



i = 0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i += 1

for name in NAMES:
    print(name)

for name, age in zip(NAMES, AGES):
    print(f"{name} {age}")



for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)

# enumerate
for i, name in enumerate(NAMES):
    print(f"{i}  {name}")

#play with zipping....
print("play with 'zipping' lists in a loop; try four at once")
HOBBIES = ["fishing", "flying", "fighting", "flipping"] 
RIDE = ["modernLongBoard", "thruster", "gun", "swallowTail"]   
for name, age, hobby, surfBoard in zip(NAMES, AGES, HOBBIES, RIDE):
    print(f"name:{name}_____age: {age}______surf board:{surfBoard}_____hobby:{hobby}")


