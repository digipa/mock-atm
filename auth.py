# # # --- Welcome ---
import random
import datetime
import validation
import database
# from atmOptions import main_options
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
    
        user = database.authenticated_user(account_number_from_user, password)

        if user:
            auth_session_created = database.create_auth_session( account_number_from_user )
            main_options(user, account_number_from_user)
            
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
    
    is_user_created = database.create(account_number, first_name, last_name, email, password, str(0))

    if is_user_created:
        print('Your account number is: %d \n' % account_number)

        login()
    
    else:
        print("Something went wrong, please try again")
        register()

def generate_account_number():
    return random.randrange(1000000000, 9999999999)

def main_options( user_details, account_number_from_user ):

    print('Welcome %s %s' % (user_details[0], user_details[1]))

    selection = int(input('What would you like to do?: 1: Balance 2: Withdrawal 3: Cash Deposit 4: Complaint 5: Main Options 6: Logout 7: Exit \n'))

    if selection == 1:
        balance(user_details)
        main_options(user_details, account_number_from_user)

    elif selection == 2:
        withdrawal( user_details, account_number_from_user )
        main_options(user_details, account_number_from_user)

    elif selection == 3:
        deposit( user_details, account_number_from_user )
        main_options(user_details, account_number_from_user)

    elif selection == 4:
        complaint()
        main_options(user_details, account_number_from_user)

    elif selection == 5:
        main_options(user_details, account_number_from_user)
    
    elif selection == 6:
        logout(account_number_from_user)

    elif selection == 7:
        print('Thank you %s %s. We look forward to seeing you again.' % (user_details[0], user_details[1]))
        logout(account_number_from_user)
        exit()
    else:
        invalidOption()
        main_options(user_details, account_number_from_user)

def balance(user_details):
    get_current_balance(user_details)
    print('Your balance is %s.' % (user_details[4]))
    
def set_current_balance(user_details, balance):
    user_details[4] = balance

def get_current_balance(user_details):
    return user_details[4]

def withdrawal(user_details, account_number_from_user):
    amount_to_withdrawal = int(input('How much would you like to withdraw? \n'))
    current_user_balance = get_current_balance(user_details)
    updated_balance = int(current_user_balance) - amount_to_withdrawal

    set_current_balance(user_details, updated_balance)
    database.update_user_record( account_number_from_user, user_details )
    database.update_auth_session( account_number_from_user, user_details )
    print('Take your cash \n')

def deposit(user_details, account_number_from_user):
    amount_to_deposit = int(input('How much would you like to deposit? \n'))
    current_user_balance = get_current_balance(user_details)
    updated_balance = int(current_user_balance) + amount_to_deposit

    set_current_balance(user_details, updated_balance)
    database.update_user_record( account_number_from_user, user_details )
    database.update_auth_session( account_number_from_user, user_details )
    print('Your current balance is %s' % updated_balance)

def complaint():
    input('What issue will you like to report? \n')
    print('Thank you for contacting us')

def invalidOption():
    print('That is an invalid opti1on')
    main_options(user_details, account_number_from_user)

def logout(account_number_from_user ):
    database.delete(account_number_from_user)
    login()

welcome()