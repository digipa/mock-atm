# --- Welcome ---
# --- Register ---
# first name, last name, password, password match, email
# --- Generate Account Number ---

# --- Login ---
# account number, password
# --- Generate Account Number ---



# --- Other Improvements ---

# --- Welcome ---
import random

database = {}

allowedUsers = []
allowedPasswords = []
firstName = []
lastName = []
email = []

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


# --- Login ---
# account number, password
# --- Generate Account Number ---

def login():
    print('Login')
    name = input("Username: \n")
    if name in allowedUsers:
        password = input("Password: \n")
        userId = allowedUsers.index(name)
        if password == allowedPasswords[userId]:
            print('Welcome %s' % name)
            # option()
        else:
            print('Password Incorrect, please try again')
    else:
        print('Name not found, please try again')

    accountNumber = generateAccountNumber()

    database[accountNumber] = [ firstName, lastName, email, password ]


# --- Register ---
# first name, last name, password, password match, email

def register():
    firstName.append(input("First Name \n"))
    lastName.append(input("Last Name \n"))
    allowedUsers.append(input("Username \n"))
    email.append(input("Email \n"))
    createdPassword = allowedPasswords.append(input("Password \n"))
# set allowedPasswords to match the second password input
    checkPassword = allowedPasswords.append(input("Password \n"))
    if checkPassword == createdPassword:
        print('Passwords match')
    else:
        print('Passwords do not match')
        # register()
    login()
    

def generateAccountNumber():
    return random.randrange(1000000000, 9999999999)