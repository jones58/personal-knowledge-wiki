---
title: Python Notes
---

# Python notes

## Running Python Scripts

Can do `python... file_name.py` to run a file, or can open a REPL in the terminal by just writing `python...`
or can just click start button.

F5 to debug.

The `-i` flag means 'open a REPL that can use the code in this file' - e.g. `python -i 017_expressions.py` in the terminal, either iTerm or in VSCode Terminal

can exit REPL by writing `exit()` or using ctrl-d

indentation is important!

## F strings

e.g. `f"hello {name}"`
The python version of template literals in js.

## Type

The equivalent of typeof in python is type().

## New lines

\n - new line in python.

## Snake case

Python generally uses snake case for variables - e.g. `snake_case`

## Using Translation table

Have to set the translation table and then use the translate function

```python
my_string = "tamperlot"
translation_table = str.maketrans({'t': 'c', 'l': 'b'})
translated_string = my_string.translate(translation_table)
```

## Functions

Remember to write def when writing a function, e.g. `def my_function():` and have import modules at the top of the file, outside the main function. Use if**name**=="**main**": to run the function and not the contents of the import modules.

```python
def my_function():
    print("hello")
    print("how are you?")

if __name__ == "__main__":
    my_function()
```

## Comments

`#` is a comment in python
`"""` or `'''` is a multiline comment

## Single underscore

`_` is a single underscore and is used for private variables you don't care about in python.

## List comprehensions

Help make the code more efficient, with less syntax. Can mimic certain lambda functions, easier to read. - e.g.

```python
my_list = [x*x for x in range(10)]
```

instead of

```python
my_list = [] for i in range(1,11): my_list.append(x*x)`
```

can also use `if` in the list comprehension:

`list = [expression for item in iterable if conditional]`

as well as:

`list = [expression for item in iterable]`
`list = [expression if/else for item in iterable]`

NB the expression and everything has to be inside the [] for the list.

## all function

all() is a built-in Python function that returns True if all the elements inside a given iterable evaluate to True. Otherwise, it returns False.

Can be added to if statement to check if all elements in a list are true.

## Generator expression

```python
my_list = (x*x for x in range(10))
```

Just like list comprehension, but without square brackets. Can be faster, and uses less memory as it is not stored but deleted after use.

## Keyword arguments

These are used to pass arguments to functions. e.g. `my_function(1, 2, 3)`
becomes `my_function(a=1, b=2, c=3)`

- When you use keyword arguments, the order of the arguments does not matter.
- You can use default values if you don't want to pass an argument.
- You can use a mix of positional and keyword arguments.
- You can use just one keyword argument to pass the default value of other arguments.

## range function
NB range is a built-in function in python and can be used with for loops, e.g.
`for i in range(number_of_moves):`

## NB negation in python

In Python, the not keyword is used for negation, whereas ! is not a valid operator for negation in Python. Different to js. Nevertheless, not equal (!=) is still valid.

## NB

Have to write += because python prefers to be explicit and not use ++ .

use .extend() instead of += for lists

row_empty = row.replace('0', ' ')
replace (x, y) where x replaces y.

Inside the method, unpack the empty tuple into row and col.

row, col = empty

## Walrus operator

the walrus operator (:=), otherwise known as the assignment expression operator, combines the assignment and the conditional check into a single line, e.g.

```python
if (next_empty := self.find_empty_cell()) is None
```

## Classes

Define a class with the class keyword, e.g. `class MyClass:`

# Roadmap

Fill this in as learn: https://roadmap.sh/python

## Resources

Python documentation: https://docs.python.org/3/tutorial/datastructures.html

https://fireship.io/lessons/code-this-not-that-python-edition/
