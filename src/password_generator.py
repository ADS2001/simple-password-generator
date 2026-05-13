import random

def generate_password(length):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    try:
        length = int(input("Enter the desired password length (at least 8 characters): "))
        password = generate_password(length)
        print(f"Generated Password: {password}")

        input("\nPress Enter to exit...")
    except ValueError as e:
        print(e)
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()