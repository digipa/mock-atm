# # # --- Welcome ---
import random
import datetime
from atmOptions import mainOptions

x = datetime.datetime.now()

# atmOptions.mainOptions

database = {}


def welcome():
    print("Welcome to GCU Bank. %s" % x.strftime("%c"))
    have_account = int(input("Do you have an account with us? 1: yes 2: no \n"))
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("Option invalid")
        welcome()

# # --- Login ---
# # account number, password
# # --- Generate Account Number ---

def login():
    print('LOGIN')
    account_number_check = int(input("What is your account number? \n"))
    password_check = input("What is your password \n")

    for account_number, userDetails in database.items():
        if account_number == account_number_check:
            if userDetails[3] == password_check:
                mainOptions(userDetails)
                
    print('Invalid account or password')
    register()


# # --- Register ---
# # first name, last name, password, password match, username, email

def register():
    print('REGISTER')
    first_name = input("First Name \n")
    last_name = input("Last Name \n")
    email = input("Email \n")
    password = input("Password \n")
    account_number = generate_account_number()
    database[account_number] = [ first_name, last_name, email, password]
    print('Your account number is: %d \n' % account_number)

    login()

def generate_account_number():
    return random.randrange(1000000000, 9999999999)

welcome()