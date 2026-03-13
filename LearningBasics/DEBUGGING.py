"""Simple registration/login example using an in-memory dict as the database."""


def register_user(user_db: dict) -> bool:
    """Register a user and store their info in user_db.

    Returns True if registration succeeds, False otherwise.
    """

    print("\n--- Register ---")

    name = input("Name: ").strip()
    if not name:
        print("Name is required.")
        return False

    try:
        age = int(input("Age: "))
    except ValueError:
        print("Age must be a number.")
        return False

    if age <= 10:
        print("Age must be greater than 10.")
        return False

    username = input("Username: ").strip()
    if not username:
        print("Username is required.")
        return False

    if username in user_db:
        print("Username already exists. Please choose another.")
        return False

    password = input("Password (6 digits): ").strip()
    if not password.isdigit() or len(password) != 6:
        print("Password must be exactly 6 digits.")
        return False

    user_db[username] = {
        "name": name,
        "age": age,
        "password": password,
    }

    print("Registration successful!")
    return True


def login(user_db: dict) -> bool:
    """Prompt the user to log in using the stored user_db."""

    print("\n--- Login ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    user = user_db.get(username)
    if not user:
        print("User not found.")
        return False

    if user["password"] != password:
        print("Wrong password.")
        return False

    print(f"Welcome back, {user['name']}! (age {user['age']})")
    return True


def main():
    user_db = {}

    while True:
        print("\n1) Register")
        print("2) Login")
        print("3) Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            register_user(user_db)
        elif choice == "2":
            login(user_db)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

