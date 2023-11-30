# function called validate_password that takes a password as input
def validate_password(password):

    if len(password) < 8:
        return False
    
    return True
    
    has_upper = False
    has_lower = False
    has_digit = False
    has_space = True

    for i in password:
        if i.isupper():
            has_upper = True
        elif i.islower():
            has_lower = True
        elif i.isdigit():
            has_digit = True
        elif i.isspace():
            has_space = False
            
    if not has_digit or not has_space or not has_lower or not has_upper:
        return False

    

p= validate_password("LK0jjjhhjhjh")
print(p)