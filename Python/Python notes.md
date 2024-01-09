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

# Roadmap

Fill this in as learn: https://roadmap.sh/python

## Resources

Python documentation: https://docs.python.org/3/tutorial/datastructures.html

https://fireship.io/lessons/code-this-not-that-python-edition/
