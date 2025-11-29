balance=int(input("Enter your balance: "))
while True:
    print("Welcome to ATM...!")
    print("\n")
    print("1.check your Bank Balance.")
    print("2.Deposit amount to yuor Bank Account.")
    print("3.Withdrow amount in Your Bank Account.")
    print("4.Exit")
    choice=int(input("Enter your choice(1 to 4): "))
    if choice == 1:
        print("Your Bank Balance is: ",balance)
    elif choice == 2:
        deposit=int(input("Enter amount to deposit in your Bank Account: "))
        balance=deposit+balance
        print("Your Amount is Deposit Successfully..!")
        print("Now your Bank balance is: ",balance)
    elif choice == 3:
        withdrow=int(input("Enter the Amount you want to withdrow: "))
        if withdrow<=balance:
            balance=balance-withdrow
            print("Withdrow Amount is Successfully..!")
            print("Now your Bank balance is: ",balance)
        else:
            print("Sorry...!Your Bank Balance is Low.")
    elif choice == 4:
        print("Thank you to visit ATM..!")
        break
        
    else:
        print("Thank you to visit ATM..!")
        






