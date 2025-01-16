lst1 = [12,34,423,5,54,5,45,346,54]
lst2 = [234,45,6,7,8,67,86,79,678,34,5435]
from itertools import zip_longest
prit= zip_longest(lst1,lst2)
print(list(prit))