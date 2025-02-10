for c in range(334, 500):
    for a in range(1, int((1000 - c) / 2)):
        b = (1000 - c) - a

        if a ** 2 + b **2 == c **2:
            print(f"Answer---->> {a * b * c}")