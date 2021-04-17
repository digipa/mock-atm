accountBalance = []

def main_options(user):

    print('Welcome %s %s' % (user[0], user[1]))

    selection = int(input('What would you like to do?: 1: Balance 2: Withdrawal 3: Cash Deposit 4: Complaint 5: Main Options 6: Exit \n'))

    if selection == 1:
        balance()
        main_options(user)

    elif selection == 2:
        withdrawal()
        main_options(user)

    elif selection == 3:
        deposit()
        main_options(user)

    elif selection == 4:
        complaint()
        main_options(user)

    elif selection == 5:
        main_options(user)

    elif selection == 6:
        print('Thank you %s %s. We look forward to seeing you again.' % (user[0], user[1]))
        exit()
    else:
        invalidOption()
        main_options(user)

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

    main_options(user)
