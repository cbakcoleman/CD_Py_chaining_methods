# create USER class 
class User:
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = 0

    # DEPOSIT method
    def make_deposit(self, amount):
        self.balance += amount
        return self

    # WITHDRAW method
    def make_withdraw(self, amount):
        self.balance -= amount
        return self

    # DISPLAY balance method
    def display_user_balance(self):
        print(self.balance)
        return self

# create user 1 of 3
user1 = User("Buffy Summers", "bsummers@slayer.com", 0)
# user 1 of 3: 3xDEPOSIT, 1xWITHDRAW, DISPLAY through chaining
user1.make_deposit(20).make_deposit(10).make_deposit(30).make_withdraw(70).display_user_balance()

# create user 2 of 3
user2 = User("Zander Harris", "zharris@goodbowler.com", 20)
# user 2 of 3: 2xDEPOSIT, 2xWITHDRAW, DISPLAY through chaining
user2.make_deposit(40).make_deposit(40).make_withdraw(20).make_withdraw(20).display_user_balance()

# create user 3 of 3
user3 = User("Willow Rosenberg", "wrosen@raspberryhats.com", 50)
# user 3 of 3: 1xDEPOSIT, 3xWITHDRAW, DISPLAY through chaining
user3.make_deposit(100).make_withdraw(15).make_withdraw(30).make_withdraw(20).display_user_balance()
