import random
import string

print("=" * 50)
print("            RANDOM PASSWORD GENERATOR")
print("=" * 50)

while True:
    try:
        length = int(input("\nEnter Password Length: "))

        if length < 4:
            print("Password length should be at least 4.")
            continue

        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        digits = string.digits
        special = string.punctuation

        all_characters = uppercase + lowercase + digits + special

        password = []

        password.append(random.choice(uppercase))
        password.append(random.choice(lowercase))
        password.append(random.choice(digits))
        password.append(random.choice(special))

        for i in range(length - 4):
            password.append(random.choice(all_characters))

        random.shuffle(password)

        final_password = "".join(password)

        print("\nGenerated Password:")
        print(final_password)

        print("\nPassword Analysis")
        print("-" * 30)

        print("Length :", len(final_password))

        upper_count = 0
        lower_count = 0
        digit_count = 0
        special_count = 0

        for char in final_password:
            if char.isupper():
                upper_count += 1
            elif char.islower():
                lower_count += 1
            elif char.isdigit():
                digit_count += 1
            else:
                special_count += 1

        print("Uppercase Letters :", upper_count)
        print("Lowercase Letters :", lower_count)
        print("Numbers           :", digit_count)
        print("Special Characters:", special_count)

        if length >= 12:
            print("Password Strength : Strong")
        elif length >= 8:
            print("Password Strength : Medium")
        else:
            print("Password Strength : Weak")

        choice = input("\nGenerate Another Password? (yes/no): ")

        if choice.lower() != "yes":
            print("\nThank You For Using Password Generator!")
            break

    except ValueError:
        print("Please enter a valid numeric value.")