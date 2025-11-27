#login function
#Auth system using dictionary to store user credentials



def login_system(user_db):
    print("Please enter username and password to log in.")
    username = input("Username: ")
    password = input("Password: ")
    try:
        if username in user_db and user_db[username]['password'] == password:
            print("Auth successful!")
            return True
        else:
            print("Incorrect password. Please try again.")
            return False

    except KeyError:
        print("Username not found. Please try again.")
        return False
