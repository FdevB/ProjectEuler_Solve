def multiple(number):
    if number % 3 == 0 or number % 5 == 0:
        return True
    else:
        return False

sum = 0

for i in range(1, 1000):
    if multiple(i):
        sum += i

print(f"Answer---->> {sum}")