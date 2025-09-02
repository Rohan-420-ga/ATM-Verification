print("Select your language:")
print("1. English")
print("2. Tamil")
lang = input("Enter choice (1 or 2): ")

if lang == "1" or lang.lower() == "english":
    pin = "1234"
    balance = 2000
    
    entered_pin = input("Enter your pin number: ")
    if entered_pin != pin:
        print("Incorrect pin")
    else:
        print("Welcome to My Bank")
        while True:
            print("\nOptions:")
            print("1. Fast Withdraw")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Check Balance")
            print("5. Exit")
            
            choice = input("Enter your selection: ")
            
            if choice == "1":
                amount = int(input("Enter withdraw amount: $"))
                if amount > balance:
                    print("Insufficient balance")
                else:
                    balance -= amount
                    print("Please take your cash.")
                    print("Receipt:")
                    print(f"Balance amount: ${balance}")
                    print("Thank you")
            
            elif choice == "2":
                acc_type = input("Select account (current/savings): ").lower()
                if acc_type in ["current", "savings"]:
                    amount = int(input("Enter withdraw amount: $"))
                    if amount > balance:
                        print("Insufficient balance")
                    else:
                        balance -= amount
                        print("Please collect your cash.")
                        print("Receipt:")
                        print(f"Balance amount: ${balance}")
                        print("Transaction ID: xxxx6373")
                        print("Thank you")
                else:
                    print("Invalid account type selection.")
            
            elif choice == "3":
                amount = int(input("Enter deposit amount: $"))
                balance += amount
                print(f"Deposit successful. New balance: ${balance}")
                print("Receipt:")
                print(f"New balance: ${balance}")
                print("Transaction ID: xxxx6373")
                print("Thank you")
            
            elif choice == "4":
                print("Receipt:")
                print(f"Your current balance: ${balance}")
                print("Thank you")
            
            elif choice == "5":
                print("Thank you for using My Bank ATM.")
                break
            
            else:
                print("Invalid option. Please try again.")
else:
    print("Selected language not supported.")
