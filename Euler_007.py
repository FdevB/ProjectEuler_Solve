def prime(number):
    flag = True
    for i in range(2, int((number/2)+1)):
        if number % i == 0:
            flag = False
    return flag

flag = True
number = 3
prime_number = []

while flag:
    if number % 2 != 0:
        if prime(number):
            prime_number.append(number)
            if len(prime_number) == 10000:
                print(f"Answer---->> {prime_number[-1]}")
                flag = False

    number += 1