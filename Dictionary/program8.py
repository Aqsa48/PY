# Return a shallow copy of the dictionary.
import copy

d = dict(one=1, two=2, three=3)
e = copy.deepcopy(d)
print(e)

