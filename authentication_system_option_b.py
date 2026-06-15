
import re
import random
from datetime import datetime

users = {}

def password_strength(password):
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "$#@/?.,'><_&^%!~" for c in password): score += 1
    if len(password) >= 8: score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    return "Strong"

def validate_password(password):
    if not (6 <= len(password) <= 12):
        return False
    return (
        any(c.islower() for c in password)
        and any(c.isupper() for c in password)
        and any(c.isdigit() for c in password)
        and any(c in "$#@/?.,'><_&^%!~" for c in password)
    )

def save_log(msg):
    with open("login_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} : {msg}\n")

def register():
    username = input("Username: ")
    if username in users:
        print("User already exists.")
        return

    email = input("Email: ")
    if not re.match(r"^[^@]+@[^@]+\.[^@]+$", email):
        print("Invalid email")
        return

    mobile = input("Mobile (10 digits): ")
    if not (mobile.isdigit() and len(mobile) == 10):
        print("Invalid mobile number")
        return

    password = input("Password: ")
    if not validate_password(password):
        print("Password does not meet requirements.")
        return

    print("Strength:", password_strength(password))

    confirm = input("Confirm Password: ")
    if confirm != password:
        print("Passwords do not match.")
        return

    otp = random.randint(100000, 999999)
    print("Demo OTP:", otp)

    entered = input("Enter OTP: ")
    if entered != str(otp):
        print("OTP verification failed.")
        return

    question = input("Security Question - Favourite Color? ")
    answer = input("Answer: ")

    users[username] = {
        "email": email,
        "mobile": mobile,
        "password": password,
        "question": question,
        "answer": answer
    }

    print("Registration Successful")

def login():
    username = input("Username: ")

    attempts = 3
    while attempts > 0:
        password = input("Password: ")

        if username in users and users[username]["password"] == password:
            print("Login Successful")
            save_log(f"{username} login success")
            dashboard(username)
            return

        attempts -= 1
        print("Wrong credentials. Attempts left:", attempts)

    save_log(f"{username} account locked")
    print("Account Locked")

def forgot_password():
    username = input("Username: ")

    if username not in users:
        print("User not found")
        return

    print("Security Question:", users[username]["question"])
    ans = input("Answer: ")

    if ans == users[username]["answer"]:
        print("Password is:", users[username]["password"])
    else:
        print("Incorrect answer")

def change_password(username):
    old = input("Old Password: ")

    if old != users[username]["password"]:
        print("Incorrect old password")
        return

    new = input("New Password: ")

    if not validate_password(new):
        print("Weak password")
        return

    users[username]["password"] = new
    print("Password changed successfully")

def dashboard(username):
    while True:
        print("\n===== USER DASHBOARD =====")
        print("1. View Profile")
        print("2. Change Password")
        print("3. Logout")

        ch = input("Choice: ")

        if ch == "1":
            print(users[username])

        elif ch == "2":
            change_password(username)

        elif ch == "3":
            print("Logged out")
            break

def admin_panel():
    admin_user = input("Admin Username: ")
    admin_pass = input("Admin Password: ")

    if admin_user != "admin" or admin_pass != "admin123":
        print("Invalid admin credentials")
        return

    while True:
        print("\n===== ADMIN PANEL =====")
        print("1. View Users")
        print("2. Delete User")
        print("3. Exit")

        ch = input("Choice: ")

        if ch == "1":
            for u in users:
                print(u)

        elif ch == "2":
            u = input("Username to delete: ")
            users.pop(u, None)
            print("User removed")

        elif ch == "3":
            break

while True:
    print("\n===== AUTHENTICATION SYSTEM =====")
    print("1. Register")
    print("2. Login")
    print("3. Forgot Password")
    print("4. Admin Panel")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        register()

    elif choice == "2":
        login()

    elif choice == "3":
        forgot_password()

    elif choice == "4":
        admin_panel()

    elif choice == "5":
        print("Goodbye")
        break

    else:
        print("Invalid choice")
