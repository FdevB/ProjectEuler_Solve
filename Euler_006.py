sum_squares = 0
squares_sum = 0

for i in range(1, 101):
    power_1 = i ** 2
    sum_squares += power_1

squares_sum = (100 * 101 / 2) ** 2

Answer = squares_sum - sum_squares

print (f"Answer---->> {Answer:.0f}")