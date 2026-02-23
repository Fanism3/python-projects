#Simple Banking System
#Author: <Fanism3>
#Description: A beginner Python banking simulation.

import time

balance = 0
is_running = True

def check1(x):
    if not x.isdigit():
        return "invalid"

def check2(x):
    if balance < int(x):
        return "invalid balance"

def money_add():
    global money_added
    global balance
    money_added = int(money_added)
    balance = balance + money_added
    time.sleep(1)  # i use time.sleep often for a better visual effect

def options(x):
    if x == "1":
        return "view balance"
    elif x == "2":
        return "deposit"
    elif x == "3":
        return "withdraw"
    elif x == "4":
        return "quit program"
    else:
        return "invalid"

while is_running:
    print("*********************")
    print("1. -> View balance")
    print("2. -> Deposit money")
    print("3. -> Withdraw money")
    print("4. -> Quit program")
    print("*********************")
    entry = input("Enter here: ")
    check1_entry = check1(entry)
    if check1_entry == "invalid":
        print("Please enter a valid value")
        time.sleep(1)
        continue

    options_entry = options(entry)
    if options_entry == "view balance":
        time.sleep(1)
        print("*********************")
        print(f"Your balance is ${balance}")
    elif options_entry == "deposit":
        while True:
            print("*********************************")
            money_added = input("Deposit the desired amount here: ")
            check1_money_added = check1(money_added)
            if check1_money_added == "invalid":
                print("*************************************")
                print("Enter a valid value next time please")
            else:
                money_add()
                time.sleep(1)
                print("*************************************************************")
                print("Your money has been deposited into your account successfully")
                break
    elif options_entry == "withdraw":
        while True:
            withdraw_amount = input("Enter the amount of money you would like to withdraw: ")
            check1_withdraw_amount = check1(withdraw_amount)
            if check1_withdraw_amount == "invalid":
                print("***************************")
                print("Please enter a valid input")
            else:
                break

        check2_withdraw_amount = check2(withdraw_amount)
        if check2_withdraw_amount == "invalid balance":
            withdraw_amount = int(withdraw_amount)
            balance = int(balance)
            money_short = withdraw_amount - balance
            time.sleep(1)
            print("**************************************************")
            print(f"We are sorry but you are ${money_short} short ")
        else:
            withdraw_amount = int(withdraw_amount)
            balance = balance - withdraw_amount
            time.sleep(1)
            print("****************************************")
            print("Your money were withdrawn successfully")
            print(f"Your new balance is ${balance}")

    elif options_entry == "quit program":
        print("***************")
        print("Thank you, Bye")
        is_running = False