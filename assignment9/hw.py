"""
Exercise-1: Find missing elements
Write a function "missing_elements(my_list: list) -> list" that takes a
sorted list of integers and returns a list of missing integers in the range of the list.

Example:
missing_elements([1, 2, 4, 6, 7]) -> [3, 5]
"""

def missing_elements(my_list: list) -> list:
    if not my_list:
        return []
    ex1_range = set(range(my_list[0], my_list[-1] + 1))
    return sorted(list(ex1_range - set(my_list)))

#print(missing_elements([1, 2, 4, 6, 7]))



"""
Exercise-2: Count occurrences
Write a function "count_occurrences(my_list: list) -> dict" that takes a
list of integers and returns a dictionary where keys are unique integers
from the list and values are their counts in the list.

Example:
count_occurrences([1, 2, 3, 1, 2, 4, 5, 4]) -> {1: 2, 2: 2, 3: 1, 4: 2, 5: 1}
"""

def count_occurrences(my_list: list) -> dict:
    ex2_inbox = {}
    for ex2_item in my_list:
        ex2_inbox[ex2_item] = ex2_inbox.get(ex2_item, 0) + 1
    return ex2_inbox

#print(count_occurrences([1, 2, 3, 1, 2, 4, 5, 4]))


"""
Exercise-4: Common elements
Write a function "common_elements(list1: list, list2: list) -> list" that takes two
lists of integers and returns a list of unique common elements.

Example:
common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) -> [3, 4, 5]
"""

def common_elements(list1: list, list2: list) -> list:
    ex2_unique = set(list1) & set(list2)
    return list(ex2_unique)

#print(common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))

"""
Exercise-5: Character frequency
Write a function "char_frequency(my_string: str) -> dict" that takes a
string and returns a dictionary with the frequency of each character in the string.

Example:
char_frequency('hello world') -> {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
"""

def char_frequency(my_string: str) -> dict:
    ex5_char_freq = {}
    for char in my_string:
        ex5_char_freq[char] = ex5_char_freq.get(char, 0) + 1
    return ex5_char_freq

#print(char_frequency('hello world'))

"""
Exercise-6: Unique words
Write a function "unique_words(my_string: str) -> int" that takes a
string and returns the number of unique words in the string.

Example:
unique_words('hello world hello') -> 2
"""

def unique_words(my_string: str) -> int:
    ex6_uniq_words = set(my_string.split())
    return len(ex6_uniq_words)

#print(unique_words('hello world hello'))

"""
Exercise-7: Word frequency
Write a function "word_frequency(my_string: str) -> dict" that takes a
string and returns a dictionary with the frequency of each word in the string.

Example:
word_frequency('hello world hello') -> {'hello': 2, 'world': 1}
"""

def word_frequency(my_string: str) -> dict:
    ex7_words_list = {}
    ex7_words = my_string.split()
    for words in ex7_words:
        ex7_words_list[words] = ex7_words_list.get(words, 0) + 1
    return ex7_words_list

#print(word_frequency('hello world hello world hello hello'))



"""
Exercise-8: Count elements in range
Write a function "count_in_range(my_list: list, start: int, end: int) -> int" that
takes a list of integers and two integers as range boundaries and
returns the count of unique elements within that range in the list.

Example:
count_in_range([1, 2, 3, 4, 5, 4, 3, 2, 1], 2, 4) -> 3
"""

def count_in_range(my_list: list, start: int, end: int) -> int:
    ex8_unique_elements_in_range = {ex8_item for ex8_item in my_list if start <= ex8_item <= end}
    return len(ex8_unique_elements_in_range)




#print(count_in_range([1, 2, 3, 4, 5, 4, 3, 2, 1], 2, 4))




"""
Exercise-9: Swap dictionary keys and values
Write a function "swap_dict(d: dict) -> dict" that takes a dictionary
and returns a new dictionary where keys become values and values become keys.
if you face duplicates, the first key should be saved.

Example:
swap_dict({1: 'a', 2: 'b', 3: 'c'}) -> {'a': 1, 'b': 2, 'c': 3}
"""

def swap_dict(d: dict) -> dict:
    ex9_list = {}

    for key, value in d.items():
        if value not in ex9_list:
            ex9_list[value] = key

    return ex9_list

#print(swap_dict({1: 'a', 2: 'b', 3: 'c'}))


"""
Exercise-10: Subset check
Write a function "is_subset(set1: set, set2: set) -> bool" that takes two
sets and returns True if set2 is a subset of set1, and False otherwise.

Example:
is_subset({1, 2, 3, 4, 5}, {3, 4, 5}) -> True
"""

def is_subset(set1: set, set2: set) -> bool:
    return set2.issubset(set1)

#print(is_subset({1, 2, 3, 4, 5}, {3, 4, 5}))

"""
Exercise-11: Intersection of lists
Write a function "list_intersection(list1: list, list2: list) -> list" that takes two
lists and returns a list of unique elements that are in both lists.

Example:
list_intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) -> [3, 4, 5]
"""

def list_intersection(list1: list, list2: list) -> list:
    ex11_intersection_set = set(list1) & set(list2)
    return list(ex11_intersection_set)


#print(list_intersection([1, 2, 3, 4, 5], [3, 4, 5]))


"""
Exercise-12: Union of lists
Write a function "list_union(list1: list, list2: list) -> list" that takes two
lists and returns a list of unique elements that are in either of the lists.

Example:
list_union([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]) -> [1, 2, 3, 4, 5, 6, 7]
"""

def list_union(list1: list, list2: list) -> list:
    ex12_union_list = set(list1) | set(list2)
    return list(ex12_union_list)

#print(list_union([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))

"""
Exercise-13: Most frequent element
Write a function "most_frequent(my_list: list) -> int" that takes a
list of integers and returns the most frequent element in the list.

Example:
most_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]) -> 1
"""

def most_frequent(my_list: list) -> int:
    ex13_list = {}
    for item in my_list:
        ex13_list[item] = ex13_list.get(item, 0) + 1
    ex13_list_items = max(ex13_list, key=ex13_list.get)

    return ex13_list_items

#print(most_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]))

"""
Exercise-14: Least frequent element
Write a function "least_frequent(my_list: list) -> int" that takes a
list of integers and returns the least frequent element in the list.

Example:
least_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]) -> 3
"""

def least_frequent(my_list: list) -> int:
    ex14_list = {}
    for item in my_list:
        ex14_list[item] = ex14_list.get(item, 0) + 1
    ex14_list_items = min(ex14_list, key=ex14_list.get)
    return ex14_list_items

#print(least_frequent([1, 2, 3, 1, 2, 4, 5, 4, 1]))

