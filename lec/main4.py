# ----------data structures--------------

# 4 types of in built DS List, Tuple,Dictionary, Set



# mutable - value can be changed
# duplicates - can be duplicate values
# hetergenous - can contain different type of data types 
# ordered - can access values from indexes

# 1.List -  to store an ordered collection of items, it follows all 4 props

# a = [1,2.4,True,print(),"apple"]

# print(a[1])
# slicing
# print(a[0:2])

# to access value 1st is using index
# for i in range(len(a)):
#     print(a[i])

# 2nd - directly on values but disadv is we cant write access

# for i in a:
#     print(i)

# # method is a function defined in a class
# # methods of list

# # help(list)

# # append - add a value in end of list
# a.append(78)
# print(a)

# # insert - can add value in between list - we give index,value
# a.insert(1,2)
# print(a)

# # remove - remove first occurence of value
# a.remove()

# pop, sort ,copy...

l = [12,23,34,45,128,6,57,13]

# greatest = l[0]
# for i in l:
#     if i>greatest:
#         greatest = i

# print(greatest)

# check if list is sorted or not
# for i in range(len(l)-1):
#     if(l[i]<l[i+1]):
#         continue
#     else:
#         print("not sorted")
#         break

# else:
#     print("list is sorted")


# -------------tuple---------------
# tuples are not mutable
# it can have duplicates
# are ordered and can acces by indexes
# have heterogenous - can contain multiple data type
# uses ()
# 
# a = (1,2,3,4)
# index  = a.index(3)
# count = a.count(3)
# print(index,count)

# spec power - tuple unpacking
# l,b,c,d = (10,2,30,4)
# print(l)

# a = (1)
# this above unpacks and type will become 'int'
# and if we dont want to unpack then do this
# a = (1,)


# ---------------set--------
# to store unique values
# are mutable
# cannot have duplicates
# are unordered and can not access them through index values
# is ssemi-hetergenous it can store some data types like string,numbers,tuples but not everything
s = {1,23,4,45}

# why unordered - due to hashing , each time hashing is different 
# can only traverse using for loop 

# set has methods which provides mutability
# like - add, remove(raises an error if value no found),discard(do not raises error), pop(removes random elem), clear(remove all elem)

# methods that can be performed on two sets
q = {1,5,7,83,2}
union = s.union(q)
uni  = s|q

intersec = s.intersection(q)
intersection = s&q

difference = s.difference(q)
diff = s - q

symmetric_difference = s.symmetric_difference(q)
sym_dif = s^q
# print(sym_dif)


# ---------dictionary------
# also hashmap or json
# stores key-value pairs in it
# are mutable, keys must be unique but values can be duplicates keys work as index here
# follows insertion order
# heterogenous
# can perform CRUD

d = {1:"hey",2:"lab"}

# print(d[1])
d.update({3:300})
# or can write directly d[50] = 100
# for deletion
# del d[2]
# print(d)
# traversing--- directly iterating - for keys

# for i in d:
#     print(i)
# for values
# for i in d.values():
#     print(i)
# dictionary methods ---  --

# deep copy - ek me copy kr rhe h toh dusre me bhi copy hoga

# a = [1,23,4,5]
# b = a
# b[0] = 100
# print(b)
# shallow copy - changes are not reflected in the first from which you r copied
# a me changes kiye toh b me changes nhi honge and b me changes kre toh woh a me reflect nhi honge

# a = [12,4,45,6]
# b = a.copy()
# b[0] = 100
# print(a)
# print(b)


# now it same thing applies to dictionary


# get method in dict - get value of key
# d2 = d.get(2)
# print(d2)

# print(d.items())

d1 = {1:"jing",2:"hel",3:"yel",4:"bhel"}
d2 = {10:99,20:29,30:23,40:34}

# q. merge two diction
# for i in d2:
#     d1[i] = d2[i]

# print(d1)

# count freq of list elemts
a = [1,2,1,1,2,3,3,4,4]
di = {}
for i in a:
    if i in di.keys():
        di[i] += 1
    else:
        di[i] =1

print(di)
