def validate_password(password):
    if len(password) < 8:
        return False

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_space = False

    for i in password:
        if i.isupper():
            has_uppercase = True
        elif i.islower():
            has_lowercase = True
        elif i.isdigit():
            has_digit = True
        elif i.isspace():
            has_space = True

    if not has_uppercase or not has_lowercase or not has_digit or has_space:
        return False

    return True
