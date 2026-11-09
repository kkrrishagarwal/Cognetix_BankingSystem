import json
import os

BALANCE_FILE = "account.json"

def initialize_account():
    if not os.path.exists(BALANCE_FILE):
        write_balance(0.0)

def read_balance():
    initialize_account()
    try:
        with open(BALANCE_FILE, "r") as file:
            data = json.load(file)
            return float(data.get("balance", 0.0))
    except (json.JSONDecodeError, ValueError, IOError):
        write_balance(0.0)
        return 0.0

def write_balance(balance):
    with open(BALANCE_FILE, "w") as file:
        json.dump({"balance": round(balance, 2)}, file, indent=4)

def deposit(amount):
    if amount <= 0:
        print("❌ Error: Deposit amount must be greater than zero.")
        return
    balance = read_balance()
    balance += amount
    write_balance(balance)
    print(f"✅ Successfully deposited ₹{amount:,.2f}. New Balance: ₹{balance:,.2f}")

def withdraw(amount):
    if amount <= 0:
        print("❌ Error: Withdrawal amount must be greater than zero.")
        return
    balance = read_balance()
    if amount > balance:
        print(f"❌ Error: Insufficient balance! Current Balance: ₹{balance:,.2f}")
        return
    balance -= amount
    write_balance(balance)
    print(f"✅ Successfully withdrew ₹{amount:,.2f}. Remaining Balance: ₹{balance:,.2f}")

def check_balance():
    balance = read_balance()
    print(f"💰 Current Account Balance: ₹{balance:,.2f}")

def main():
    initialize_account()
    while True:
        print("\n====================================")
        print("   COGNETIX BANKING SYSTEM (CLI)    ")
        print("====================================")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        print("------------------------------------")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            try:
                amt = float(input("Enter amount to deposit: ₹"))
                deposit(amt)
            except ValueError:
                print("❌ Invalid input! Please enter a valid numeric amount.")
        elif choice == "2":
            try:
                amt = float(input("Enter amount to withdraw: ₹"))
                withdraw(amt)
            except ValueError:
                print("❌ Invalid input! Please enter a valid numeric amount.")
        elif choice == "3":
            check_balance()
        elif choice == "4":
            print("Thank you for using Cognetix Banking System. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please select an option from 1 to 4.")

if __name__ == "__main__":
    main()
