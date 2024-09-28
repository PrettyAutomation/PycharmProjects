# Collections in python : Counter, namedtuple, OrderedDict, defaultDict and Deque
from collections import Counter
a = 'aaaaaaaabbbbbbcccc'
my_counter = Counter(a)

"""
below will return a dictionary object with key as the letter and value as the count of letter a
in given string
"""
print(my_counter)

# below will return all the different letters as elements of list
print(list(my_counter.elements()))

# below will return dict_items with key and value
print(my_counter.items())

# below will return the dict_keys(['a', 'b', 'c'])
print(my_counter.keys())

# below will return the dict_values([8, 6, 4])
print(my_counter.values())

# below will return most common letter with count [('a', 8)]
print(my_counter.most_common(1))
print(my_counter.most_common(2))
print(my_counter.most_common(3))

# below will return the first most common as list of tuple the with [0] first tuple then
# with [0] first element of tuple
print(my_counter.most_common(1)[0][0])







