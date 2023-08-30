Tuesday, October 11, 2022
=======================
### Video Resources from Previous Cohorts
- [Videos](https://www.youtube.com/channel/UCASZ7zW_Egu0T4KG3YEdGfw/playlists)

### Lecture Topics
- Python fundamentals (`for` loops and dictionaries)
- Introduction to classes in Python

## `for` Loops in Python
---
Once you understand that basic purpose of a `for` loop, a question still remains: What do I loop over?  In Python, there are a number of variations of `for` loops, and learning how to choose the best one for the task is an important skill.

Here are some basic cases:
```python
lst
range(num)
range(len(lst))
enumerate(lst)
```
#### `lst`
If you want to directly access every value in an iterable, then you can do that simply in Python.

##### Example:
```python
# print a greeting from each name in a list
lst = ["Bob", "Sally", "Frank"]
for name in lst:
  print(f"{name} says hi")
```

#### `range(num)`
If you know how many times you want to do something, then iterating over a `range` is the right tool.

##### Example:
```python
# print all integers from 0 to 10
for i in range(11):
  print(i)
```

#### `range(len(lst))`
If you want the index of each element in a list, then you can pass the length of the list to `range`.

##### Example:
```python
# Add a last name to everyone in a list of names
lst = ["Bob", "Sally", "Frank"]
for i in range(len(lst)):
  lst[i] = lst[i] + " Smith"
```

#### `enumerate(len(lst))`
`enumerate` is a little different because it returns a tuple instead of a single value.  The tuple has the form `(index, value)`.  You can use this for cases where you want to access both the index and value.

##### Example:
```python
# Add a last name to everyone in a list of names, but first check for the correct name
lst = ["Bob", "Sally", "Frank"]
for i, name in enumerate(lst):
  if name == "Frank":
    lst[i] = lst[i] + " Jones"
  else:
    lst[i] = lst[i] + " Smith"
```


## Dictionaries
---
In the examples above we were mostly using lists.  If you want to directly access a particular value in a list, you need to know it's index.  So in `lst = ["Bob", "Sally", "Frank"]`, Bob's index would be 0.  That is perfectly fine for many use-cases.  However, there are times when we want a more meaningful label for some particular piece of data in a collection.

Let's say that, instead of just a list of names, we want to have a more detailed representation of each person.  Bob might look like this:

```python
bob = {
  "name": "Bob",
  "age": 15,
  "hobbies": ["skiing", "falling", "getting up"]
}
```
Now, if we want to know something about Bob, we can use a meaningful name (key) to grab it.  Bob's name will be `bob["name"]`.  Makes sense.

Compare this to `bob` as a list:
```python
bob = ["Bob", 15, ["skiing", "falling", "getting up"]]
```
Bob-as-a-list and Bob-as-an-dictionary both contain the same information, but Bob-as-a-list just doesn't seem as easy to work with.  If I want Bob's name, I have to know that it is at the zeroth index: `bob[0]`.  Not as intuitive.

Learning how to choose the best data structure for the task at hand is an important skill.

## Combining Loops and Dictionaries
---
We can now combine what we know about `for` loops and dictionaries.  Let's start with three people: Bob, Sally, and Frank:

```python
bob = {
  "name": "Bob",
  "age": 15,
  "hobbies": ["skiing", "falling", "getting up"]
}

sally = {
  "name": "Sally",
  "age": 31,
  "hobbies": ["sailing", "swimming", "not drowning"]
}

frank = {
  "name": "Frank",
  "age": 85,
  "hobbies": ["tennis", "running", "grunting", "falling", "getting up"]
}

```

How would we get a greeting from each person?  We could start by putting each person in a list:

```python
people = [bob, sally, frank]
```

Then we would loop over the `people` list and access every person's name:

```python
for person in people:
    print(f'{person["name"]} says hi')
```




### Challenges
* [Reading Errors](https://github.com/deltaplatoonew/reading-errors)
* [Factorial](https://github.com/deltaplatoonew/factorial)
* [Linear Search](https://github.com/deltaplatoonew/linear-search)
* [Palindromes](https://github.com/deltaplatoonew/palindromes)

### Resources
* [Python Array Methods](https://www.programiz.com/python-programming/methods/list)
