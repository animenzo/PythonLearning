
from pathlib import Path
import os
# rglob() - recursively reads all file in directory
def readfileandfolder():
    path  = Path('fileHandling')
    items = list(path.rglob("*"))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")


def createfile():
    try:
        readfileandfolder()
        name = input("please tell your file name: ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
             data = input("what u wnt to write in this file:- ")
             fs.write(data)

            print(f"File Created Successfully!")
        else:
            print(f"file already exists")
    except Exception as err:
        print(f"an error occured as {err}")

def readfile():
    try:
        readfileandfolder()
        name = input(f"which file you want to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
                print("Readed Successfully!")
        else:
            print("file does not exist")
    except Exception as err:
        print("error {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("tell which file you want to update?: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file: ")
            print("press 2 overwriting the data")
            print("press 3 for appending content")

            res = int(input("Tell me your response? "))
            if(res == 1):
                name2 = input("tell your new file name: ")
                p2 = Path(name2)
                p.rename(p2)
            
            if res == 2:
                with open(p,'w') as fs:
                    data = input("write here: ")
                    fs.write(data)
            if res == 3:
                with open(p,'a') as fs:
                    data = input("append here: ")
                    fs.write(" "+data)
    except Exception as err:
        print(f"an error {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("which file you want to delete? ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("file remocved succ")
        else:
            print("no file exist")
    except Exception as err:
        print(f"error {err}")



    
print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check = int(input("please tell your response: "))

if check ==1:
    createfile()
if check == 2:
    readfile()
if check == 3:
    updatefile()
if check == 4:
    deletefile()



