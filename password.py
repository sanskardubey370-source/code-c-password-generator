import random
import string

def generate_password():
    print("--- Password Generator Project ---")
    
    # Getting the length of the password from the user
    # Using a try-except block to handle if they type letters instead of numbers
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Invalid input! Using default length of 12.")
        length = 12

    # These are the variables based on what the user wants
    # I'm asking 'y' or 'n' for each option
    use_digits = input("Include numbers? (y/n): ").lower()
    use_special = input("Include special characters? (y/n): ").lower()
    
    # Combining all the characters into one big string
    # Always including letters (uppercase and lowercase) by default
    characters = string.ascii_letters 
    
    if use_digits == 'y':
        characters += string.digits
        
    if use_special == 'y':
        characters += string.punctuation

    # The password variable starts empty
    password = ""
    
    # Loop for the length of the password
    # In every iteration, I pick one random character from my 'characters' list
    for i in range(length):
        random_char = random.choice(characters)
        password += random_char

    print("\n-----------------------------")
    print("Your Password is:", password)
    print("-----------------------------")

# Calling the function to run the program
generate_password()