userPassword = "HelpMe!!"
numberOfTries = 3
while numberOfTries > 0:
    enteredPassword = input("Enter the password: ")
    if enteredPassword == userPassword:
        print("Password is correct")
        break
    else:
        print("Passwords do not match. Try again")
        numberOfTries -= 1