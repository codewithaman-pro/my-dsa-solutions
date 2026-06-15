print("===== USER REGISTRATION =====")

username = input("Create Username: ")

while True:

    password = input("Create Password: ")

    if len(password) < 6:
        print("Password too short (Minimum 6 characters)")
        continue

    if len(password) > 12:
        print("Password too long (Maximum 12 characters)")
        continue

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    for ch in password:

        if ch.islower():
            has_lower = True

        elif ch.isupper():
            has_upper = True

        elif ch.isdigit():
            has_digit = True

        elif ch in "$#@/?.,'><_&^%!~":
            has_special = True

    if not has_lower:
        print("Password must contain a lowercase letter")
        continue

    if not has_upper:
        print("Password must contain an uppercase letter")
        continue

    if not has_digit:
        print("Password must contain a digit")
        continue

    if not has_special:
        print("Password must contain a special character")
        continue

    confirm_password = input("Confirm Password: ")

    if password != confirm_password:
        print("Passwords do not match")
        continue

    print("Registration Successful")
    break


print("\n===== LOGIN =====")

attempts = 3

while attempts > 0:

    login_user = input("Username: ")
    login_pass = input("Password: ")

    if login_user == username and login_pass == password:
        print("Login Successful")
        print("Welcome", username)
        break

    else:
        attempts -= 1
        print("Invalid Username or Password")
        print("Attempts Left:", attempts)

if attempts == 0:
    print("Account Locked")