# Question 1 - Find all divisible numbers
num = int(input("Please enter a number: "))

# We divide the inputted number by two to cut on runtime.
for i in range(1, num // 2 + 1):

    # Check if the current number can divide the inputted number.
    if num % i == 0:
        print(i)

print(num)
