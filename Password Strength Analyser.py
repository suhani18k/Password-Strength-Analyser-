
print("   SIMPLE PASSWORD STRENGTH CHECKER ")

attempt = 1

while True:
    print("Attempt Number:", attempt)

    password = input("Enter your password: ")
    confirm = input("Confirm your password: ")

    if password != confirm:
        print("\nPasswords do not match. Try again.\n")
        attempt += 1
        continue

    
    length = len(password)    
    print("\nPassword Length:", length)

   
    has_digit = False
    has_upper = False
    has_lower = False

    digit_count = 0
    upper_count = 0
    lower_count = 0

    
    for ch in password:
        if ch.isdigit():
            has_digit = True
            digit_count += 1
        elif ch.isupper():
            has_upper = True
            upper_count += 1
        elif ch.islower():
            has_lower = True
            lower_count += 1

    
    print("Digits count:", digit_count)
    print("Uppercase letters count:", upper_count)
    print("Lowercase letters count:", lower_count)

    

    
    if length < 6:
        strength = "WEAK"

    elif length >= 8 and has_digit and has_upper and has_lower:
        strength = "STRONG"

    elif length >= 6 and has_digit:
        strength = "MEDIUM"

    else:
        strength = "WEAK"

    print("\nPassword Strength:", strength)

    
    print("\nPassword Suggestions:")
    if not has_digit:
        print("- Add at least one number")
    if not has_upper:
        print("- Add an uppercase letter")
    if not has_lower:
        print("- Add a lowercase letter")
    if length < 8:
        print("- Increase password length")

    if strength == "STRONG":
        print("Your password is good ")

   
    choice = input("\nDo you want to check another password? (yes/no): ")
    if choice.lower() != "yes":
        print("\nThank you for using the Password Strength Checker.")
        print("Total Attempts:", attempt)
        break

    attempt += 1
    print("\n-----------------------------------\n")