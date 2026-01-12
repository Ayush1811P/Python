def register_user(data,username,password):
    if not username:
        return {"error":"must enter username"}#this is called existance validation
    if not password:
        return {"error":"must enter password"}
    if username in data["users"]:
        return {"error":"username already exists"}#this is called existance validation
    if len(password)<4:
        return {"error":"password must be of min 4 digits"}#this is called existance validation
    data["users"][username]={
        "password":password,
        "balance":10000
    }
    return {"Success":True}

def add_movie(data,name,price,seats):
    if  not name:
        return {"error":"Enter the name of the movie"}
    if price<0:
        return{"error":"price can be zero for free but cannot be in -ve"}#this is called existance validation
    if seats<=0:
        return {"error":"enter valid seats"}#this is called existance validation
    if name in data["movies"]:
        return {"error":"No-duplicates allowed"}
    data["movies"][name]={
        "price":price,
        "seats":seats
    }
    return {"Success":True}

def book_ticket(data,username,movie_name):
    if not username:
        return {"error":"enter usename"}
    if not movie_name:
        return {"error":"enter movie name"}
    if username not in data["users"]:
        return {"error":"username dose not exists!"}
    if movie_name not in data["movies"]:
        return {"error":"Movie is not in our list"}
    movie=data["movies"][movie_name]
    user=data["users"][username]
    if movie["seats"]<=0:
        return {"error":"sorry we are full!"}
    if user["balance"]<movie["price"]:
        return {"error":"Insuffiecient Balance"}
    user["balance"]-=movie["price"]
    movie["seats"]-=1
    return {"success":True}

import json
def load_data():
    try:
        with open("movies.json","r")as file:
            return json.load(file)
    except FileNotFoundError:
        return{
            "users":{},
            "movies":{}
        }
    
def save_data(data):
    with open("movies.json","w")as file:
        json.dump(data,file)    


data = load_data()

register_user(data, "aayu", "abc123")
add_movie(data, "Avengers", 100, 5)
add_movie(data, "Marvel Supermane", 300, 5)
add_movie(data, "Batman", 200, 5)

book_ticket(data, "aayu", "Avengers")

save_data(data)