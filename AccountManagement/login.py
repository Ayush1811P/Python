from data_manager import find_user
def login(users):
    print("\n---Login----")
    username=input("Enter username: ")
    password=input("Enter password: ")

    user=find_user(users,username)

    if not user or user["password"]!=password:
        print("Invalid Username or Password")
        return None
    
    print(f"Welcome, {user['name']}")
    return user