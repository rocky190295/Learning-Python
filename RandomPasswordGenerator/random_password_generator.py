import random
import string

# ------------------------------
# STEP 1: User Input Function
# ------------------------------
def get_user_inputs():
    """
    Prompt the user for password configuration options and return them as a dictionary.
    Returns:
        dict: A dictionary with keys 'length', 'use_upper', 'use_lower', 'use_digits', 'use_special'.
    """
    print("\n--- Password Configuration ---")
    length = int(input("Enter desired password length: "))

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    if not any([use_upper, use_lower, use_digits, use_special]):
        print("\n[!] At least one character type must be selected. Try again.\n")
        return get_user_inputs()

    return {
        'length': length,
        'use_upper': use_upper,
        'use_lower': use_lower,
        'use_digits': use_digits,
        'use_special': use_special
    }

# --------------------------------------
# STEP 2: Password Generation Function
# --------------------------------------
def generate_password(length, use_upper, use_lower, use_digits, use_special):
    """
    Generate a random password based on the configuration provided.
    Returns:
        str: The generated password.
    """
    character_pool = ''
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        return ""

    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

# --------------------------------------
# STEP 3: Password Strength Checker
# --------------------------------------
def check_password_strength(password):
    """
    Analyze the password and return a strength rating.
    Returns:
        str: 'Weak', 'Moderate', or 'Strong'
    """
    score = 0
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score == 4:
        return "Strong"
    elif score == 3:
        return "Moderate"
    else:
        return "Weak"

# --------------------------------------
# STEP 4: Save Password to File
# --------------------------------------
def save_password_to_file(password):
    """
    Save the password to a file named 'saved_passwords.txt'.
    """
    with open("saved_passwords.txt", "a") as file:
        file.write(password + "\n")
    print("\n[+] Password saved to 'saved_passwords.txt'.")

# --------------------------------------------------
# BONUS: Auto-Generate Inputs (Let Computer Choose)
# --------------------------------------------------
def auto_generate_password():
    """
    Auto-generate configuration settings and return a valid config dictionary.
    """
    length = random.randint(12, 18)

    while True:
        include_digits = random.choice([True, False])
        include_symbols = random.choice([True, False])
        include_uppercase = random.choice([True, False])
        include_lowercase = random.choice([True, False])
        
        if any([include_digits, include_symbols, include_uppercase, include_lowercase]):
            break  # Ensure at least one character type is selected

    print("\nAuto-selected configuration:")
    print(f"Length                     : {length}")
    print(f"Include Uppercase          : {include_uppercase}")
    print(f"Include Lowercase          : {include_lowercase}")
    print(f"Include Digits             : {include_digits}")
    print(f"Include Special Characters : {include_symbols}")

    return {
        'length': length, 
        'use_upper': include_uppercase, 
        'use_lower': include_lowercase, 
        'use_digits': include_digits, 
        'use_special': include_symbols
    }

# ------------------------------
# MAIN MENU LOOP
# ------------------------------
def main():
    print("\n==== Welcome to the Password Generator ====")

    while True:
        print("\n--- Main Menu ---")
        print("1. Generate password (manual inputs)")
        print("2. Check password strength")
        print("3. Auto-generate password (computer chooses)")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            config = get_user_inputs()
            password = generate_password(**config)
            print(f"\nGenerated Password: {password}")
            strength = check_password_strength(password)
            print(f"Password Strength : {strength}")

            if input("\nWould you like to save this password? (y/n): ").lower() == 'y':
                save_password_to_file(password)

        elif choice == '2':
            user_pass = input("\nEnter a password to check strength: ")
            print(f"Strength: {check_password_strength(user_pass)}")

        elif choice == '3':
            config = auto_generate_password()
            password = generate_password(**config)
            print(f"\nAuto-Generated Password: {password}")
            strength = check_password_strength(password)
            print(f"Password Strength        : {strength}")

            if input("\nWould you like to save this password? (y/n): ").lower() == 'y':
                save_password_to_file(password)

        elif choice == '4':
            print("\nThanks for using the Password Generator. Goodbye! \U0001F44B")
            break

        else:
            print("\n[!] Invalid option. Please try again.")


if __name__ == "__main__":
    main()
