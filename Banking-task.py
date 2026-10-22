balance = 10000

print("Welcome to Kiran Bank")
print("Opening Balance: Rs.",balance)

while True:
    print("\n-----Banking Menu-----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice:")

    if choice == "1":
        print("Current Balance:Rs.",balance)
    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount:"))
            if amount > 0:
                balance += amount
                print("Deposit successful.")
                print("Updated Balance:Rs.",balance)
            else:
                print("Invalid input. Please enter withdrawal amount:")
                if amount <= 0:
                    print("Invalid amount. Please enter an amount greater than 0.")
                elif amount > balance:
                    print("Transaction failed: Insufficient balance.")
                    print("Current Balance:Rs.",balance)
                else:
                    balance -= amount
                    print("Withdrawal successful.")
                    print("Updated Balance:Rs.",balance)

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    elif choice == "4":
        print("Thank you for banking with us.Goodbye!")
        break
    else:
        print("Invalid choice. Please select an option from 1 to 4.")