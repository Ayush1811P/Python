import json
def register_user(users,username,password):
    if not username:
        return{"error": "username required"}#this is called existance validation
    if len(password)<6:
        return {"error":"Password too short"}#this is called existance validation
    if username in users:
        return {"error":"Username already exists"}#this is called existance validation
    users[username]={
        "password":password,
        "balance":1000
    }
    return{"success":True}



def login_user(users,username,password):
    if not username:
        return {"error":"enter username"}#this is called existance validation
    if not password:
        return {"error":"Enter password"}
    if  username not in users:
        return {"error":"username dose not exists"}#this is called existance validation
    stored_password=users[username]["password"]
    if password != stored_password:
        return {"error":"Incorrect password"}
    
    return {"Success":True}

def send_money(users,sender,recevier,amount):
    if not sender:
        return {"error":"senders username required"}
    if not recevier:
        return {"error":"recevier's username required"}
    if sender not in users:
        return {"error":"sender dose not exists!"}
    if recevier not in users:
        return {"error":"reciever dose not exists"}
    if amount <=0:
        return {"error":"enter a valid amount"}
   
    if users[sender]["balance"]<amount:
        return {"error":"Insufficient balance!"}
    users[sender]["balance"]-=amount
    users[recevier]["balance"]+=amount
    return{"success":True}

def load_users():
    try:
        with open("holders.json","r")as file:
            return json.load(file)
    except FileNotFoundError:
        return{}    
    
def save_users(users):
        with open("holders.json","w")as file:  
          json.dump(users,file)
    
users = load_users()

register_user(users, "Ayush", "88008191")
register_user(users, "Babbu", "88008191")

send_money(users, "Ayush", "Babbu", 200)

save_users(users)
