a = 10
b = 3
print( a + b)        # 10 + 3 = 13
print( a - b)        # 10 - 3 = 7
print( a * b)        # 10 * 3 = 30
print( a / b)        # 10 / 3 = 3.33...
print(a % b)         # 10 % 3 = 1
print(a ** b)        # 10^3 = 1000
print( a // b)       # 10 // 3 = 3





# Multiplication Table Generator

num = int(input("Enter a number: "))

print(f"\nMultiplication Table for {num}\n")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
