def prime(number):
    for i in range(2, int((number / 2) + 1)):
        if number % i == 0:
            return False
    return True

sum = 0
for numbers in range(3, 2000000, 2):
    if prime(numbers):
        sum += numbers

print(f"Answer---->> {sum + 2}")