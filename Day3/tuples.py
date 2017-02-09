tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"

# The empty tuple is written as two parentheses containing nothing
tup1 = ()
'''
To write a tuple containing a single value you have to include a comma, even though there is only one value

'''
tup1 = (50,)

# acccessing values in a tuple.
print "tup1[0]: ", tup1[0]
print "tup2[1:5]: ", tup2[1:5]

# updating values in a tuple
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print tup3


# deleting tuples
tup = ('physics', 'chemistry', 1997, 2000)

print tup
del tup
print "After deleting tup : "
print tup

print 'abc', -4.24e93, 18 + 6.6j, 'xyz'
x, y = 1, 2
print "Value of x , y : ", x, y