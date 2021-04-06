def mainOptions():

    selection = int(input('What would you like to do?: 1: Balance 2: Withdrawal 3: Cash Deposit 4: Complaint 5: Main Options 6: Exit \n'))

    if selection == 1:
        balance()

    elif selection == 2:
        withdrawal()

    elif selection == 3:
        deposit()

    elif selection == 4:
        complaint()

    elif selection == 5:
        mainOptions()

    elif selection == 6:
        print('Thank you %s. We look forward to seeing you again.' % name)

    else:
        invalidOption()
    mainOptions()



def balance():
    print('Your balance is %s.' % sum(accountBalance))
    
def withdrawal():
    accountBalance.append(-int(input('How much would you like to withdraw? \n')))
    print('Take your cash \n')

def deposit():
    accountBalance.append(int(input('How much would you like to deposit? \n')))
    print('Your current balance is %s' % sum(accountBalance))

def complaint():
    input('What issue will you like to report? \n')
    print('Thank you for contacting us')

def invalidOption():
    print('That is an invalid option')





# def mainOptions():

#     selection =return int(input('What would you like to do?: 1: Balance 2: Withdrawal 3: Cash Deposit 4: Complaint 5: Exit \n')

#     if selection == 1:
#         print('1: Balance 2: Main Screen')

#         if selection == 1:
#             balance()

#         elif selection == 2:
#             mainOptions()
#         else:
#             invalidOption()
#         mainOptions()

#     if selection == 2:
#         print('1: Withdrawal 2: Main Screen')

#         if selection == 1:
#             balance()
#         elif selection == 2:
#             mainOption()
#         else:
#             invalidOption()

#     elif selection == 3:
#         print('1. Cash Deposit 2: Main Screen')

#         if selection == 1:
#         elif selection == 2:
#             mainOption()
#         else:
#             invalidOption()

#     elif selection == 4:
#         print('1. Complaint 2: Main Screen')

#         if selection == 1:
#             mainOption()
#         elif selection == 2:
#             mainOption()
#         else:
#             invalidOption()

#     elif selection == 5:
#         print('Thank you %s. We look forward to seeing you again.' % name)

#     else:
#         invalidOption()



# def balance():
#     print('Your balance is %s.' % sum(accountBalance))
#     option()
    
# def withdrawal():
#     accountBalance.append(-int(input('How much would you like to withdraw? \n')))
#     print('Take your cash \n')

# def deposit():
#     accountBalance.append(int(input('How much would you like to deposit? \n')))
#     print('Your current balance is %s' % sum(accountBalance))

# def complaint():
#     input('What issue will you like to report? \n')
#     print('Thank you for contacting us')

# def invalidOption():
#     print('That is an invalid option')