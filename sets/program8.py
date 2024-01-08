
# Return True if the set has no elements in common with other.
# Sets are disjoint if and only if their intersection is the empty set.

set1={1,4,3}
set2={1,2,4}
set3={0,6,5}

print(set1.isdisjoint(set2))
print(set1.isdisjoint(set3))



