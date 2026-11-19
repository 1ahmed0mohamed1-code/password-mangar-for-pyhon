accounts = []
def wallcome():
    a = "passord-manger"
    print(a)
wallcome()
def add_account():
    a = input("entar you maill : ")
    b = input("enter you password : ")
    L = {'email': a , 'password': b}
    accounts.append(L)
    print("Saved!\n")

def show_accounts():
    print("\n--- Your Accounts ---")
    if not accounts: 
        print("No accounts saved yet.")
    else:
        for acc in accounts:
            print(f"Email: {acc['email']} | Password: {acc['password']}")
    print("---------------------\n")
    



def main():
    while True:
        print("1. add_account")
        print("2. Show_Accounts")
        print("3. Exit")
        choice = input("Choose (1/2/3): ")
        if choice == "1":
            add_account()
        elif choice == "2":
            show_accounts()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")
main()
