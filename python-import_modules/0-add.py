# Define variables a and b
if __name__ == "__main__":
    a = 1
    b = 2

    # Import the add function from add_0.py
    from add_0 import add

    # Perform the addition and print the result
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))