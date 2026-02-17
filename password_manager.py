import bcrypt
import sys

passwords = dict(
    hash="",
    password={}
)

def hash_password(password: str) -> bytes:
    password_bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed 

def verify_password(plain_password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

def create_new_master_password():
    password = input("Enter a master password: ")
    hashed_password = hash_password(password) 
    passwords['hash'] = hashed_password
    show_menu()

def check_old_master_password():
    password = input("Enter master password: ")
    is_correct = verify_password(password, passwords.get('hash'))
    if is_correct:
        show_menu()
    else:
        print("This password is not correct")
        check_old_master_password()

def show_menu():
    print("""
        1. View passwords
        2. Manage new password
        3. Verify master password
        4. Exit
    """
    )
    response = input(">")

    match response:
        case '1': view_passwords()
        case '2': manage_new_password()
        case '3': check_old_master_password()
        case '4': sys.exit()
        case _: 
            print("Please enter correct input")
            show_menu()

def view_passwords():
    for i, (name, password) in enumerate(passwords['password'].items()):
        print(f"{i + 1}. {name} => {password}")

    show_menu()

def manage_new_password():
    name = input("Enter name for new password: ")
    password = input("Enter the password to be saved: ")
    passwords.get('password')[name] = password
    show_menu()

if not passwords['hash']:
    create_new_master_password()
else:
    check_old_master_password()