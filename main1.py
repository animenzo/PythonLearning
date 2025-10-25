# comments = use -> #
#  multiline = use -> """... """
#print("i am learning python") 

#variables
name = "piyush"
aA = 10 #camel case
SherKing = 12 #pascal case
j_k = 13 #snake case

#data types -1.Numbers =  int,float,complex - iota/imaginary value
# a = 10/3 #float
# complex = 3 + 5j #complex number
# print(type(a))
# print(type(complex))

#2.strings
st = "hello piyush"
# print(type(st))

#3.boolean - T and F should be capital
b = True
# print(type(b))

a1= "A"
# print(ord(a)) #ASCII or unicode value of A

a2=65
# print(chr(a)) #character of ASCII or unicode value 65

k1 = "piyush"
# print(k1[0]) #indexing
# print(k1[-1]) #negative indexing
# print(k1[0:4]) #slicing [start:end-1:steps]
# print(k1[0:6:2]) #slicing with step value
# print(k1[2::]) #slicing from index 2 to end
# print(k1[::-1]) #reversing a string

#type conversion - int(), str(),float() ,bool
#falsy value: 7 values = 0,false,0.0,"",[],(),{}
a = 12 #int
a = str(a) #converted to string
print(type(a)) 

a = 12/3 # will be implicit type conversion - python automaticlly converts int to float


#-----------input and output---------
#output

name = "piyush"
age = 20
#normal way to write
# print("my name is ",name,"and my age is ",age)
#formatted string - f is impt.
# print(f"my name is {name} and my age is {age}")

#input
# gender = input("what is your gender?  ")

# print(gender)

#types of operators

#7 types of arthmetic operators : +,-,*,/,%,//,**,=
# these follow BODMAS rule in python
#flow division operator - //
a = 10
b = 3
# print(a//b) #wil give the division in integer

#exponentiation operator - **
# print(2**3) #2 raised to power 3

#comparision operators : ==,!=,>,<,>=,<=
#gives boolean output

# print("ABC"> "ACD") #compares ASCII values of characters

#logical operators : and,or,not
# and - all conditions should be true
# or - any one condition should be true
# not - reverses the boolean value

# print(122 > 100 and 34==34)
# print(122 > 100 or 34!=34)
# print(not(34==34))

# print(True and bool(0))

#Q.Write a program to compute distance between two points taking input from the user

# x1 = float(input("enter point 1 : "))
# x2 = float(input("enter point 2 : "))
# distance = x2 - x1
# print(f"the distance between two points is {distance}")

#Q2.Write a program add.py that takes 2 numbers as command line arguments and prints its sum.

# x1 = float(input("enter number 1 : "))
# x2 = float(input("enter number 2 : "))
# addition = x2 + x1
# print(f"the sum of two number is {addition}")