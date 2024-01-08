#Dictionaries and dictionary views are reversible.
d = {"one": 1, "two": 2, "three": 3, "four": 4}

print(list(reversed(d)))

print(list(reversed(d.values())))

print(list(reversed(d.items())))
