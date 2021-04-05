def option():
    print('\n What would you like to do?: 1: Balance 2: Withdrawal 3: Cash Deposit 4: Complaint 5: Exit \n')

    def selection():
        return int(input("Please select an option: \n"))

    choice = selection()

    if choice == 1:
        print('1: Balance 2: Main Screen')

        choice2 = selection()
        if choice2 == 1:
            print('Your balance is %s.' % sum(accountBalance))
            option()
        elif choice2 == 2:
            option()
        else:
            print('Invalid Option selected, please try again')
            
    if choice == 2:
        print('1: Withdrawal 2: Main Screen')

        choice2 = selection()
        if choice2 == 1:
            accountBalance.append(-int(input('How much would you like to withdraw? \n')))
            print('Take your cash \n')
            option()
        elif choice2 == 2:
            option()
        else:
            print('Invalid Option selected, please try again')

    elif choice == 3:
        print('1. Cash Deposit 2: Main Screen')

        choice2 = selection()
        if choice2 == 1:
            accountBalance.append(int(input('How much would you like to deposit? \n')))
            print('Your current balance is %s' % sum(accountBalance))
            option()
        elif choice2 == 2:
            option()
        else:
            print('Invalid Option selected, please try again')

    elif choice == 4:
        print('1. Complaint 2: Main Screen')

        choice2 = selection()
        if choice2 == 1:
            input('What issue will you like to report? \n')
            print('Thank you for contacting us')
            option()
        elif choice2 == 2:
            option()
        else:
            print('Invalid Option selected, please try again')

    elif choice == 5:
        print('Thank you %s. We look forward to seeing you again.' % name)

    else:
        print('Invalid Option selected, please try again')
        option()