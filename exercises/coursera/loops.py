# Question 1: Print numbers 1 to 7
number = 1
while number <= 7:
    print(number, end=" ")
    number += 1

print()  # new line

# Question 2: Print numbers from 5 to 0
for number in range(5, -1, -1):
    print(number)

# Question 3: Count digits
def digits(n):
    count = 0
    if n == 0:
        return 1
    while n != 0:
        n //= 10
        count += 1
    return count
