#Banking System

def show_balance(balance):
    print(f"Available Balance : {balance:.2f} ")

def deposit():
    amount= float(input("Enter Deposit: "))
    if amount<0:
        print("Amount cannot be negative.")
        return 0     
    else:
        return amount

def withdraw(balance):
    amount= float(input("Enter Withdrawal Amount : "))

    if amount<0:
        print("Amount cannot be negative.")
        return 0

    elif amount>balance:
        print("Withdrawal amount cannot be greater than balance")
        return 0
        
    else:
        return amount

def main():
    balance=0 #initial balance

    is_running=True
    
    while is_running:
        print("-------------------")
        print("Choose an Option: ")
        print("-------------------")

        print("1. Display Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("Press any button to Exit.")
        print("*******************")
        choice=input("Enter Your Choice (1-4): ")
        match choice:
            case '1':
                show_balance(balance)
            case '2':
                balance+=deposit()      
            case '3':
                balance-=withdraw(balance)
            case _:
                is_running=False
    print("********************************")
    print("Thank You for Your Patience")

if __name__=="__main__":
    main()
