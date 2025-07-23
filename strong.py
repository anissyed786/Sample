import math

def is_strong_number(num):
    """
    Checks if a number is a strong number.
    """
    if num < 0:
        return False
    
    original_num = num
    sum_of_factorials = 0
    
    # Calculate factorials of digits and sum them
    while num > 0:
        digit = num % 10
        sum_of_factorials += math.factorial(digit)
        num //= 10
        
    return sum_of_factorials == original_num

# Iterate from 1 to 5000 and print strong numbers
print("Strong numbers between 1 to 5000:")
for i in range(1, 5000):
    if is_strong_number(i):
        print(i)