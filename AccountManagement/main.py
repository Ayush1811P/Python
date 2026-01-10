from data_manager import load_users
from register import register
from login import login
from add_money import add_money
from check_balance import check_balance
from send_money import send_money

def user_menu(user,users):
    while(True):
        print("""
--- User Menu ---
1. Add Money
2. Check Balance
3. Send Money
4. Logout
""")
        
        choice = input("choose option 1-4 : ")

        if choice== "1":
            add_money(user,users)
        elif choice== "2":
            check_balance(user)    
        elif choice== "3":
            send_money(user,users)    
        elif choice == "4":
            print("Logged OUT")  
            break  

def main():
    users=load_users

    while True:
                print("""
--- Main Menu ---
1. Register
2. Login
3. Exit
""")
                choice = input("Enter choice 1-3: ")

                if choice== "1":
                     register(users)
                elif choice == "2":
                    user= login(users)
                    if user:
                         user_menu(user,users)      
                elif choice== "3":
                     print("BYE!")  
                     break 
                else:
                     print("Invalid choice!")      

if __name__ == "__main__":
     main()                