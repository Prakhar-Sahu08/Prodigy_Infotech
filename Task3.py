import re

def check_password_strength(password):
    length = len(password)
    score = 0
    
    # Check length
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    
    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
    
    # Check for special characters
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    
    return score

def main():
    while True:
        password = input("Enter your password: ")
        
        strength = check_password_strength(password)
        
        if strength == 0:
            print("Very Weak: Password does not meet any criteria.")
        elif strength == 1:
            print("Weak: Password meets minimal requirements.")
        elif strength == 2:
            print("Moderate: Password meets some requirements but can be improved.")
        elif strength == 3:
            print("Strong: Password is fairly strong but can be further improved.")
        elif strength == 4:
            print("Very Strong: Password is strong and meets most criteria.")
        elif strength == 5:
            print("Excellent: Password is very strong and meets all criteria.")

        another = input("Do you want to check another password? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
