# Question 2 - Compute Average and Sum of inputted numbers
index = 1
total = 0
avg = total // index
num = int(input(f"Please enter a number #{index}: "))

while num >= 0:
    total += num
    avg = total // index
    index += 1
    num = int(input(f"Please enter a number #{index} (avg={avg}. sum={total}): "))

print("Thank You Goodbye!")


