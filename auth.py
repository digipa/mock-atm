# --- Welcome ---
# --- Register ---
# first name, last name, password, password match, email
# --- Generate Account Number ---

# --- Login ---
# account number, password
# --- Generate Account Number ---



# --- Other Improvements ---

# --- Welcome ---

allowedUsers = []
allowedPasswords = []

def welcome():
    print("Welcome to GCU Bank. %s" % x.strftime("%c"))
    haveAccount = int(input("Do you have an account with us? 1: yes 2: no \n"))

def register():
# --- Register ---
# first name, last name, password, password match, email

allowedUsers.append(input("Create a Username \n"))
allowedPasswords.append(input("Create a Password \n"))

def login():
# --- Login ---
# account number, password
# --- Generate Account Number ---

name = input("What is your Username? \n")
if name in allowedUsers:
    password = input("What is your Password \n")
    userId = allowedUsers.index(name)
    if password == allowedPasswords[userId]:
        print('Welcome %s' % name)
        option()
    else:
        print('Password Incorrect, please try again')
else:
    print('Name not found, please try again')
