# What is the difference between list, tuples, and sets in Python?
 1. Lists and sets are mutable i.e they can be edited. Tuples are immutable (tuples are lists which can’t be edited).
 2. Lists and Tuples are ordered i.e. we can recall the order in which the elements were put in. Sets are unordered i.e. the order of elements is not constant. 
 3. List and tuples can contain duplicate elements. Sets automatically discard any duplicates.
 4. Lists are slower than tuples. Tuples are faster than list. Sets are especially fast at set operations (e.g. union, difference ...) and checking whether an element is contained in a set.
 5. Syntax: list_1 = [10, ‘Chelsea’, 20]. Syntax: tup_1 = (10, ‘Chelsea’ , 20). Syntax: set_1 = {10, ‘Chelsea’ , 20}

# What are the key features of Python?
1 .Python is an interpreted language. 
2 .Python is dynamically typed.
3 .Python can be used as object orientated programming.
4 .Python does not have access specifiers 

# What is pep 8?
PEP stands for Python Enhancement Proposal. It is a set of rules that specify how to format Python code for maximum readability.

# What sorting algorithm is used in Python's `sort()` and `sorted()` functions?
Python uses [Tim sort](https://en.wikipedia.org/wiki/Timsort)

# What is the difference between a generator and an iterator
Generator generates a new element each time that is required (e.g. each time the function is called). Iterator has all elements stored in advance. 

# What is a class static method ?
A class static method denoted @staticmethod is a method that is bound to a class instead of an object. A call to it could be done without an object

# What is a class class method ?
A class class method denoted @classmethod don't need a reference to an object as for @staticmethod. Class methods are tied to a class and have their importance in an inheritance context
