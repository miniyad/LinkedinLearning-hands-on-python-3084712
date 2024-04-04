print("most common type of python collection is a list")
print("lists are mutable")

NAMES = ["John", "Paul", "George", "Ringo"]
AGES = [20, 21, 22, 23]


JOHN = NAMES[0]
PAUL = NAMES[1]

print("slice notation names[:2], names[2:3], etc")
print("can create new lists from slices")
print("names", NAMES)
print("ages", AGES)
JOHN_PAUL = NAMES[:2]
GEORGE_RINGO = NAMES[2:]
REVERSE = NAMES[::-1]   #notation[start:stop:step] so no start no stop, step by -1 whole list
EVERY_OTHER = NAMES[::2] #no start no stop, step 2 Paul Ringo
EVERY_THIRD = NAMES[::3]
EVERY_FOURTH = NAMES[::4] #always start with the first, then step

print("built-in functions sum, min, max")
print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(JOHN_PAUL)
print(GEORGE_RINGO)
print(REVERSE, "print the whole list from right side, step by -1")
print(EVERY_OTHER, "print first, step 2")
print(EVERY_THIRD, "print first, step 3")
print(EVERY_FOURTH, "print first, step four...off the end")
