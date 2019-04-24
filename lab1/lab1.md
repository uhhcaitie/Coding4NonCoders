Lab 1
=======

### *How to view this file*

*This is a Markdown file denoted by its ".md" extension. It is used by programmers
as a way to store documentation in a Project. There is nothing special about 
this file as opposed to any other text file. They are both just text. 
Markdown files generally follow specific conventions, with symbols like 
"#" denoting headers, or an asterisk denoting a bullet point. 
Some editors and applications can render Markdown files to produce an 
enriched document. In VSCode this is done using Ctrl + K V. If you need help viewing this file, ask!*

# Setting Up
## Git
Git is a popular Version Control System used. Version Control Systems are 
programs that help us maintain a history and track changes to a project over time.
Git is your friend and you should keep it close by. It can be used through its Command Line Interface using a Terminal like "CMD", or through a graphical application (GUI). Either works. I highly suggest familiarizing yourself with how to
use Git, especially the basic concepts of Cloning, Adding, Committing, and Pushing changes.

* [Git Basics](https://git-scm.com/book/en/v1/Getting-Started-Git-Basics)

### [Download Git here](https://git-scm.com/downloads)

If you are reading this file you have probably already cloned this repository.

## Python

Install [Python](https://www.python.org/downloads/release/python-372/)

* If you are on Windows, select the 64 bit installer
* If you are Max OS X, select the Mac installer

## Editor

Make sure you have your favorite text editor or IDE open and ready. See the file 
`README.md` at the root of this repository for some popular ones. If you are not using VS Code, 
make sure you have a terminal like CMD or Mac Terminal available. If you are
using VS Code, toggle the terminal using Ctrl + `.
Make sure you have line numbers enabled.

# Exercise 1

Run printing.py by calling the python interpreter on your `printing.py` file.

```shell
$ cd kickoff
$ python printing.py
```

1. Add another print statement after line 5 to print your name.
2. Fix the spelling of "Montevideo" on line 7. Run printing.py again. What happens?
3. Try printing 3 things at once

# Exercise 2
Let's talk variables. Most of the time, what you need to print out to the user
is not constant. It changes over the course of the programs execution. We can use
variables, defined by the `=` (equals) symbol, to store data in order to reference it later.
The `=` symbol can also reassign variables to new values.

Example:

```python
first = 'John'
```

`first` is the name of the variable.

`=` is the assignment operator.

`'john'` is now the value of the variable.


Open `variables.py` to see how variables are assigned to numbers
and strings. Run `variables.py` to see what prints out.

```shell
$ python variables.py
```

1. Answer the question below using the following code block

```python
romance = 'Casablanca'
action = 'The Terminator'
favorite = 'My favorite movie is '

bob = favorite + romance
alice = favorite + action

foo = bob + alice

print(foo)
```
Without checking first. what will foo print out?

2. Calculate the amount of seconds in a year using Python. Print it out.

3. What happens when you try to use a number as a variable name?

```python
1 = 'House'
```

4. What will the following code print out?

```python
A = 'zebra'
B = 'Bear'

A = B
print(A)
```

# Exercise 3

Conditionals are special constructs that allow the programmer to make decisions.
In Python, the following words are *special* and cannot be used as variable names.
They are used for conditional logic.

* if
* elif
* else

This is not an exhaustive list of all of the keywords, but three very commons ones.

Another useful operator is the `==` (equals-equals) symbol. It is used for
comparisons. It will evaluate to `True` or `False`.

```python
10 == 10 # True
5 == 'Car' # False
'bob' == 'bob' # True
3*3 == 9 # True
```

1. Without running it first, what will the `conditionals.py` program print out?

2. What happens if you change line 8 so that `my_color` is assigned to `red`

3. What does `else` do?

4. What will the following print out?

note: `>` means `Greater than` and `<` is `Less than`

```python
height = 6
if height > 10: 
    print('foo')
elif height < 8:
    print('bar')
else:
    print('baz')
```

3. Whats the difference between `else` and `elif`?

# Bonus

What does the following segment of code print out?

```python
nails = 20
wood_planks = 10
hammer = True

day = 'Monday'

if nails > 10:

    weekday = day != 'Saturday' and day != 'Sunday'

    if not weekday:
        print('The largest building is in Dubai.')
    elif day == 'Wednesday':
        print('James Madison was born on March 16.')
    elif wood_planks >= 10:
        print('Snails can sleep for three years.')

else:
    print('Git and Github are not the same thing.')
```