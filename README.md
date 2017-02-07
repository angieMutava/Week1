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

### References.
```
https://docs.python.org/2/tutorial/datastructures.html
```
       


