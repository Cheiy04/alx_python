def convert_to_integer_or_string(value):
    if isinstance(value, str):
        if value.isdigit():  # Checking if the string contains only digits
            return int(value)  
        else:
            return value
    elif isinstance(value, int):
        return value
    else:
        return "Unsupported type"

