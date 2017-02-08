w = {"house":"Haus","cat":"Katze","red":"rot"}

 #to a access all the keys
 for keys in w.keys():
     print keys

 #alternatively values can be obtained in
 for keys in w.keys():
     print w[keys]   

#to access all the values in the dictionary
for values in w.values():
    print values

#to access key value pairs
for key, value in w.items():
    print "{}  {}".format(key, value)

#challenge
''' Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
'''
d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

def mydict(d1, d2):
  new_dictionary = {}
  for keys in d1.keys():
    for key in d2.keys():
      if keys == key:
        new_dictionary[key] = d1[keys] + d2[key]
  return new_dictionary 
 
print(mydict(d1, d2))  