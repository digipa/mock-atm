#CRUD Records

import os
import validation

user_db_path = "data/user_record/"

--------------------------------------------------- C R E A T E ------------------------------------------------------

def create(user_account_number, first_name, last_name, email, password):
# add does_email_exist, does_account_number_exist
# add a try except block which contains read, and delete functions

    user_data = first_name + "," + last_name + "," + email + "," + password + "," +str(0)

    if does_account_number_exist(user_account_number):
        
        return False
    
    if does_email_exist(email):
        print("User already exists")
        return False
    
    completion_state = False

    try:
        f = open(user_db_path + str(user_account_number) + ".txt")
        
        if not does_file_contain_data:
            delete(user_account_number)
        
        else:

            f.write(str(user_data));
            completion_state = True

        finally:

            f.close();
            return completion_state


----------------------------------------------------- R E A D --------------------------------------------------------

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

--------------------------------------------------- U P D A T E ------------------------------------------------------

def update(user_account_number):
    print("Update user record")

--------------------------------------------------- D E L E T E ------------------------------------------------------

def delete(user_account_number):

    is_delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):
        
        try:
            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True
        
        except FileNotFoundError:

            print("User not found")
            
        finally:

            return is_delete_successful

----------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------

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
    if does_account_number_exist(account_number)
        user = str.split(read(account_number), ',')
        if password == user[3]