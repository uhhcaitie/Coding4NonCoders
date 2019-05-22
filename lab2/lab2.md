Lab 2
=======
## If you are viewing this file and have not installed Python, Git, or have an editor ready to go, then view this project's README.md or the prologue of Lab 1

# *Feel free to enrich this document with your answers, notes, and code. It's yours. You cloned it.*

### *How to view this file*

*This is a Markdown file denoted by its ".md" extension. It is used by programmers
as a way to store documentation in a Project. There is nothing special about 
this file as opposed to any other text file. They are both just text. 
Markdown files generally follow specific conventions, with symbols like 
"#" denoting headers, or an asterisk denoting a bullet point. 
Some editors and applications can render Markdown files to produce an 
enriched document. In VSCode this is done using Ctrl + K V. If you need help interacting 
with this file, ask!*

# First, let's go over the basics

## Creating a function

Functions are perhaps the most useful feature of Python. It allows a programmer to take advantage of things like [Abstraction](https://en.wikipedia.org/wiki/Abstraction_(computer_science)), [Code reuse](https://en.wikipedia.org/wiki/Code_reuse), Readability, and many other good things! Writing functions to perform specific duties is essential to maintaining large programs.

Python uses the special keyword `def` to indicate that a function is about to be declared. For example:

```python
def my_print():
    print('hello world')
```

Here, `def` is our special *function keyword*, `my_print` is the *function name*, and `()` is our *function arguments*
(there are none), and the colon "`:`" finishes the declaration. We then indent over and write our *function body* -- What we want it do when we **call** it.

## Calling a function

Functions are defined to be called later. We can call (execute, run, etc) our function by doing the following

```python
my_print()
```

That is, the function name `my_print` following by arguments "`()`". Again, this function has no arguments (we'll get there).

## Function arguments

Right. Arguments. We can pass variables into our functions to make them much more dynamic. Think of math functions like "f(x)", `x` is the argument to the function `f`, producing a value.

```python
def print_name(name):
    print('My name is', name)
```

Here, `name` is a single argument to the function `print_name`. The function 
simply prints our `name` nicely. Function arguments can be named anything you want.
Although, it's a good idea to name them with regards to their purpose.

If you want more than one argument, seperate them with commas:

```python
def print_lots(foo, bar):
    print(foo, bar)
```

# Exercise 1

1. Run `my_print.py` and observe 'Hello world' in your terminal

2. Add an argument to the `my_print` function to print our instead of 'hello world'

3. In `my_print.py` (or a new file), define a function that will allow you to print out the Country and Capital in the pattern "The Capital of `X` is `y`". For example if I supply your function with "Uruguay" and "Montevideo", then "The Capital of Uruguay is Montevideo" Should be printed.

4. Call this function with the arguments "Spain", and "Madrid", then with "United States" and "Washington DC"

5. Create a function called `area` that takes two arguments, `width` and `height`, and prints out the result of width x height. For example, if I passed in 5 and 4 to the `area` function, I should see 20 printed out.

# Return

Functions do not have to be restricted to just printing things out. They can return values to the caller too using the special keyword `return`. We can then store the output into variables for later use. For example:

```python
def format_name(first_name, last_name):
    return last_name + ', ' + first_name
```

This function formats a first name and last name. It will print out "Smith, John" when passed 
in "John" and "Smith". We can use this to format names easier.

```python
john = format_name("John", "Smith")
jane = format_name("Jane", "Doe")
joe = format_name("Joe", "Schmoe")
```

This way we do not need to rewrite the formatting operation everytime.

# Exercise 2

1. Modify the `format_name` function to return in the format of "[first] -- [last]". Run
`format_name` again. Observe how we only made the code modification in one place, but reaped the rewards everywhere it is called. This is essential!

# Loops

## TODO