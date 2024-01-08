# ifference(*others)
# set - other - ...
# Return a new set with elements in the set that are not in the others.

set1={1,4,3}
set2={1,2,4}
set1.difference_update(set2)
print(set1)

print(set1.difference(set2))
