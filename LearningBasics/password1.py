def pass_verification():
    try:
            password = int(input("SET 6 Digit PIN: "))
    except ValueError:
            print("PIN must be a number")
            return False

    if len(str(password)) != 6:
            print("PIN must be 6 digits")
            return False

    return True

#pass_verification()