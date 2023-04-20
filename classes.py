class Account:
    """
    Abstract class representing an account object.

    Attributes:
        account_id: four-digit numeric string
        balance: balance of the account, for checking and savings this denotes the ammound available,
                 for credit, this denotes the total charges on the account
        interest: the interest rate of the account, these are fixed values
                  checking: 0%, savings: 1%, credit: 30%
    """

    # will comment at a later time
    def __init__(self, new_id, new_balance, account_interest):
        self.account_id = new_id
        self.balance = new_balance

        if isinstance(self, Checking):
            self.interest = 0.00
        elif isinstance(self, Savings):
            self.interest = 0.01
        elif isinstance(self, Credit):
            self.interest = 0.30

    def __str__(self):
        return f'{self.account_id}'

    def get_account_id(self):
        return self._account_id

    def set_account_id(self, new_id):
        if not isinstance(new_id, str):
            raise TypeError ('input id should be a string')
        elif len(new_id) != 4:
            raise ValueError('id should be four digits long')

        allowed_chars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        for digit in new_id:
            if digit not in allowed_chars:
                raise ValueError('id should consist only of numeric digits')

        self._account_id = new_id

    def del_account_id(self):
        del self._account_id
        del self

    account_id = property(get_account_id, set_account_id, del_account_id)

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        if not isinstance(new_balance, float):
            raise TypeError ('balance should be a float type')
        elif new_balance < 0:
            raise ValueError ('balance cannot be negative')

        self._balance = new_balance

    def del_balance(self):
        self._balance = 0

    balance = property(get_balance, set_balance, del_balance)

    def get_account_interest(self):
        return self._interest

    def set_account_interest(self, account_interest):
        raise TypeError ('interest rates cannot be changed')

    def del_account_interest(self):
        raise TypeError ('interest rates cannot be deleted')

    account_interest = property(get_account_interest, set_account_interest, del_account_interest)


class Checking(Account):
    """
    This class inherits all methods and attributes from the Account class. No additional code is required.
    """


class Savings(Account):
    """
    This class inherits all methods and attributes from the Account class. No additional code is required.
    """


class Credit(Account):
    """
    Not finished
    """
