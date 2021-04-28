class Category:

    def __init__(self, type, amount):
        self.type = type
        self.amount = amount
    
    def deposit(self, amount):
        self.amount += amount
        return 'Deposited {} in {} category.\n'.format(amount, self.type)
    
    def withdraw(self, amount):
        self.amount -= amount
        return 'Withdrew {} in {} category.\n'.format(amount, self.type)
    
    def transfer(self, amount, type):
        return self.withdraw(amount) + type.deposit(amount)
    
    def checkBalance(self):
        return 'Current balance is {}'.format(self.amount)

# ----------------------------------------------------------------  Example Budget Categories  -----------------------------------------------------------------

groceries_category = Category("Groceries", 1000)
dining_out_category = Category("Dining Out", 1000)
entertainment_category = Category("Entertainment", 1000)
excursions_category = Category("Excursions", 1000)
household_bills_category = Category("Household Bills", 1000)
personal_expenditure_category = Category("Personal Expenditure", 1000)

# -----------------------------------------------------------  Testing Methods using Print Statement  -----------------------------------------------------------------

print(groceries_category.transfer(250, dining_out_category))
print(groceries_category.deposit(500))
print(groceries_category.withdraw(100))
print(groceries_category.checkBalance())