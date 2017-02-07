lists = [1, 2, 3, 4, 5, 6, 7]
list2 = [5, 6, 8]

lists.append(10)
lists.extend(list2)
lists.remove(4)
lists.pop(5)
lists.index(1)
lists.count(2)
lists.reverse()

#List comprehension...
created_list = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
for item in created_list:
	print item

###Challenge
'''
Write a function that takes a list of strings an prints them, one per line, in a rectangular frame. For example the list ["Hello", "World", "in", "a", "frame"] gets printed as:

*********
* Hello *
* World *
* in    *
* a     *
* frame *
*********
'''

lists = ["Hello", "World", "in", "a", "frame"]
print("*******")
for item in lists:
  print('*'+ item, ''+'*' )
print("*******")

