DATA = {
    'SP': 67_836.43,
    'RJ': 36_678.66,
    'MG': 29_229.88,
    'ES': 27_165.48,
    'Outros': 19_849.53
}


def main():
    total = 0

    for value in DATA.values():
        total += value

    for key, value in DATA.items():
        participation_percent = (value / total) * 100
        print(f'{key}: {participation_percent:.2f}%')

if __name__ == "__main__":
    main()