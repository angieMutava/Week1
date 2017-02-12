# Week1
Learning DataStuctures to the core

###list.append(x)

    Add an item to the end of the list; equivalent to a[len(a):] = [x].


###list.extend(L)

    Extend the list by appending all the items in the given list; equivalent to a[len(a):] = L.

###  list.insert(i, x)

    Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x)

### list.remove(x)

    Remove the first item from the list whose value is x. It is an error if there is no such item.


### list.pop([i])

    Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

### list.index(x)

    Return the index in the list of the first item whose value is x. It is an error if there is no such item.

### list.count(x)

    Return the number of times x appears in the list.

### list.sort(cmp=None, key=None, reverse=False)

    Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

### list.reverse()

    Reverse the elements of the list, in place.

### List comprehension
List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.    
## Dictionaries
Items in dictionaries are accessed via keys and not via their position. A dictionary is an associative array (also known as hashes). Any key of the dictionary is associated (or mapped) to a value. The values of a dictionary can be any Python data type. So dictionaries are unordered key-value-pairs.

Dictionaries don't support the sequence operation of the sequence data types like strings, tuples and lists. Dictionaries belong to the built-in mapping type. They are the sole representative of this kind!

##Tuples
A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

Creating a tuple is as simple as putting different comma-separated values. Optionally you can put these comma-separated values between parentheses also.

###Indexing, Slicing, and Matrixes
Because tuples are sequences, indexing and slicing work the same way for tuples as they do for strings. Assuming following input.
```
L = ('spam', 'Spam', 'SPAM!')
```

Python Epression | Result | Description
--- | --- | ---
L[2]|'SPAM!'|Offsets start at zero
L[2]|'Spam'|Negative: count from the right
L[1:]|['Spam', 'SPAM!']|Slicing fetches sections

## No Enclosing Delimiters

Any set of multiple objects, comma-separated, written without identifying symbols, i.e., brackets for lists, parentheses for tuples, etc., default to tuples.

## Built-in Tuple Functions
Python includes the following tuple functions.<br/>
---
SN|Function with description
---|---
1|cmp(tuple1, tuple2).Compares elements of both tuples
2|len(tuple).Gives the total length of the tuple.
3|max(tuple).Returns item from the tuple with max value.
4|min(tuple).Returns item from the tuple with min value.
5|tuple(seq).Converts a list into tuple.

##Sets
Sets are lists with no duplicate entries.Sets are a powerful tool in Python since they have the ability to calculate differences and intersections between other sets.
To find out which members attended both events, you may use the "intersection" method:
```
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

set(['John'])
a.intersection(b)
set(['John'])
b.intersection(a)
set(['John'])

```
To find out which members attended only one of the events, use the "symmetric_difference" method:
```
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

a.symmetric_difference(b)
set(['Jill', 'Jake', 'Eric'])
b.symmetric_difference(a)
set(['Jill', 'Jake', 'Eric'])

```
To find out which members attended only one event and not the other, use the "difference" method:
```
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

a.difference(b)
set(['Jake', 'Eric'])
b.difference(a)
set(['Jill'])
```
To receive a list of all participants, use the "union" method:
```
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

a.union(b)
set(['Jill', 'Jake', 'John', 'Eric'])
```











### References.
```
https://docs.python.org/2/tutorial/datastructures.html
http://www.tutorialspoint.com/python/python_tuples.htm
```
       


