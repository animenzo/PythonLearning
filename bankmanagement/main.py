import json
import random 
import string
from pathlib import Path


class Bank:
    database = 'F:/1placeprep/Python/bankmanagement/data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")
    except Exception as err:
        print(f"exception occured as {err}")
    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits,k=3)
        spchar = random.choices("!@#$%^&*",k=1)
        id = alpha + num +spchar
        random.shuffle(id)
        return "".join(id)



    def createaccount(self):
        info = {
            "name":input("tell your name: "),
            "age":int(input("tell us your age:  ")),
            "email":input("tell us your email: "),
            "pin":int(input("tell your pin: ")),
            "accountNo.":Bank.__accountgenerate(),
            "balance":0
        }

        if(info['age']<18 or len(str(info['pin']))!=4):
            print("sorry you can not create you account")
        else:
            print("account has been created successfully")
            for i in info:
                print(f"{i}: {info[i]}")
            print("please note down you account number")
            Bank.data.append(info)
            Bank.__update()

    def depositmoney(self):
        accnum = input("please tell your account number: ")
        pin = int(input("please tell your pin number: "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("sorry no data found")
        else:
            amount =int(input("how much you want to deposit: "))
            if amount>10000 or amount<1:
                print("sorry amount is too much you can deposit below 10000")
            else:
                    
                    if len(userdata) > 0:
                        userdata[0]['balance'] += amount
                        Bank.__update()
                        print("Amount deposited!")
                    else:
                         print("No user data found!")

    def withdrawmoney(self):
        accnum = input("please tell your account number: ")
        pin = int(input("please tell your pin number: "))
        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("sorry no data found")
        else:
            amount =int(input("how much you want to withdraw: "))
            if userdata[0]['balance']<amount or amount<1:
                print("sorry you dont have that much money")
            else:
                    
                    if len(userdata) > 0:
                        userdata[0]['balance'] -= amount
                        Bank.__update()
                        print("Amount withdrew!")
                    else:
                         print("No user data found!")


    def showdetails(self):
        accnum = input("please tell your account number: ")
        pin = int(input("please tell your pin number: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]

        print("your information is \n")

        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")


    def updatedetails(self):
        accnum = input("please tell your account number: ")
        pin = int(input("please tell your pin number: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("No such user found")
        else:
            print("you can only change name, email and pin")
            print("Fill the details or leave it empty")

            newdata = {
                "name":input("tell new name or press enter: "),
                "email":input("enter your new email or press enter to skip: "),
                "pin":input("enter new pin or press enter to skip: ")
                
            }
            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]["pin"]

            newdata['age'] = userdata[0]['age']
            newdata['accountNo.'] = userdata[0]['accountNo.']
            newdata['balance'] = userdata[0]['balance']

            if type(newdata['pin'])== str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("Updated successfully!")

        
    def delete(self):
        accnum = input("please tell your account number: ")
        pin = int(input("please tell your pin number: "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("No user found")
        else:
            check = input("Press y to if want to delete or n if not: ")
            if check == 'n' or check == 'N':
                print("Bypassed")
            else:
                index  = Bank.data.index(userdata[0])
                Bank.data.pop(index)

                print("Account delete success")
                Bank.__update()


user = Bank()

print("1.create an account")
print("2. deposit money in account")
print("3. withdraw money")
print("4. Know your Bank Details")
print("5. Update Details")
print("6. Delete account")

check = int(input("tell you response: "))

if check ==1:
    user.createaccount()


if check ==2:
    user.depositmoney()


if check ==3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.delete()