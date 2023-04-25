# Importing csv for the Interface
import csv
# Creating a global variable for use in the Interface
master_customer_list = []


class Account:
    """
    Abstract class representing an account object.

    Attributes:
        account_id: four-digit numeric string
        balance: balance of the account, for checking and savings this denotes the amount available,
                 for credit, this denotes the total charges on the account
        interest: the interest rate of the account, these are fixed values
                  checking: 0%, savings: 1%, credit: 30%
    """

    # Specifying how the Account is Initialized, no default values are given or expected.
    def __init__(self, new_id, new_balance):
        self.account_id = new_id
        self.balance = new_balance
        # Specifying different interest amounts based on the type of Account
        if isinstance(self, Checking):
            self.interest = 0.00
        elif isinstance(self, Savings):
            self.interest = 0.01

    # Printing an Account object will simply return the user's Account ID
    def __str__(self):
        return f'   ID: {self.account_id}\n' \
               f'   Balance: {self.balance}\n' \
               f'   Interest: {self.interest}'

    # Get, set, and del methods for account_id
    def get_account_id(self):
        return self._account_id

    def set_account_id(self, new_id):
        # Ensuring the account_id is a string of length 4
        if not isinstance(new_id, str):
            raise TypeError('input id should be a string')
        elif len(new_id) != 4:
            raise ValueError('id should be four digits long')
        # The ID must be made of numerical characters. The following for loop tests each single character of the string.
        allowed_chars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        for digit in new_id:
            if digit not in allowed_chars:
                raise ValueError('id should consist only of numeric digits')

        self._account_id = new_id

    def del_account_id(self):
        # Deleting the account_id and also the entire Account object
        del self._account_id
        del self

    # Get, set, del methods for balance
    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        # The balance must be a float or integer type greater than zero.
        if not isinstance(new_balance, (float, int)):
            raise TypeError('balance should be a float or integer type')
        elif new_balance < 0:
            raise ValueError('balance cannot be negative')

        self._balance = new_balance

    def del_balance(self):
        self._balance = 0

    # Get, set, del methods for interest
    def get_interest(self):
        if isinstance(self, Checking):
            return 0.00
        elif isinstance(self, Savings):
            return 0.01
        elif isinstance(self, Credit):
            return 0.30

    def set_interest(self, interest):
        # Unless the interest is being set to a specific value, a TypeError is raised
        if not isinstance(self, Checking) and interest != 0.00:
            pass
        elif not isinstance(self, Savings) and interest != 0.01:
            pass
        elif not isinstance(self, Credit) and interest != 0.30:
            pass
        else:
            raise TypeError('interest rates cannot be changed')

    def del_interest(self):
        # Interest rates are fixed
        raise TypeError('interest rates cannot be deleted')

    # Wrapping each (get, set, del) set into a property
    account_id = property(get_account_id, set_account_id, del_account_id)
    balance = property(get_balance, set_balance, del_balance)
    interest = property(get_interest, set_interest, del_interest)

    def increment_balance(self, amount):
        if isinstance(self, Credit):
            raise TypeError('Cannot Increment Credit Balance')
        elif amount < 0.0:
            raise TypeError('Amount must be a positive value')
        else:
            self.balance += amount


class Checking(Account):
    """
    This class inherits all the methods in the Account class. This exists simply to distinguish the Account types,
    no additional code is needed.
    """


class Savings(Account):
    """
    This class inherits all the methods in the Account class. This exists simply to distinguish the Account types,
    no additional code is needed.
    """


class Credit(Account):
    """
    This class inherits all the methods in the Account class.

    The Credit class has some unique differences to other Account types. Rather than having a balance, the Credit class
    has an attribute 'credit_limit' representing a credit limit. The __init__ and __str__ methods are
    overloaded to account for this attribute swap.
    """

    # Overloading the __init__ method from Account add credit_limit.
    def __init__(self, new_id, new_balance, new_credit_limit):
        self.account_id = new_id
        self.balance = new_balance
        self.credit_limit = new_credit_limit
        self.interest = 0.30

    # Overloading the __str__ method from Account to add credit_limit
    def __str__(self):
        return f'   ID: {self.account_id}\n' \
               f'   Balance: {self.balance}\n' \
               f'   Credit Limit: {self.credit_limit}\n' \
               f'   Interest: {self.interest}'

    # Get, set, del methods for credit_limit
    def get_credit_limit(self):
        return self._credit_limit

    def set_credit_limit(self, new_credit_limit):
        # The credit_limit must be a float type greater than zero.
        if not isinstance(new_credit_limit, float):
            raise TypeError('credit_limit should be a float type')
        elif new_credit_limit < self._balance:
            raise ValueError('credit_limit cannot be less than balance')

        self._credit_limit = new_credit_limit

    def del_credit_limit(self):
        self._credit_limit = 0

    credit_limit = property(get_credit_limit, set_credit_limit, del_credit_limit)


class Customer:
    """
    Abstract class representing a customer object.
    Uses account information but does not inherit the Account class.

    Attributes:
        username: string representation of the customer
        checking: a Checking object representing the checking account of this customer
        savings: a Savings object representing the savings account of this customer
        credit: a Credit object representing the credit account of this customer
    """

    # Specifying the attributes for Customer. No defaults are given or expected.
    def __init__(self, username, checking, savings, credit):
        self.username = username
        self.checking = checking
        self.savings = savings
        self.credit = credit

    # Specifying how Customer will print to the user
    def __str__(self):
        return f'Username: {self.username}\n' \
               f'Checking:\n{self.checking}\n' \
               f'Savings:\n{self.savings}\n' \
               f'Credit:\n{self.credit}\n'

    # Get, set, del methods for username
    def get_username(self):
        return self._username

    def set_username(self, username):
        # The username must be a string
        if not isinstance(username, str):
            TypeError('username must be a string type')
        self._username = username

    def del_username(self):
        # Deleting a Customers username deletes their entire Account
        del self

    # Get, set, del methods for checking
    def get_checking(self):
        return self._checking

    def set_checking(self, checking):
        # Must be a Checking type
        if not isinstance(checking, Checking):
            TypeError('checking must be a Checking class type')
        self._checking = checking

    def del_checking(self):
        del self._checking

    # Get, set, del methods for savings
    def get_savings(self):
        return self._savings

    def set_savings(self, savings):
        # Must be a savings type
        if not isinstance(savings, Savings):
            TypeError('checking must be a Savings class type')
        self._savings = savings

    def del_savings(self):
        del self._savings

    # Get, set, del methods for Credit
    def get_credit(self):
        return self._credit

    def set_credit(self, credit):
        # Must be a Credit type
        if not isinstance(credit, Credit):
            TypeError('checking must be a Credit class type')
        self._credit = credit

    def del_credit(self):
        del self._credit

    # Defining properties for our sets of (Get, set, del) methods
    username = property(get_username, set_username, del_username)
    checking = property(get_checking, set_checking, del_checking)
    savings = property(get_savings, set_savings, del_savings)
    credit = property(get_credit, set_credit, del_credit)


def prompt_for_customer():
    global master_customer_list

    print('Select Customer: ')
    for num in range(0, len(master_customer_list)):
        customer = master_customer_list[num].username
        print(f'#{num+1} - {customer}')
    return input('Customer: #')


def prompt_for_account():
    print('Select Account Type')
    print('#1 - Checking')
    print('#2 - Savings')
    return input('Account (1/2)')


def import_from_csv():
    """
    Interface Option
    This function will read in the specified csv file. When the csv is read in, a list containing each customer is
    created. This list is in the global scope, so any other Interface Option function will have access to it. Each time
    'Import csv' is selected, the master_customer_list is reset; this is done to avoid accidental duplication.
    :return: None
    """
    print('---Importing from .csv---')
    acct_file = input("File location: ")
    # Resetting master_customer_list to an empty list
    global master_customer_list
    master_customer_list = list()
    # Using try-except to open, read, and create a list out of the contents of the csv file.
    try:
        with open(acct_file + '.csv') as file:
            reader = csv.reader(file)
            # Looping over each line of the csv file
            for line in reader:
                # Creating customer objects, 'username' denotes column names, so we will avoid that line.
                if line[0] != 'username':
                    # Creating a temporary variable instantiating a Customer object
                    temp_item = Customer(line[0],
                                         Checking(line[1], float(line[2])),
                                         Savings(line[3], float(line[4])),
                                         Credit(line[5], float(line[6]), float(line[7])))

                    master_customer_list.append(temp_item)
    # If the try clause fails, an error is printed to the user
    except FileNotFoundError:
        print('Must reference valid accounts.csv file')


def view_customers():
    """
    Interface Option
    This function will print each customer along with their Account information
    :return:
    """
    global master_customer_list
    for customer in master_customer_list:
        print(customer)


def deposit():
    """
    Interface Option #3
    :return:
    """
    global master_customer_list
    customer_num = int(prompt_for_customer()) - 1
    # account_type 1-Checking, 2-Savings
    account_type = int(prompt_for_account())
    amount = float(input('Dollar Amount: $'))

    if account_type == 1:
        account = master_customer_list[customer_num].get_checking()

    elif account_type == 2:
        account = master_customer_list[customer_num].get_savings()
    account.increment_balance(amount)
    print(f'New Balance: ${account.balance}')

    # Increment account balance for customer:

    return


def withdraw():
    """
    Interface Option #4
    :return:
    """
    customer = master_customer_list[prompt_for_customer()]
    account_type = input('Checking or Savings: ')
    amount = input('Dollar Amount: $')
    try:
        bal = customer.account_type.get_balance()
        customer.account_type.set_balance(bal-amount)
    except ValueError:
        print(f'Insufficient funds for withdrawal of {amount}')
    return


def cc_charge():
    """
    Interface Option #5
    :return:
    """
    return


def cc_payment():
    """
    Interface Option #6
    :return:
    """
    return

#
# def save_to_csv():
#     """
#     Interface Option #9
#     Returns:
#
#     """
#     acct_file = input('accounts csv name: ')
#     try:
#         with open(acct_file+'.csv', 'w') as file:
#             writer = csv.writer(file)
#             for customer in master_customer_list:
#                 writer.write_row([customer.get_username(), ])
#
#     return


def interface():

    choice = ''
    while choice != '9':

        # Print the interface options
        print("1: Import from csv")
        print("2: View Customers")
        print("3: Deposit")
        print("4: Withdraw")
        print("5: Credit Card Charge")
        print("6: Credit Card Payment")

        print("9: Exit.")

        # Collect user input
        choice = input('Select an option:').strip()

        if choice == '1':
            import_from_csv()
        elif choice == '2':
            view_customers()
        elif choice == '3':
            deposit()
        elif choice == '4':
            withdraw()
        elif choice == '5':
            cc_charge()
        elif choice == '6':
            cc_payment()
        elif choice == '9':
            print("Shutting down...")
            save_to_csv()
        else:
            print("Please select an actual option.")


interface()
