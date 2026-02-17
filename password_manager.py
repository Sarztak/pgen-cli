import bcrypt
import sys
import sqlite3

conn = sqlite3.connect("./passwords.db")
cursor = conn.cursor()

def hash_password(password: str) -> bytes:
    password_bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed 

def verify_password(plain_password: str, hashed_password: bytes) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password)

def create_new_master_password():
    password = input("Enter a master password: ")
    hashed_password = hash_password(password) 
    cursor.execute(
        "insert or replace into master (id, hash) values (?, ?)",
        (1, hashed_password)
    )
    conn.commit() # without this changes won't be saved
    show_menu()

def check_old_master_password():
    password = input("Enter master password: ")
    cursor.execute("select hash from master where id = 1")
    master_password = cursor.fetchone()[0] # (hash, 0) hash is a byte
    is_correct = verify_password(password, master_password)
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
        case '4': 
            conn.close()
            sys.exit()
        case _: 
            print("Please enter correct input")
            show_menu()

def view_passwords():
    cursor.execute("select name, password from passwords")
    rows = cursor.fetchall() # rows is a list of tuple corresponding to each row
    for i, (name, password) in enumerate(rows):
        print(f"{i + 1}. {name} => {password}")
    show_menu()

def manage_new_password():
    name = input("Enter name for new password: ")
    password = input("Enter the password to be saved: ")
    cursor.execute(
        "insert or replace into passwords (name, password) values (?, ?)",
        (name, password)
    )
    conn.commit() # without this changes won't be saved
    show_menu()


cursor.execute("select hash from master where id = 1")
master_password = cursor.fetchone()

if not master_password:
    create_new_master_password()
else:
    check_old_master_password()