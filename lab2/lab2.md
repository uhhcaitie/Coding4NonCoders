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
simply prints our `name` nicely.
