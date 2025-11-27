#sign up function
# This function handles user sign-up by collecting user details and storing them securely in a dictionary.


def signup_system(user_db):

    print("Please enter the following details to sign up.")
    try:
        while True:
            username = input("Username: ")

            #username validation
            if ' ' in username or username.isdigit():
                print("Invalid username. Username should not contain spaces or be entirely numeric.")

            else:
                break

        while True:
            password = input("Password: ")

            #password validation
            #password mix of letters and numbers
            if password.isalpha() or password.isdigit():
                print("Invalid password. Password should be a mix of letters and numbers.")

            else:
                break


        while True:
            age = input("Age: ")

            #age validation
            if not age.isdigit() or int(age) <= 0:
                print("Invalid age. Please enter a valid positive number for age.")

            else:
                break

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

    # Check if username already exists
    if username in user_db:
        print("Username already exists. Please try a different username.")
        return False

    # Store user details in the dictionary
    user_db[username] = {
        'password': password,
        'age': age
    }


    print("Sign-up successful! You can now log in with your credentials.")
    return True


