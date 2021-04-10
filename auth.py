# # # --- Welcome ---
import random
import datetime
from atmOptions import mainOptions

x = datetime.datetime.now()

# atmOptions.mainOptions

database = {}

# def generateAccountNumber():
#     return random.randrange(1000000000, 9999999999)

def welcome():
    print("Welcome to GCU Bank. %s" % x.strftime("%c"))
    haveAccount = int(input("Do you have an account with us? 1: yes 2: no \n"))
    if haveAccount == 1:
        login()
    elif haveAccount == 2:
        register()
    else:
        print("Option invalid")
        welcome()

# # --- Login ---
# # account number, password
# # --- Generate Account Number ---

def login():
    print('LOGIN')
    accountNumberCheck = int(input("What is your account number? \n"))
    passwordCheck = raw_input("What is your password \n")

    for accountNumber, userDetails in database.items():
        if accountNumber == accountNumberCheck:
            if userDetails[3] == passwordCheck:
                mainOptions(userDetails)
                
    print('Invalid account or password')
    register()


# # --- Register ---
# # first name, last name, password, password match, email

def register():
    print('REGISTER')
    firstName = raw_input("First Name \n")
    lastName = raw_input("Last Name \n")
    # user = input("Username \n")
    email = raw_input("Email \n")
    password = raw_input("Password \n")
    passwordCheck = raw_input("Re-enter password \n")
    accountNumber = generateAccountNumber()
    database[accountNumber] = [ firstName, lastName, email, password]
    print('Your account number is: %d \n' % accountNumber)

    login()

def generateAccountNumber():
    return random.randrange(1000000000, 9999999999)

welcome()