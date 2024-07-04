import random
import string

def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    symbols = "{}?@!#$%^&*()_+-"
    
    # Combining all characters
    all_chars = lower + upper + numbers + symbols
    
    # Ensure at least one character from each category
    password = []
    password.append(random.choice(lower))
    password.append(random.choice(upper))
    password.append(random.choice(numbers))
    password.append(random.choice(symbols))
    
    # Generate remaining characters
    password.extend(random.sample(all_chars, length - 4))
    
    # Shuffle the password to ensure randomness
    random.shuffle(password)
    
    # Convert list to string
    password_str = ''.join(password)
    
    return password_str

# Get password length from user
while True:
    try:
        length = int(input("Enter desired password length (minimum 4): "))
        if length < 4:
            print("Password length must be at least 4 characters.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Generate and print password
password = generate_password(length)
print(f"Generated Password: {password}")
