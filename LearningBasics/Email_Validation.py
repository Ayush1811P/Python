
from f import email_verification
def registration():
    """Collects and validates basic user registration information.

    Returns True when all inputs pass simple validation checks.
    """

    name = input("Enter your name: ").strip()
    if not name:
        print("Enter name first!")
        return False

    try:
        age = int(input("Enter your age: "))
    except ValueError:
        print("Age must be a number")
        return False

    if age <= 10:
        print("Enter age > 10")
        return False

    email = input("Enter your email: ")
    email_verification(email)
    if email_verification==True:

        try:
            password = int(input("SET 6 Digit PIN: "))
        except ValueError:
            print("PIN must be a number")
            return False

        if len(str(password)) != 6:
            print("PIN must be 6 digits")
            return False

        return True
    else:
        print("Email verification false")
registration()