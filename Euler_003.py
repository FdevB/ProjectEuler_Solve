def large(number):
    factor = 2
    while factor * factor <= number:
        if number % factor == 0:
            number //= factor
        else:
            factor += 1
    return number

our_number = 600851475143
print(f"Anwer ---->> {large(our_number)}")