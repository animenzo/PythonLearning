#if else
# a = 13
# if a > 10:
#     print("a is greater than 10")
# else:
#     print("a is 10 or less")

# money = int(input("give me money  "))
# if money == 10:
#     print(" i will eat chocolate")
# elif(money ==20):
#     print("i will eat ice-cream")
# elif(money >20):
#     print("i will eat burger")
# else:
#     print("i will eat nothing")

# a1 = input("enter first number: ")
# a2 = input("enter second number: ")

# if a1 > a2:
#     print(a1)
# else:
#     print(a2)

# gender = input("what is your gender: ")
# if(gender == "male"):
#     print("morning sir")
# elif(gender == "female"):
#     print("morning ma'am")

# a1 = int(input("enter a number: "))
# if(a1%2 == 0):
#     print("even number")
# else:
#     print("odd number")

# year = int(input("enter a year: "))
# if((year%400 == 0 and year%4 == 0 )or (year%100 != 0 and year%4 == 0 )):
#     print("leap year")
# else:
#     print("not a leap year")


#-----------loops----------------------

# range func - accepts three things start, stop ,steps
# a = range(1,20,2)#1,3,5,7...

# for i in a:
#     print(i)

# n = int(input("enter a number: "))

# for i in range (n,n*10+1,n):
#     print(i)


a = "piyush is a boy"
# print(len(a))

# break - else -----  

# for i in range(1,21):
#     if(i == 13):
#         print("break executed")
#         break
#     print(i)

# else:
#     print("break is not executed")

# Q. accept an int and print hell n times

# n = int(input("enter a number:"))
# for i in range(n):
#     print(f"{i}: hell")


# Q factorial of a number
# n = int(input("enter a number: "))
# fact = 1
# for i in range(1,n+1):
#     fact = fact*i

# print("factorial is ",fact)


# Q count char , digits,special char in a string

# a = input("enter a string: ")
# dig = 0
# char = 0
# spchar = 0

# for i in a:
#     if(i.isdigit()):
#         dig+=1
#     elif(i.isalpha()):
#         char+=1
#     else:
#         spchar+=1

# print(f"digits: {dig}, characters: {char}, special characters: {spchar}")

# to see methods of string
# print(dir(str))


# for i in range(2,11,1):
#     print(f"decimal equivalent of 1/{i} = {1/i}")



#-------------while loop---------

# Q. print reverse and check if it is pal

# n = int(input("Enter a number: "))
# copy = n
# reverse = 0
# while n>0:
#     reverse = reverse*10+n%10
#     n = n//10

# print(reverse)

# if(copy == reverse):
#     print("Palindromic")
# else:
#     print("not pal")


