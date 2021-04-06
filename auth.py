# # # --- Welcome ---
# import random
# import datetime

# x = datetime.datetime.now()

database = {}

allowedUsers = []
allowedPasswords = []
firstName = []
lastName = []
email = []

# # --- Login ---
# # account number, password
# # --- Generate Account Number ---

def login():
    print('Login')
    username = raw_input("Username: \n")
    if name in allowedUsers:
        password = raw_input("Password: \n")
        userId = allowedUsers.index(name)
        if password == allowedPasswords[userId]:
            print('Welcome %s' % name)
        else:
            print('Password Incorrect, please try again')
    else:
        print('Name not found, please try again')
login()

def register():
    firstName.append(raw_input("First Name \n"))
    lastName.append(raw_input("Last Name \n"))
    allowedUsers.append(raw_input("Username \n"))
    email.append(raw_input("Email \n"))
    password = raw_input("Password \n")
# set allowedPasswords to match the second password raw_input
    checkPassword = raw_input("Password \n")
    if checkPassword == password:
        allowedPasswords.append(checkPassword)
    else:
        print('Passwords do not match')
    login()
register()

# def welcome():
#     print("Welcome to GCU Bank. %s" % x.strftime("%c"))
#     haveAccount = int(raw_input("Do you have an account with us? 1: yes 2: no \n"))
#     if haveAccount == 1:
#         login()
#     elif haveAccount == 2:
#         register()
#     else:
#         print("Option invalid")
#         welcome()
# welcome()



# accountNumber = generateAccountNumber()

# database[accountNumber] = [ firstName, lastName, email, password ]

# # --- Register ---
# # first name, last name, password, password match, email


# def generateAccountNumber():
#     return random.randrange(1000000000, 9999999999)