
class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        # Checks if new_name is between 2 and 10 characters
        if len(new_name) >= 2 and len(new_name) <= 10:
            # Checks that new_name is different than existing name
            if self.name != new_name:
                # checks new_name doesn't contain spaces
                if (" " not in new_name):
                    print(self.name, "is now updated to", new_name)
                    self.name = new_name
                else:
                    print("New Username can't contain spaces")
            else:
                print("You must input a new name")
        else:
            print("New name must be between 2 and 10 characters ")

    def change_pin(self, new_pin):
        # checks that new pin is 4 characters
        if len(new_pin) == 4:
            # checks new pin doesn't contain spaces
            if (" " not in new_pin):
                # checks new pin is not the same as the old one
                if self.pin != new_pin:
                    # checks that new_pin is a number
                    if isinstance(new_pin, int):
                        self.pin = new_pin
                    else:
                        print("New Pin must be a number")
                else:
                    print("The new pin can't be the same as the old one")
            else:
                print("Spaces can't be included in Pin")
        else:
            print("New Pin must be 4 Numbers")

    def change_password(self, new_password):
        # checks that new password is greater than 5 characters
        if len(new_password) >= 5:
            # checks the new password doesn't contain spaces
            if (" " not in new_password):
                # checks that new password isn't the same as the old one
                if self.password != new_password:
                    self.password = new_password
                else:
                    print("The new password can't be the same as the old one")
            else:
                print("Password cant contain spaces")
        else:
            print("New Password must be greater than 5 characters")

# Subclass of User


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0
        self.on_hold = False

    # Flips the on_hold vairable to False if currently True
    # or to True if currently False
    def change_on_hold_status(self):
        if self.on_hold == True:
            self.on_hold = False
        elif self.on_hold == False:
            self.on_hold = True

    # Displays current balance
    def show_balance(self):
        print(self.name, "has an account balance of: ",
              # Displays self.balance as a string with 2 decimal points
              "{:.2f}".format(self.balance))

    # Decreases inputed amount from balance
    def withdraw(self, withdraw_amt):
        # checks to make sure account is not on hold
        if self.on_hold == False:
            self.balance -= withdraw_amt
        else:
            print("Transaction Canceled: Your account is on hold")

    # Increases inputed amount from balance
    def deposit(self, desposit_amt):
        # checks to make sure account is not on hold
        if self.on_hold == False:
            self.balance += desposit_amt
        else:
            print("Transaction Canceled: Your account is on hold")

    # 'User to send' is another instance of the BankUser class
    # Reduces balance of current user by transfer amount and increases
    # User to send's balance
    def transfer_money(self, user_to_send, transfer_amt, ):
        print(self.on_hold)
        # checks to make sure account is not on hold
        if self.on_hold == False and user_to_send.on_hold == False:
            print("You are transfering", transfer_amt, "to", user_to_send.name)
            # validate self.balance is greater than or equal to transfer amount
            if transfer_amt < self.balance:
                print("Authentication required")
                pin = int(input("Enter your Pin: "))
                # validates transferers pin in order to complete transfer
                print("Tranfer amoutn less than balance")
                if pin == self.pin:
                    print("Transfer Authorized")
                    self.withdraw(transfer_amt)
                    user_to_send.deposit(transfer_amt)
                    return True
                else:
                    print("Invalid Pin. Transaction Canceled")
                    return False
            else:
                print("Transfer Amount Exceeds current balance")
        else:
            print("Transaction Canceled: Your account is on hold")

    # 'User to request' is another instance of the BankUser class
    # Reduces balance of user_to_request by requested amount and increases
    # current user's balance
    def request_money(self, user_to_request, request_amt):
        # checks to make sure account is not on hold
        if self.on_hold == False and user_to_request.on_hold == False:
            print("You are requesting", request_amt,
                  "from", user_to_request.name)
            # validate end user's balance is greater than or equal to request amount
            if user_to_request.balance > request_amt:
                print("User authentication is reqiured...")
                user_pin = int(
                    input("Enter " + user_to_request.name + "'s Pin: "))
                # validates current user has the correct pin of user_to_request
                if user_pin == user_to_request.pin:
                    user_password = input("Enter your password: ")
                    # validates current user password
                    if user_password == self.password:
                        print("Request Authorized")
                        user_to_request.withdraw(request_amt)
                        print(user_to_request.name +
                              " sent $" + str(request_amt))
                        self.deposit(request_amt)
                    else:
                        print("Invalid Password. Transaction canceled")
                        return False
                else:
                    print("Invalid User Pin. Transaction canceled")
                    return False
            else:
                print("Requested amount exceeds balance")
        else:
            print("Transaction Canceled: Your account is on hold")


def is_valid_amt(amt):
    try:
        float(amt)
        if float(amt) <= 0:
            print("You must input a positive number")
            return 0
        else:
            return 1
    except ValueError:
        print("You must input a positive number")
        return 0


#  """ Driver Code for Task 1 """
user1 = User("Bob", 1234, "pass")

# print(user1.name, user1.pin, user1.password)

#  """ Driver Code for Task 2 """
# user1 = User("Bob", 1234, "pass")
# # print(user1.name, user1.pin, user1.password)

# user1.change_name("Bob")
# user1.change_pin("4322")
# user1.change_password("new_pass")
# print(user1.name, user1.pin, user1.password)

# """ Driver Code for Task 3"""

# user1 = BankUser("Barry", 1212, "pass")
# print(user1.on_hold)
# print("On hold flip")
# user1.change_on_hold_status()
# print(user1.on_hold)

# print(user1.name, user1.pin, user1.password, user1.balance)

# """ Driver Code for Task 4"""
# user1 = BankUser("Barry", 1212, "pass")
# print(user1.name, user1.pin, user1.password, user1.balance)
# user1.show_balance()
# user1.deposit(100)
# user1.show_balance()
# user1.withdraw(50)
# user1.show_balance()
# """ Driver Code for Task 5"""
alice = BankUser("Alice", 1234, "pass1234")
bob = BankUser("Bob", 4321, "pass4321")


alice.deposit(5000)
alice.show_balance()
bob.show_balance()

print("\n")

transfer_successful = alice.transfer_money(bob, 500)
alice.show_balance()
bob.show_balance()

if transfer_successful:
    print("\n")
    bob.request_money(alice, 100)
    alice.show_balance()
    bob.show_balance()
