# Secure Password Generator 🔐

A secure password generator built with Python using the `secrets` module for cryptographically strong random password generation.

This tool generates strong passwords with customizable length and character types, ensuring security by enforcing minimum character requirements.

---

## Features

* Generate secure passwords using Python's `secrets` module
* Includes at least:

  * 1 digit
  * 1 lowercase letter (optional)
  * 1 uppercase letter (optional)
  * 1 punctuation/special character (optional)
* Custom password length
* Automatic clipboard copy using `pyperclip`
* Input validation with clear error handling

---

## Requirements

* Python 3.8+
* Required package:

```bash
pip install pyperclip
```

---

## How It Works

The generator ensures that every password contains required character categories based on user input.

### Character sets used:

* Digits → `string.digits`
* Letters → `string.ascii_letters`
* Lowercase → `string.ascii_lowercase`
* Uppercase → `string.ascii_uppercase`
* Symbols → `string.punctuation`

The password is built in 3 steps:

1. Add required characters
2. Fill remaining length with random characters
3. Shuffle the password to randomize character positions

---

## Usage

Run the script:

```bash
python password_generator.py
```

Example:

```text
How long your password should be: 16
Use letters in password (Y/n): y
Use punctuations in password (Y/n): y
```

Example output:

```text
Your password is: 7@fK9!Lm2#Qw8$Er
It is copied to clipboard and ready to paste.
```

---

## Project Structure

```text
password-generator/
│
├── password_generator.py
└── README.md
```

---

## Function Overview

### `password_generator(count, is_letter, is_punc)`

Generates a secure password.

### Parameters

| Parameter | Type | Description                 |
| --------- | ---- | --------------------------- |
| count     | int  | Desired password length     |
| is_letter | str  | Include letters (`Y/n`)     |
| is_punc   | str  | Include punctuation (`Y/n`) |

### Returns

```python
str
```

Generated password string.

---

## Security Notes

* Uses `secrets.choice()` for secure random selection
* Uses `SystemRandom.shuffle()` for secure shuffling
* Safer than using Python's `random` module for password generation


## License

MIT License
