def palindrom(number):
    number = str(number)
    if number[0:] == number[::-1]:
        return True
    else:
        return False

palindrom_number = []

for i in range(100, 1000):
    for k in range(100, 1000):
        if palindrom(i*k):
            result = i * k
            palindrom_number.append(result)

print(f"anwer---->> {max(palindrom_number)}")