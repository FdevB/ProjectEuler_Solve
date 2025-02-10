def even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
first_number = 1 
second_number = 2
sum = 0

while (first_number < 4000000):
    if even(first_number):
        sum += first_number
        
    new_number = first_number + second_number
    first_number = second_number
    second_number = new_number

print(f"Answr---->> {sum}")