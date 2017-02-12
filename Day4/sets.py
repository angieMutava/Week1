#challenge
'''
In the exercise below, use the given lists to print out a set 
containing all the participants from event A which did not attend event B.

a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]
'''
#solution
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print (a.difference(b))