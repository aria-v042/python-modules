> **[info]** *Work in progress...*

# Python Modules

Python Modules from [42](https://42.fr/)'s curriculum.

## Useful Resources

### Style guides

[PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/)

[PEP 20 – The Zen of Python](https://peps.python.org/pep-0020/)

### Python Module 00

[Python documentation >> The Python Tutorial](https://docs.python.org/3/tutorial/index.html)

### Python Module 01

[Python documentation >> Classes](https://docs.python.org/3/tutorial/classes.html)

[GeeksforGeeks: Python super()](https://www.geeksforgeeks.org/python/python-super/)

### Python Module 02

[Python documentation >> Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)

[Python documentation >> Built-in Exceptions](https://docs.python.org/3/builtins/exceptions.html#bltin-exceptions)

[Stack Overflow: Converting String to Int using try/except in Python](https://stackoverflow.com/questions/8075877/converting-string-to-int-using-try-except-in-python#comment118245688_8075959)

[Stack Overflow: How do I determine what type of exception occurred?](https://stackoverflow.com/a/9824050/32270021)

### Python Module 03

[Python documentation >> sys >> sys.argv](https://docs.python.org/3/library/sys.html#sys.argv)

[Python documentation >> Introduction >> Lists](https://docs.python.org/3/tutorial/introduction.html#lists)

[Python documentation >> Built-in Types >> Lists](https://docs.python.org/3/builtins/stdtypes.html#typesseq-list)

[Python documentation >> Data Structures >> More on Lists](https://docs.python.org/3/builtins/stdtypes.html#typesseq-list)

[GeeksforGeeks: Python Lists](https://www.geeksforgeeks.org/python/python-lists/)

Python list essentials:
```python
# Create an empty list
empty_list = []
empty_list = list()

# Create a list with items
my_list = [1]       # Single item
my_list = [0, 1, 2] # List with 3 items

# Create a list based on an existing iterable object (e.g. another list)
## Iterable can be a list, str, tuple, dict, etc...
my_iterable = [1, 2]
my_list = list(my_iterable) # [1,2]
## New list with each item of other list +1
my_iter_plus1 = [i+1 for i in my_iterable]  # [2, 3]
## New list from a string
abc_list = list("abc") # ['a', 'b', 'c']

# Access items from a list
my_list = [4, 6, 0, 2]
my_list[1] # 6 (the value in index 1)
## Negative numbers count from the end
my_list[-2] # 0 (value in 2nd to last index)

# Re-assign values in a list
my_list = [4, 6, 0, 1, 2]
my_list[2] = 1
my_list # [4, 6, 1, 1, 2]

# Slices of a list
my_list = [4, 6, 0, 1, 2]
my_list[:] # [4, 6, 0, 1, 2] --> whole list
my_list[2:] # [0, 1, 2] --> items starting from index 2
my_list[:2] # [4, 6] --> items up to index 2, not included
my_list[1:3] # [6, 0] --> items start at [1] and stop at [3] (not included)

# Slices return a copy of the list, not direct references to it
my_list = [6, 4, 2]
my_sliced_list = my_list[:] # [6, 4, 2] --> copies the whole list
my_sliced_list[0] = 0   # Re-assign value of index 0
my_sliced_list # [0, 4, 2] --> only changed the copy
my_list # [6, 4, 2] --> original list keeps original values
```
