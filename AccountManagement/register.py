from data_manager import get_next_id,find_user,save_users
def register(users):
    print("\n---Register-----")
    name=input("Enter name: ")
    username=input("chose username: ")

    if find_user(users,username):
        print("username already exists")
        return
    
    password=input("Chose Password: ")

    new_user={
        "id":get_next_id,
        "name":name,
        "username":username,
        "password":password,
        "balance":0.0
    }
    users.append(new_user)
    save_users(users)
    print("Registration Complete")