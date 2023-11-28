def fibonacci_sequence(n):
    if n < 0:
        return []

    result = []
    a = 0
    b = 1

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result