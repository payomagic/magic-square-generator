## OLD - DO NOT USE!!!

# function to check if the square is magic
def is_magic_square(square, magic_sum):
    # check rows
    for i in range(len(square)):
        if sum(square[i]) != magic_sum:
            return False
    
    # check columns
    for i in range(len(square)):
        col_sum = 0
        for j in range(len(square)):
            col_sum += square[j][i]
        if col_sum != magic_sum:
            return False
    
    # check diagonal
    diagonal_sum = 0
    for i in range(len(square)):
        diagonal_sum += square[i][i]
    if diagonal_sum != magic_sum:
        return False
    
    # check secondary diagonal
    secondary_diagonal_sum = 0
    for i in range(len(square)):
        secondary_diagonal_sum += square[i][len(square) - i - 1]
    if secondary_diagonal_sum != magic_sum:
        return False
    
    # check corners
    corner_sum = square[0][0] + square[0][len(square)-1] + square[len(square)-1][0] + square[len(square)-1][len(square)-1]
    if corner_sum != magic_sum*2:
        return False
    
    # if all checks passed, return True
    return True

# get user input for n1, n2, and magic_sum
n1 = int(input("Enter first number (between 1 and 12): "))
n2 = int(input("Enter second number (between 1 and 12): "))
position1 = int(input(f"Enter position for {n1} (1-16): "))
position2 = int(input(f"Enter position for {n2} (1-16 excluding {position1}): "))
magic_sum = int(input("Enter magic sum (between 19 and 49): "))

# create empty square
square = [[0 for i in range(4)] for j in range(4)]

# fill in n1 and n2
square[(position1-1)//4][(position1-1)%4] = n1
square[(position2-1)//4][(position2-1)%4] = n2

# calculate the remaining numbers
remaining_numbers = [i for i in range(1, 13) if i not in [n1, n2]]
i = 0
for row in range(4):
    for col in range(4):
        if square[row][col] == 0:
            square[row][col] = remaining_numbers[i]
            i += 1

# find a magic square with the given sum
while not is_magic_square(square, magic_sum):
    # rotate the remaining numbers
    remaining_numbers.append(remaining_numbers.pop(0))
    i = 0
    for row in range(4):
        for col in range(4):
            if square[row][col] == 0:
                square[row][col] = remaining_numbers[i]
                i += 1

# print the magic square
for row in square:
    print(row)
