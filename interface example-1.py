import csv


def import_from_csv():
    """
    Interface Option #1
    :return:
    """
    print('---Importing from .csv---')
    acct_file = input("File location: ")
    try:
        with open(acct_file + '.csv') as file:
            reader = csv.reader(file)
            for line in reader:
                print(line)
                # Create customer objects here?
#                 Customer(username=line[0], acct = ...)
#                 chking = Checking(line[1],line[2])
#                 savings = Savings(line[3], line[4])
#                 credit = Credit(line[])
    except FileNotFoundError:
        print('Must reference valid accounts.csv file')


def view_customers():
    """
    Interface Option #2
    :return:
    """
    return


def deposit():
    """
    Interface Option #3
    :return:
    """
    return


def withdraw():
    """
    Interface Option #4
    :return:
    """
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
        else:
            print("Please select an actual option.")


interface()

