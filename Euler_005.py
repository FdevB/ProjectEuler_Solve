def divisible(number):
    for i in range(2, 21):
        if number % i != 0:
            return False
    return True

test_number = 40

while True:
    if divisible(test_number):
        print(f"Answer---->> {test_number}")
        break
    test_number += 1