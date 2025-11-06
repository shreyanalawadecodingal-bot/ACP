import random
import string

# Function to generate a random password
def generate_password(length):
    # Characters to include in the password
    letters = string.ascii_letters   # a-z + A-Z
    digits = string.digits           # 0-9
    symbols = string.punctuation     # Special characters like !,@,#

    # Combine all characters
    all_chars = letters + digits + symbols

    # Randomly choose characters from the combined set
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# Main program
password_length = int(input("Enter the desired password length: "))
password = generate_password(password_length)
print("Generated Password:", password)
