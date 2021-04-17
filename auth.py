# # # --- Welcome ---
import random
import datetime
import validation
import database
from atmOptions import main_options
from getpass import getpass

x = datetime.datetime.now()

def welcome():
    print("Welcome to Global Citizens United Bank. %s" % x.strftime("%c"))

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
    
    account_number_from_user = input("What is your account number? \n")
    
    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")
    
        user = database.authenticated_user(account_number_from_user, password);

        if user:
            main_options(user)

        print('Invalid account or password')
        login()
    
    else:
        print("Account number invalid:  Check that the account number is ten digits and contains only numbers")


# # --- Register ---
# # first name, last name, password, password match, username, email

def register():

    print('REGISTER')
    
    first_name = input("First Name \n")
    
    last_name = input("Last Name \n")
    
    email = input("Email \n")
    
    password = getpass("Password \n")
    
    account_number = generate_account_number()
    
    is_user_created = database.create(account_number, first_name, last_name, email, password)
    
    if is_user_created:
        print('Your account number is: %d \n' % account_number)

        login()
    
    else:
        print("Something went wrong, please try again")
        register()

def generate_account_number():
    return random.randrange(1000000000, 9999999999)

welcome()