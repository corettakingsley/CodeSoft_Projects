import random
import string

# Define character sets
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digit_numbers = "0123456789"
symbols = "!@#$%^&*(){}[]/"

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    characters = ''

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += symbols

    if not characters:
        print("You must select at least one character type (uppercase, lowercase, digits, or symbols).")
        return None

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Get user input for the password length and character types
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Password length must be greater than 0.")
            return
        
        # Get character type preferences from the user
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        # Generate and display the password
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
        if password:
            print(f"Generated password: {password}")
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
