# SBI Simple Bank Management System

customers = {}

def addcustomers():
    nm = input("Enter Customer Name: ")
    cn = input("Enter Contact: ")
    amt = float(input("Enter Amount: "))
    customers[nm] = {'contact': cn, 'balance': amt}
    print("== Customer Added Successfully ==")

def depositamount():
    nm = input("Enter Customer Name: ")
    if nm in customers:
        amt = float(input("Enter Deposit Amount: "))
        customers[nm]['balance'] += amt
        print("== Amount Deposited Successfully ==")
        print("Updated Balance:", customers[nm]['balance'])
    else:
        print("Customer not found.")

def withdrawalamount():
    nm = input("Enter Customer Name: ")
    if nm in customers:
        amt = float(input("Enter Withdrawal Amount: "))
        if customers[nm]['balance'] >= amt:
            customers[nm]['balance'] -= amt
            print("== Amount Withdrawn Successfully ==")
            print("Updated Balance:", customers[nm]['balance'])
        else:
            print("Insufficient balance.")
    else:
        print("Customer not found.")

def viewbalance():
    nm = input("Enter Customer Name: ")
    if nm in customers:
        print("\n=== Account Details ===")
        print("Customer:", nm)
        print("Contact:", customers[nm]["contact"])
        print("Balance:", customers[nm]["balance"])
    else:
        print("Customer not found.")

def menu():
    while True:
        print("\n=== Welcome to SBI ===")
        print("1. Add Customer")
        print("2. Deposit Amount")
        print("3. Withdraw Amount")
        print("4. View Balance")
        print("5. Exit")

        op = input("Please Select Option: ")

        if op == "1":
            addcustomers()
        elif op == "2":
            depositamount()
        elif op == "3":
            withdrawalamount()
        elif op == "4":
            viewbalance()
        elif op == "5":
            print("Exiting program... Thank you for banking with SBI!")
            break
        else:
            print("Invalid option, try again....")

# Run Program
menu()
