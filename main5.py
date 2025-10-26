# exception handling----------------

# errors - types - sytax , identation, tab error
# other than these errors are exceptions

# exception - unexpected event that disrupts normal flw of code

# exception handling - try, except, else findally raise
# try  - wrap the bloack of code that might cause an exptn
# except - handle the exception if it occurs
# else - run if no exptn
# finally - run code even if there is error or no error does not matter
# raise - throw an exptn manually

# try and except always come together in python
# others are not necessary
# a = int(input("tell number: "))
# try:
#     print(10/a)
# except ZeroDivisionError:
#     print("can not div by 0")
# some excpetion are - zero division error, traceback, ...

# print("done")

# a = int(input("tell number: "))
# try:
#     print(10/a)
# except Exception as error:
#     print(f"there is an error {error}")
# else:
#     print("no excption")

# print("done")

# age = int(input("tell age: "))

# try:
#     if age <10 or age >18:
#         raise ValueError("you age must be bet 10 and 18")
#     else:
#      print("welcom")
    
# except Exception as err:
#    print(f"an eror occured as{err}")

# print("lcub")



# ---------------file handling-----------
# open and fn - opens a file for us and read in terminal
# p = open("F:/1placeprep/Python/tempCodeRunnerFile.py")

# print(p.read())

# r =  open("ironman.txt","w")
# r =  open("ironman.txt","a")
# r =  open("ironman.txt","x")
# # x = creates a new file only
# # r.write("hello this is me the ironman making nanotech suit")
# r.write("so let do this")
# r.close()


