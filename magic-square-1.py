import random

# Get input from spectators
p = int(input("Enter the first random number between 1 and 12: "))
w = int(input("Enter the second random number between 1 and 12: "))

# Get input from magician
n = int(input("Enter the sum 'n' between 18 and 49: "))
while n < 18 or n > 49:
    n = int(input("Invalid input. Enter the sum 'n' between 18 and 49: "))

# Generate magic square
square = [[0 for x in range(4)] for y in range(4)]
square[0][0] = p
square[3][3] = w
square[2][2] = (n - p - w) // 2
square[1][1] = n - square[0][0] - square[2][2]
square[1][2] = n - square[1][1] - square[1][0]
square[2][1] = n - square[2][2] - square[2][0]
square[0][1] = n - square[1][1] - square[2][1]
square[1][3] = n - square[1][0] - square[1][1]
square[2][3] = n - square[2][2] - square[2][1]
square[3][1] = n - square[2][1] - square[1][1]
square[0][2] = n - square[0][0] - square[0][1]
square[0][3] = n - square[0][0] - square[0][2]
square[3][2] = n - square[3][3] - square[3][1]
square[3][0] = n - square[3][3] - square[3][2]

# Print magic square
print("Magic square with sum", n)
for i in range(4):
    for j in range(4):
        print(square[i][j], end="\t")
    print()
