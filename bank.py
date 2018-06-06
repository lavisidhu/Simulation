accountnumber=0
accounts=[]
transactions={}
accountnumbers = []
def main():

    while True:
        print("Bank account application\n\t1) Create new account\n\t2) Credit/Debit an\
 account\n\t3) List all accounts\n\t4) List account history\n\t5) Sum of all account\
 balances\n\t6) Quit")
        choice = input("What would you like to do: ")

        if choice == '1':
            print("Creating a new account.....")
            print("Please enter the individuals")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            begining_balance = float(input("begining balance: "))
            account_number = create(first_name,last_name,begining_balance)
            print("New account created for {} {} Account#{}".format(first_name.title(),last_name.title(),account_number))

        elif choice =='2':
            print("Crediting/Debiting account.....")
            account=int(input("Please enter the account number: "))
            amount=float(input("Please enter the amount: "))
            credit_debit(account,amount)

        elif choice =='3':
            listaccount()

        elif choice =='4':
            transaction()

        elif choice=='5':
            total=sum_balance()
            print("Sum of all account balances: ${0:,.2f}".format(total))

        elif choice =='6':
            print("*****Thank you*******")
            break

        else:
            print("Enter valid option")


def create(first_name,last_name,begining_balance):
    global accounts,account_number,accountnumbers
    account=[first_name,last_name,begining_balance,begining_balance]
    accounts.append(account)
    accountnumbers.append(len(accounts))
    account_number=len(accounts)
    return account_number


def credit_debit(account,amount):
    temp = []
    if account not in transactions.keys():
        temp.append(amount)
        transactions[account] = temp
    else:
        temp1 = transactions.get(account)
        temp1.append(amount)
        transactions[account] = temp1

    if isvalid(account):

        if amount < 0:
            accounts[account-1][2]=float(accounts[account-1][2])+float(amount)
            print("{0:} {1:} (Account# {2:}) debited ${3:.2f}".format(accounts[account-1][0].title(),accounts[account-1][1].title(),account,abs(amount)))
            print("New balance: ${} ".format(accounts[account-1][2]))
        else:
            accounts[account-1][2]=float(accounts[account-1][2])+float(amount)
            print("{0:} {1:} (Account# {2:}) credited ${3:.2f}".format(accounts[account-1][0].title(),accounts[account-1][1].title(),account,abs(amount)))
            print("New balance: ${} ".format(accounts[account-1][2]))


def listaccount():
    print("Listing accounts....")
    for account in range(account_number):
        print("{}\t{} {}\t${}".format(account+1,accounts[account][0].title(),accounts[account][1].title(),accounts[account][2]))


def transaction():
    print("Transaction history")
    account = int(input("Enter the account number: "))

    if isvalid(account):
        print("{}\t{} {}".format(account,accounts[account-1][0].title(),accounts[account-1][1].title()))
        transaction_list=transactions.get(account)
        balance=accounts[account-1][3]
        for amount in transaction_list:
            print("${}\t\t\t${}".format(balance,amount))
            balance=balance+amount
        print("${}".format(accounts[account-1][2]))


def isvalid(account):
    if account in accountnumbers:
        return True
    else:
        print("Account number not in record.")


def sum_balance():
    total=0
    for account in accounts:
        total=total+account[2]
    return total


def memory_clear():
    global accounts,accountnumbers,balances
    accounts=[]
    accountnumbers=[]
    transactions={}


# main()
