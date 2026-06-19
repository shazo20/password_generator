import string
import secrets
import pyperclip


def password_generator(count, is_letter, is_punc):
    password_list = []
    characters = string.digits
    minimum_length = 1
    if not count:
        count = 8
    password_list.append(secrets.choice(string.digits))
    minimum_length += 1
    if is_letter.lower() == "y":
        password_list.append(secrets.choice(string.ascii_lowercase))
        password_list.append(secrets.choice(string.ascii_uppercase))
        minimum_length += 2
        characters += string.ascii_letters
    if is_punc.lower() == "y":
        password_list.append(secrets.choice(string.punctuation))
        minimum_length += 1
        characters += string.punctuation
    if count < minimum_length:
        raise ValueError(f"Password length must be at least {minimum_length}")
    for _ in range(count - len(password_list)):
        password_list.append(secrets.choice(characters))
    secure_random = secrets.SystemRandom()
    secure_random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    return password


try:
    count = int(input("How long your password should be: "))
    is_letter = input("Use letters in password (Y/n): ")
    is_punctuation = input("Use punctuations in password (Y/n): ")
    if not is_letter:
        is_letter = "y"
    if not is_punctuation:
        is_punctuation = "y"

    print(
        f"Your passsword is: {password_generator(count, is_letter, is_punctuation)}\n it is copied to clipboard and ready to paste."
    )

except Exception as e:
    print(f"Error: {e}")
    exit(1)
