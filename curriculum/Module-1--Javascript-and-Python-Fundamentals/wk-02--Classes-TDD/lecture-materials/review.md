# Reviewing Python Basics / Terminology
Below are some general beginner items to review for Python. 

General explanations of what things are as well as terminology that may be more helpful as you sharpen your skills at the language written as Python syntax using Docstrings and comments.

```python
""" This is a docstring, Python does not ignore them.
Depending on where you place one of these Python can bind it
to some part of your code.

For this docstring, Python will make it a module level docstring. Module being
the .py file this code would live in. .py files are called Modules. Docstrings
are helpful for documenting how your code works and then running a package
against your code that will actually auto-generate HTML/PDF documentation
for you!

Try using the help() function. It provides in console 
documentation which read the docstring of the str() class.

In a Python REPL:
>>> help(str)

Use 'q' to exit.
"""

# This is a single-line comment, Python ignores them.

# --- VARIABLES ---
# Python reads the thing to the RIGHT of the =
# and sets a named variable in memory to point at the value to the right.
my_name = 'Chris' # VALUE is: 'Chris', DATA TYPE is: String

# --- DATA TYPES ---
# String data type (strung together characters)
str_val = 'Chad'
# Integer data type (whole numbers)
num_val = 123
# Float data type (decimals, with limited precision)
float_val = 3.14
# Dictionary data type (collection of key/value pairs)
dict_val = {'name': 'Chris'}
# Set data type (collection of only unique keys)
set_val = {'Chris', 'Chad'}
# List data type (collection of values)
list_val = ['Chris', 'Chad'] # 1-dimension ( aka flattened List)
# Extra: List of Lists
list2_val = [['Chris'], ['Chad']] # 2-dimensions (nested List)

# --- FUNCTIONS ---
def say_hello(name):
    """Docstring belonging to this function.

    Functions are a way to write isolate extract 1 or more lines that 
    you have found useful that you might want to repeat again and again 
    though you just want to swap out 1 or more values.

    It lets you group lines you want to execute without having to rewrite/repeat 
    all those lines again each time you want to do it.
    """
    # Print is also a function, functions can CALL other functions.
    print("Hello, " + name) # prints to "standard out" aka your console
    # Functions ALWAYS return a value.
    # NOTE: if you DO NOT specify a return then one happens for you:
    # return None

# Invoked by writing: say_hello("Chris")

# Lambda function (anonymous function)
# I am assigning a lambda function to the variable name of "say_hello"
say_hello = lambda name: print("Hello, " + name)
# So Python stores the thing on right (function object) in the name say_hello.
# Because this my function object was given a name so I can use that name to call it.
# Making this line functionally equivalent to the function above.

# Invoked by writing: say_hello("Chris")

# --- CLASSES ---
# Classes ALWAYS inherit from Python base-class 'object'.
# which give it a bunch of dunder methods like def __str__, def __gt__, etc.
class Person:
    """Docstring that would describe the purpose of this class Person."""
    def __init__(self, name):
        # This is called init method also known as the "Initializer"
        # it lets you "initialize" any new Person object instance with
        # assigned attributes/values or run logic in the final steps of creating
        # this object.

        # assigning an "Instance attribute" to the Person object being constructed
        self.name = name

        # NOTE: When you do: person1 = Person("Chris") <- this is when __init__ runs.
    
    def say_name(self):
        # this is an Instance method. We can tell because it takes in self
        # as the first parameter in the method name.
        # NOTE: Although it looks like a function, we now call it a METHOD.
        # because this is a function that now BELONGS to a class Person.
        # Person class wraps around this function so it becomes METHOD.
        print("My name is: ", self.name)

# --- INSTANCE OBJECTS (instances of a Class) ---
# Creates a new Person object(instance) 
person1 = Person("Chad") # def __init__ runs passing in "Chad" as name

# Creates a new Person object(instance) 
person2 = Person("Chris") # def __init__ runs passing "Chris" as name

# These two instances are separate "containers" of information, they hold data
# inside them and exist apart from each other. Instance methods can do work 
# against themselves or do their work using their own data stored inside that 
# instance

# --- UNIT TEST SKELETON ---
# Bare minimum needed to setup Unit Testing.
import unittest

# Running multiple test cases is called a "running a Test Suite".

class NameOfMyTests(unittest.TestCase):
    """ A Test Case can test a module/feature of your code.
    It can contain multiple individual tests that individually test each part
    of your code like testing what SHOULD pass and what SHOULD fail.
    """

    def test_useful_name_here(self):
        """ Individual test, tests 1 part of your code.
        
        This could be testing a function that has a condition (IF) return.
        And it could test just the TRUTHY side of that return.
        """
        # In here you can prep arguments
        # test 1 part of a thing in here.
        self.assertEqual(1, 1) # make your assertion of what should have happened.
        # actually test something useful, like return value from function call.

    def test_another_name_here(self):
        # test 1 other part of a thing in here.
        self.assertNotEqual(2, 1)
        # actually test something useful, like return value from function call.

if __name__ == '__main__':
    # If this script is run via `python <test_scriptname>.py`
    # Then ask unittest to run main() -> run this TestCase class for us.
    unittest.main()

```

Here is a link to the [Python Unit Test documentation](https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug) for the chart showing some of the methods you can use to make your assertions such as `self.assertEqual()`. Any of these methods are accessible using `self.` as a prefix so `self.<method name>()`
