from data_manager import find_user,save_users

def send_money(sender,users):
    receiver_username=input("Enter the Receiver username: ")
    receiver=find_user(users,receiver_username)

    if not receiver:
        print("Reciver not found!")
        return
    
    try:
        amount=float(input("Enter amount to send: "))
        if amount <=0:
            print("Amount must be positive")
            return
        
        sender["balance"]-=amount
        receiver["balance"]+=amount

        print(f"Sent ₹{amount: .2f} to {receiver['username']}")
    except ValueError:
        print("Invalid amount/ Low Balanace")    