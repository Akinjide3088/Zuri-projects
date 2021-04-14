import datetime
import random

database = {}


def init():
    print("$---- Welcome to Bank Python ----$")
    haveaccount = int(input("Do have an Account with us?\n 1. Yes\n 2. No\n"))

    if haveaccount == 1:
        login()
    elif haveaccount == 2:
        register()
    else:
        print("Invalid option, please try again")
        init()


def login():
    print("***** Login *****")

    islogin = False

    while islogin == False:

        useracctnum = int(input("Enter Account Number:\n"))
        userpassword = input("Enter password:\n")

        for acctnum, userdetails in database.items():

            if acctnum == useracctnum:
                if userdetails[3] == userpassword:
                    islogin = True

        print("Invalid account number or password\n Try again")
    bankoperations()


def register():
    firstname = input("Enter first name:\n")
    lastname = input("Enter last name:\n")
    email = input("Enter email address:\n")
    password = input("Create a password:\n")

    useracctnum = generateacctnum()

    database[useracctnum] = [firstname, lastname, email, password]
    print("This is your Account Number: %d" % useracctnum)
    print("Make sure to keep it safe")
    print("== === === == == === ====")
    login()


def generateacctnum(): 
    acctnum = random.randrange(1111111111,5555555555)
    return acctnum


def bankoperations():
    print(datenow())

    print("This are the availabe options:\n 1. Withdrawal\n 2. Cash deposit\n 3. Complaint\n 4. Exit")
    selectoptions = int(input("Select option:\n"))

    if selectoptions == 1:
        withdrawal()

    elif selectoptions == 2:
        cashdeposit()

    elif selectoptions == 3:
        complaint()

    elif selectoptions == 4:
        exit()

    else:
        print("Invalid option, try again")
        bankoperations()


def withdrawal():
    print("***** Withdrawal *****")
    current_balance = 0
    useracctnum = generateacctnum()
    options  = int(input("1. Current\n2. Savings\n"))
    if options == 1 or 2:
        pass

    else:
        print("invalid option")
        withdrawal()

    withdraw_option = int(input("How Much will you like to Withdraw?\n 1. 10000       2. 5000\n 3. 1000        4. Others\n"))

    if withdraw_option == 1:
        current_balance -= 10000
        print("Take cash")
        print("Current balance: %d" % current_balance)
        database[useracctnum] = (current_balance)
        transaction()

    elif withdraw_option == 2:
        current_balance -= 5000
        print("Take cash")
        print("Current balance: %d" % current_balance)
        database[useracctnum] = (current_balance)
        transaction()

    elif withdraw_option == 3:
        current_balance -= 1000
        print("Take cash")
        print("Current balance: %d" % current_balance)
        database[useracctnum] = (current_balance)
        transaction()

    elif withdraw_option == 4:
        withdraw = int(input("Enter amount:\n"))
        current_balance -= withdraw
        print("Take cash")
        print("Current balance: %d" % current_balance)
        database[useracctnum] = (current_balance)
        transaction()

    else:
        print("Incorrect option, try again")
        withdrawal()


def cashdeposit():
    print("***** Cash Deposit *****")
    useracctnum = generateacctnum()
    current_balance = 0
    deposit_option = int(input("How Much will you like to deposit?\n 1. 10000        2. 5000\n 3. 1000        4. Others\n"))
    print(deposit_option)

    if deposit_option == 1:
        current_balance += 10000
        print("Cash successfully deposited")
        print("Current balance: %d" % current_balance)
        database[useracctnum] = (current_balance)
        transaction()

    if deposit_option == 2:
        print("Take cash")
        current_balance += 5000
        print("Cash successfully deposited")
        print("Current balance: %d" % current_balance)
        database[useracctnum] = (current_balance)
        transaction()

    if deposit_option == 3:
        print("Take cash")
        current_balance += 1000
        print("Cash successfully deposited")
        print("Current balance: %d" % current_balance)
        database[useracctnum] = (current_balance)
        transaction()

    elif deposit_option == 4:
        deposit = int(input("Enter amount:\n"))
        print("Cash successfully deposited")
        current_balance += deposit
        print("Current balance: %d" % current_balance)
        database[useracctnum] = (current_balance)
        transaction()

    else:
        print("Incorrect option, try again")
        cashdeposit()


def complaint():
    print("***** Complaint *****")
    print(input("What issue will you like to report?\n"))
    print("Thanks for contacting us")
    transaction()


def transaction():
    anothertransaction = int(input("Will you like to perform another transaction?\n 1. Yes\n 2. No\n 3. Exit\n"))
    print(anothertransaction)

    if anothertransaction == 1:
        bankoperations()

    elif anothertransaction == 2:
        logout()

    elif anothertransaction == 3:
        exit()

    else:
        print("Invalid option, try again")
        transaction()


def datenow():
    now = datetime.datetime.now()
    timenow = now.strftime("%b %d %Y\n %H:%M:%S")
    return timenow

def logout():
    login()

#----- Actual Banking System -----#
init()