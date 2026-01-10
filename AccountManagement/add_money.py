from data_manager import save_users
def add_money(user,users):
    try:
        amount=float(input("Enter amount to Wallet: "))
        if amount < 0:
            print("Enter positive amount ")
            return
        
        user["balance"]+=amount
        save_users(save_users)
        print("Money added to your Wallet")
    except ValueError:
        print("Invalid input")    