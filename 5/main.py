def reverse_string(s):
    # Em python as strings são imutáveis, caso contrário seria possível 
    # tratar como uma lista de caracteres e ter uma complexidade de O(n/2) ao invés de O(n)
    reversed = ''
    for i in range(len(s) - 1, -1, -1):
        reversed += s[i]
    return reversed

def main():
    print(reverse_string("Hello, World!"))

if __name__ == "__main__":
    main()
