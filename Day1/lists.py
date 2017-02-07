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