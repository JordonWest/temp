Saturday, October 29, 2022
=======================
### Video Resources from Previous Cohorts
- [Videos](https://www.youtube.com/channel/UCASZ7zW_Egu0T4KG3YEdGfw/playlists)

### Lecture Topics
- Currying
- Decorators
- Generators
- Debugging (Python's `embed`)


# Currying, Decorators, and Generators

## Currying
Currying is a Functional Programming technique that allows for reuse of a more general function.  It is a particular kind of "partial application."  Partial application is basically a way to pre-load some of a function's parameters.  Let's look at an example to make it clearer.

Let's say that we want to write a function that adds zero-padding to a number.  We could straightforwardly write a regular function:

```python
def pad(slots, num):
    diff = slots - len(str(num))
    return "0"*diff + str(num)
print(pad(3, 78))
# 078
```

But what if we find that our application almost always uses three places?  It might make our code easier to understand and maintain if we could somehow "subclass" the `pad` function to be `pad_3`. We can modify `pad` to enable this:

```python
def pad(slots):
    def inner(num):
        diff = slots - len(str(num))
        return "0"*diff + str(num)
    return inner
```

Now we can flexibly create as many "subclasses" as we like without changing `pad`:

```python
pad_3 = pad(3)
print(pad_3(78))
# 078

pad_5 = pad(5)
print(pad_5(789))
# 00789
```

## Decorators
Decorators are used when you want to apply a modification to several other functions.  Let's say you have an appliation that makes a bunch of financial transactions.  One of the functions interacts with the database to record sell requests.

```python
def sell(asset_id, value):
  # mock database call
  print("sell request recorded")
```

It might make sense to control how many times a given transaction could occur.  Let's say that we only want a given request to be made once.  We can create a decorator that "wraps" the `sell` function and modifies how it works without directly changing `sell`.

```python
def once(f):
    called = False
    def inner(*args):
        nonlocal called
        if not called:
            called = True
            return f(*args)
        raise Exception("Can only call once")
    return inner
```

Python provides convenient syntactic sugar for using decorators:

```python
@once
def sell(asset_id, value):
  # mock database call
  print("sell request recorded")
```

Now, if we try to call `sell` more than once, we will get an error:

```python
sell(9473, 23.45)
sell(6543, 12.34)
# sell request recorded
# Traceback (most recent call last):
#   File "/Users/codeplaton/Desktop/CodePlatoon/func2/decorator.py", line 18, in <module>
#     sell(6543, 12.34)
#   File "/Users/codeplaton/Desktop/CodePlatoon/func2/decorator.py", line 8, in inner
#     raise Exception("Can only call once")
# Exception: Can only call once
```

## Generators
Generators are everywhere in Python.  They are a specific kind of iterator.  Iterators allow you to sequentially get items from collections (iterables).

In order to create an iterable in Python, all we have to do is fulfill the API's requirements.  Iterables have to implement the `__iter__` dunder method, and `__iter__` has to return an iterator.

I've always found it a little bit annoying that you can't directly loop over an integer in python:

```python
for i in 9:
  print(i)
# throws an error
```

We can fix that and write an iterable integer:

```python
# is an iterable because it implements __iter__
class IterableInt:

    def __init__(self, num):
        self.num = num
        self.iterator = IntIterator(self.num)

    # returns an iterator
    def __iter__(self):
        return IntIterator(self.num)
```

OK, so what about that iterator?  Iterators have their own API.  Iterators need to implement the `__next__` dunder (and should also have their own `__iter__`, but that is not strictly necessary).

Let's create our integer iterator:

```python
class IntIterator:

    def __init__(self, num):
        self.str_num = str(num)
        self.current = 0

    def __next__(self):
        try:
            digit = self.str_num[self.current]
            self.current += 1
            return digit
        except:
            raise StopIteration()

    def __iter__(self):
        return self
```

The `__next__` dunder will return the value at the current index, or it will raise the standard `StopIteration` exception.

Now we can create an iterable integer and use it like a native Python object:

```python
it_num = IterableInteger(234)
for i in it_num:
  print(i)
```

Now that we know what iterables and iterators are, let's look at generators.  Generators are functions that `yield` instead of `return`.

Here is an implentation of an iterable integer using a generator:

```python
def iterable_num(num):
    num = str(num)
    for d in num:
        yield d

for i in iterable_num(234):
    print(i)
```


This allows us to get pieces of information one at a time, instead of all at once.  Why wouldn't we just want to get everything all at once?  Let's say you want to read the contents of a file, append every line to an array, and, loop over the array and do some processing, and finally save a new file.  What happens if that initial file is larger than your memory?

First we will mimic a very large file by creating an infinite number generator:

```python
from random import randint

def infinite():
    while True:
        yield str(randint(0,9))
```

If you loop over this, it will run forever:

```python
for n in infinite():
    print(n)
```

If we try to create a list from this generator, our computer will crash.

```python
# DON'T RUN THIS LOCALLY
# Try using replit.com
# x = [n for n in infinite()]
```

Instead of trying to get all the values at once, we should just ask for what we need, when we need it.  This is often called "lazy" evaluation.

```python
for n in infinite():
  n = n + "10"
  with open('x.txt', 'a') as f:
    f.write(n)
```

Now our computer's memory is no longer constraining the file size we can process.


## Debugging (Python's `ipdb`)
* Sometimes, you are running code and just want to pause in the middle of a loop and see what's going on around you. Up to this point, we haven't been able to do that, but with a Python library, we'll be able to stop our code at any point
* First, we install IPython: `pip install ipdb` and create our file we want to write out Python code in. Copy and paste the code below:
```python
import ipdb

def say_hello(first_name):
    ipdb.set_trace()
    print(f"Hello there, {first_name}!")

say_hello('Jon')
```
* If you run `python filename.py`, you will see:
```python
> /Users/jyoung/Desktop/delete.py(5)say_hello()
      4     ipdb.set_trace()
----> 5     print(f"Hello there, {first_name}!")
      6

ipdb>
```
At this point, you can view your variables, including `first_name`. The same can be done with loops:
```python
age = 12
while age < 21:
    ipdb.set_trace()
    print(f"You are not old enough yet - you are only {age} years old! Come back when you are older.")
    age += 1
```
* The code above will run and stop when it hits `ipdb.set_trace()`. You can see what `age` is. Ultimately, you want to use this when you hit issues and need help debugging your code. More information can be found on the [official docs](https://pypi.org/project/ipdb/) and via [this cheatsheet](https://wangchuan.github.io/coding/2017/07/12/ipdb-cheat-sheet.html).

### Challenges
* [Caesar Cipher](https://github.com/deltaplatoonew/caesar-cipher)
* [Pig Latin](https://github.com/deltaplatoonew/pig-latin)
* [Bubble Sort](https://github.com/deltaplatoonew/bubble-sort)
