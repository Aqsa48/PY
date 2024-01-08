

# Remove d[key] from d. Raises a KeyError if key is not in the map.

d = dict(one=1, two=2, three=3)
d["four"] = 4
# del["four"] 

print(d)
del d["four"] 
print(d)


