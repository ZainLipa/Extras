def is_armstrong_number(num):
    #Calculate the number of digits in number
    num_str = str(num)
    num_digits = len(num_str)
     
    #Calculate the sum of the cubes of each digit
    digit_sum = sum(int(digit)**num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return digit_sum == num

num = int(input("Enter a positive integer: "))

if is_armstrong_number(num):
    print(num, "number is an Armstrong number.")
else:
    print(num, "number is not an Armstrong number.")
