Wednesday, November 2, 2022
======================
### Video Resources from Previous Cohorts
- [Videos](https://www.youtube.com/channel/UCASZ7zW_Egu0T4KG3YEdGfw/playlists)

### Lecture Topics
- Constraint Satisfaction Problems

# Constraint Satisfaction Problems
One of the basic tasks of software engineers is looking for patterns, and then expressing those patterns in abstractions.  This basic process works at all levels, from designing builtins (what can't you use a `for` loop for?), to class hierarchies, to problem-solving.

One of these problem-solving abstractions is known as "constraint satisfaction."  [Here](https://web.stanford.edu/class/cs227/Lectures/lec14.pdf) is a more technical explanation of a constraint satisfaction problem (CSP).  For now, we'll strip it down as simply as possible and look at an example.

CSPs have three components:
1. Variables
2. Domains
3. Constraints

Variables are just the slots you are trying to fill.<br/>
Domains are all the possible values that a given variable might have.<br/>
Constraints are all of the rules that have to be satisfied in order to have a valid solution.

## Example
Let's say that we start out with a list of six zeros (Note: `0` here is just a placeholder):
```python
variables = [0,0,0,0,0,0]
```

We also have a range of values that any given slot in our list could possibly have:
```python
domain = [1,2,3,4,5,6,7,8,9]
```

Finally, we have a set of rules that we must follow (constraints):
1. Even indexes must have even integers.
2. No integer can occur more than once.


Let's try and come up with a solution on our own.  We start out with our variables:
```python
variables = [0,0,0,0,0,0]
```

Any given variable can take on a value in our domain, so an initial solution might look like this:
```python
variables = [1,4,6,3,9,4]
```

Now we have to check our initial solution against the constraints.  But before we do that, note that each of the two constraints is a little bit different.  The first one only cares about individual values.  We call that a "unary" constraint.  The second constraint cares about the wider context.  We call that a "higher-order" constraint.

Following our constraints, we see that our initial solution is invalid.  It actually violates both the unary constraint (9 should be an even number) and the higher-order constraint (4 occurs twice).

We can of course easily solve this problem as a human, but how could we tell a computer (way dumber) how to do it?

## A Possible Solution
Let's start by randomly guessing a number within our domain (1 through 9 inclusive).  We can immediately check if it satisfies the first constraint:
```python
random_guess1 = 4
current_idx = 0
variables = [0,0,0,0,0,0]

# if current_idx is even, check if random_guess1 is even
# if it is, then update variables

variables = [4,0,0,0,0,0]
```

We got lucky that time.  Let's continue
```python
random_guess2 = 9
current_idx = 1
variables = [4,0,0,0,0,0]

# since current_idx is odd, we've satisfied constraint 1
# update variables
variables = [4,9,0,0,0,0]
```

All right, we're on a roll!  But wait, aren't we forgetting about our second constraint?  We need to make sure our updated `variables` doesn't contain any duplicates (excluding the placeholder zeros, of course).  Let's redo that last step:

```python
random_guess2 = 9
current_idx = 1
variables = [4,0,0,0,0,0]

# since current_idx is odd, we're done
# update variables
variables = [4,9,0,0,0,0]

# check that variables contains no duplicates
# constraint satisfied
variables = [4,9,0,0,0,0]
```

Continuing on:
```python
random_guess3 = 3
current_idx = 2
variables = [4,9,0,0,0,0]

# constraint 1 fails...
# guess again
random_guess4 = 4
current_idx = 2
variables = [4,9,0,0,0,0]

# constraint 1 passes
# update variables
variables = [4,9,4,0,0,0]

# constraint 2 check
# constraint 2 fails...
```
So we recovered easily from the first failure, but what do we do now?  Depending on how our solution is implemented (we'll see that shortly), we might have just painted ourselves into a corner.  Something that seemed like a good solution initially might cause problems down the road.  In such cases it would be useful to somehow backtrack to where the problem started and try again.

## Backtracking
Backtracking is often a key part of CSPs.  Oftentimes you won't know if a given solution works until you get to the end.  How exactly you implement an "undo" is up to you and your application, but in our case, resetting the most recent guess to 0 and starting over should do the trick.  Sounds like a perfect opportunity for recursion.


## Implementation
```python
from random import randint

# unary constraint
def check_index(val, idx):
    if idx % 2 == 0:
        if val % 2 == 0:
            return True
        else:
            return False
    return True

# higher-order constraint
def check_reps(variables):
    non_zero = [v for v in variables if v != 0]
    return len(non_zero) == len(set(non_zero) )

def csp_list(variables, current_idx=0):
    domain = (1,9) # 1 through 9 inclusive
    if 0 not in variables:
        return variables
    else:
        guess = randint(*domain)
        if check_index(guess, current_idx):
            variables[current_idx] = guess
            current_idx += 1
            if not check_reps(variables):
                current_idx -= 1
                variables[current_idx] = 0
        return csp_list(variables, current_idx)

print(csp_list([0 for _ in range(6)]))
```
There are a number of things we could do to make this more efficient, but this is the basic idea.

If you try running this a bunch of times, you'll likely notice a problem on occasion.  What is causing it?  There seems to be another constraint implied, but not directly stated in the problem description.  If you were to add another constraint to fix this implementation, would it be unary or higher-order?  Why?


### Weeklong Group Project
* [Sudoku](https://github.com/deltaplatoonew/Sudoku)
