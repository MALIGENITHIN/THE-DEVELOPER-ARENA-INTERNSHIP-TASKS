# Program to calculate average of numbers

# Take input from user
numbers = list(map(float, input("Enter numbers separated by space: ").split()))

# Calculate average
average = sum(numbers) / len(numbers)

print("Average =", average)
