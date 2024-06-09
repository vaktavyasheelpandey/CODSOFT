import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length for the password:"))
        if length < 1:
            raise ValueError("Password length must be at least 1.")
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError as ve:
        print(f"Invalid input: {ve}")

if __name__ == "__main__":
    main()