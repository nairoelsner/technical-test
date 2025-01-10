def is_fibonacci_number(n):
    if n < 0:
        return False

    # Inicia a sequência de Fibonacci
    a, b = 0, 1

    while a <= n:
        if a == n:
            return True
        a, b = b, a + b

    return False

def main():
    print(is_fibonacci_number(13)) # True
    print(is_fibonacci_number(14)) # False

if __name__ == "__main__":
    main()
