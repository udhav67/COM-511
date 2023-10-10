def is_armstrong(n):
    num = n
    power = len(str(n))
    sum_of_cubes = sum(int(digit) ** power for digit in str(n))
    return sum_of_cubes == num

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
