def convert_to_integer_or_string(a):
    if isinstance(a, str):
        if a.isdigit() or int(a) < 0:  # Checking if the string contains only digits
            return int(a)  
        else:
            return a
    elif isinstance(a, int):
        return a
    else:
        return "Unsupported type"

