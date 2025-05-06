def generate_fibonacci_sequence(num_terms):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(num_terms):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

