import string
class BankUser:
    wrongpsw = 0
    def __init__(self, name, surname, age, number, sum, password):
        if not(name.isalpha() and surname.isalpha()):
            raise Exception("Wrong name or surname")
        if not (type(age) is int and age > 0):
            raise Exception("Wrong age")
        if len(number) != 16:
            for i in number.split(" "):
                if len(i) != 4:
                    raise Exception("Wrong account number")
        if sum < 0:
            raise Exception("Wrong cash amount")
        if len(password) < 8:
            raise Exception("Password must contain at least 8 sybols")
        self._name = name
        self._surname = surname
        self._age = age
        self.__number = number
        self.__sum = sum
        self.__password = password
    
    def info(self):
        if self.wrongpsw > 2:
            return "You can use only 'confirm' method"
        return f"name: {self._name}\nsurname: {self._surname}\nage: {self._age}"
    
    def balance(self, psw):
        if psw != self.__password:
            self.wrongpsw += 1
            if self.wrongpsw > 2:
                return "Too many tries. You need to confirm your account"
            return "Incorrect password"
    
        return f"acc. number: {self.__number}\nbalance: {self.__sum}"
            
    
    def add(self, cash):
        if self.wrongpsw > 2:
            return "Too many tries. You need to confirm your account"
        if cash < 0:
            print("Wrong cash amount")
        else:
            self.__sum += cash
    
    def withdraw(self, cash):
        if self.wrongpsw > 2:
            return "Too many tries. You need to confirm your account"
        if cash < 0 or cash > self.__sum:
            print("Wrong amount of withdrawing cash")
        else:
            self.__sum -= cash
    def confirm(self, name, surname, l4digit):
        if name == self._name and surname == self._surname and l4digit == self.__number[-4::]:
            self.wrongpsw = 0
            print("Your account is confirmed")


user1 = BankUser("Poxos", "Poxosyan", 32, "4355 0539 2662 8225", 32500, "12345678")
print(user1.info())
print(user1.balance("12345678"))
user1.add(5000)
print(user1.balance("12345678"))
user1.withdraw(3000)
print(user1.balance("1234568"))
print(user1.balance("1234568"))
print(user1.balance("1234568"))
user1.confirm("Poxos", "Poxosyan", "8225")
print(user1.balance("12345678"))

