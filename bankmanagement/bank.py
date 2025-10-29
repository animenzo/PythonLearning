import json
import random
import string
from pathlib import Path


class Bank:
    database = Path("F:/1placeprep/Python/bankmanagement/data.json")

    def __init__(self):
        # Load existing data or initialize empty
        if self.database.exists():
            try:
                with open(self.database, "r", encoding="utf-8") as fs:
                    self.data = json.load(fs)
            except json.JSONDecodeError:
                self.data = []
        else:
            self.data = []
            self.__update()

    def __update(self):
        with open(self.database, "w", encoding="utf-8") as fs:
            json.dump(self.data, fs, indent=4)

    def __accountgenerate(self):
        alpha = random.choices(string.ascii_uppercase, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        acc_id = alpha + num + spchar
        random.shuffle(acc_id)
        return "".join(acc_id)

    # ----------------- MAIN FUNCTIONS -----------------
    def create_account(self, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return False, "❌ Age must be ≥18 and PIN must be 4 digits."

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": self.__accountgenerate(),
            "balance": 0,
        }
        self.data.append(info)
        self.__update()
        return True, info

    def find_user(self, accnum, pin):
        for user in self.data:
            if user["accountNo"] == accnum and user["pin"] == pin:
                return user
        return None

    def deposit_money(self, accnum, pin, amount):
        user = self.find_user(accnum, pin)
        if not user:
            return False, "Account not found."
        if amount <= 0 or amount > 10000:
            return False, "Amount must be between 1 and 10,000."
        user["balance"] += amount
        self.__update()
        return True, f"Deposited ₹{amount} successfully!"

    def withdraw_money(self, accnum, pin, amount):
        user = self.find_user(accnum, pin)
        if not user:
            return False, "Account not found."
        if amount <= 0 or amount > user["balance"]:
            return False, "Insufficient balance or invalid amount."
        user["balance"] -= amount
        self.__update()
        return True, f"Withdrawn ₹{amount} successfully!"

    def show_details(self, accnum, pin):
        user = self.find_user(accnum, pin)
        if not user:
            return None, "Account not found."
        return user, "Account details fetched successfully."

    def update_details(self, accnum, pin, name=None, email=None, new_pin=None):
        user = self.find_user(accnum, pin)
        if not user:
            return False, "Account not found."

        if name:
            user["name"] = name
        if email:
            user["email"] = email
        if new_pin:
            if len(str(new_pin)) != 4:
                return False, "PIN must be 4 digits."
            user["pin"] = int(new_pin)

        self.__update()
        return True, "Account details updated successfully!"

    def delete_account(self, accnum, pin):
        user = self.find_user(accnum, pin)
        if not user:
            return False, "Account not found."
        self.data.remove(user)
        self.__update()
        return True, "Account deleted successfully!"
