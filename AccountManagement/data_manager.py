import json
import os

FILE_NAME = "users.json"

def load_users():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_users(users):
    with open(FILE_NAME, "w") as file:
        json.dump(users, file, indent=4)

def get_next_id(users):
    if not users:
        return 1
    return max(user["id"] for user in users) + 1

def find_user(users, username):
    for user in users:
        if user["username"] == username:
            return user
    return None   # ✅ OUTSIDE loop
