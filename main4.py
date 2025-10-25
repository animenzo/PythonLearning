# ----------data structures--------------

# 4 types of in built DS List, Tuple,Dictionary, Set



# mutable - value can be changed
# duplicates - can be duplicate values
# hetergenous - can contain different type of data types 
# ordered - can access values from indexes

# 1.List -  to store an ordered collection of items, it follows all 4 props

a = [1,2.4,True,print(),"apple"]

# print(a[1])
# slicing
# print(a[0:2])

# to access value 1st is using index
for i in range(len(a)):
    print(a[i])

# 2nd - directly on values but disadv is we cant write access

for i in a:
    print(i)

# method is a function defined in a class
# methods of list

# help(list)

# append - add a value in end of list
a.append(78)
print(a)

# insert - can add value in between list - we give index,value
a.insert(1,2)
print(a)

# remove - remove first occurence of value
a.remove()

# pop, sort ,copy...

