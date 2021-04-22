#CRUD Records

import os
import validation

user_db_path = "data/user_record/"
auth_session_path = "data/auth_session/"

# --------------------------------------------------- C R E A T E ------------------------------------------------------

def create( user_account_number, first_name, last_name, email, password, account_balance ):
# add does_email_exist, does_account_number_exist
# add a try except block which contains read, and delete functions

    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)

    if does_account_number_exist(user_account_number):
        
        return False
    
    if does_email_exist(email):
        print("User already exists")
        return False
    
    completion_state = False

    try:
        f = open(user_db_path + str(user_account_number) + ".txt", "x")
    
    except FileExistsError:

        does_file_contain_data = read(user_db_path + str(user_account_number) + ".txt")

        if not does_file_contain_data:
            delete(user_account_number)
        
    else:

        f.write(str(user_data));
        completion_state = True

    finally:

        f.close();
        return completion_state

# --------------------------------------- C R E A T E   A U T H   S E S S I O N ---------------------------------------

def create_auth_session( user_account_number ):

        duplicated_user_record_file = open(user_db_path + str(user_account_number) + ".txt").read()
        f = open(auth_session_path + str(user_account_number) + ".txt", "x")
        f.write(str(duplicated_user_record_file));

# ----------------------------------------------------- R E A D --------------------------------------------------------

def read(user_account_number):
    is_valid_account_number = validation.account_number_validation(user_account_number)

    try:
        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")

        else:
            f = open(user_db_path + user_account_number, "r")

    except FileNotFoundError:
        print("User not found")

    except FileExistsError:
        print("User does not exist")

    except TypeError:
        print("Invalid account number format")

    else:
        return f.readline()

    return False


# ------------------------------------- U P D A T E   U S E R   R E C O R D --------------------------------------------

def update_user_record( user_account_number, user ):
    print("Update user record")
    current_balance = user[4]
    
    updated_user = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(user[4])

    f = open(user_db_path + str(user_account_number) + ".txt", "w")
    f.write(updated_user)
    f.close()


# -------------------------------------- U P D A T E   A U T H   S E S S I O N  -----------------------------------------

def update_auth_session( user_account_number, user ):
    print("Update user record")
    current_balance = user[4]
    
    updated_user = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(user[4])

    f = open(auth_session_path + str(user_account_number) + ".txt", "w")
    f.write(updated_user)
    f.close()


# --------------------------------------------------- D E L E T E ------------------------------------------------------

def delete(user_account_number):

    is_delete_successful = False

    if os.path.exists(auth_session_path + str(user_account_number) + ".txt"):
        
        try:
            os.remove(auth_session_path + str(user_account_number) + ".txt")
            is_delete_successful = True
        
        except FileNotFoundError:

            print("User not found")
            
        finally:

            return is_delete_successful


# -------------------------------------------- AUTHENTICATION: Email, Account Number, Password -------------------------

def does_email_exist(email):
    
    all_users = os.listdir(user_db_path)

    for user in all_users:
        user_list = str.split(read(user), ',')
    
        if email in user_list:
            return True
    
    return False

def does_account_number_exist(account_number):

    all_users = os.listdir(user_db_path)
    
    for user in all_users:
    
        if user == str(account_number) + ".txt":
            return True
    
    return False

def authenticated_user(account_number, password):
    
    if does_account_number_exist(account_number):
        user = str.split(read(account_number), ',')
    
        if password == user[3]:
            return user
    
    return False