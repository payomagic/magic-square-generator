## OLD - DO NOT USE!!!


def generate_magic_square(n1, n2, magic_sum):
    # Calculate the third number based on the sum of maximum possible combinations
    n3 = magic_sum - n1 - n2
    
    # Initialize the magic square matrix
    magic_square = [[0 for x in range(4)] for y in range(4)]
    
    # Set the chosen numbers in the matrix
    magic_square[0][0] = n1
    magic_square[3][3] = n2
    
    # Set the third number in the matrix
    magic_square[0][1] = n3 - n2 + n1
    magic_square[0][3] = n3 - n1 + n2
    magic_square[3][0] = n3 - n2 + n1
    magic_square[3][2] = n3 - n1 + n2
    
    # Set the remaining numbers in the matrix
    for i in range(4):
        for j in range(4):
            if i == 0 and j not in [0, 1, 3]:
                magic_square[i][j] = n3 - magic_square[i][0] - magic_square[i][1] - magic_square[i][3]
            elif i == 3 and j not in [0, 2, 3]:
                magic_square[i][j] = n3 - magic_square[i][0] - magic_square[i][2] - magic_square[i][3]
            elif j == 0 and i not in [0, 3]:
                magic_square[i][j] = n3 - magic_square[0][j] - magic_square[3][j] - magic_square[i][3]
            elif j == 3 and i not in [0, 3]:
                magic_square[i][j] = n3 - magic_square[0][j] - magic_square[3][j] - magic_square[i][0]
            elif i == 1 and j == 1:
                magic_square[i][j] = n3 - magic_square[0][0] - magic_square[0][1] - magic_square[1][3]
            elif i == 1 and j == 3:
                magic_square[i][j] = n3 - magic_square[0][3] - magic_square[0][1] - magic_square[1][0]
            elif i == 2 and j == 0:
                magic_square[i][j] = n3 - magic_square[3][0] - magic_square[3][2] - magic_square[2][3]
            elif i == 2 and j == 3:
                magic_square[i][j] = n3 - magic_square[3][3] - magic_square[3][2] - magic_square[2][0]
    
    return magic_square

# Example usage:
n1 = int(input("Enter the first number (between 1 and 12): "))
n2 = int(input("Enter the second number (between 1 and 12): "))
magic_sum = int(input("Enter the sum of maximum possible combinations (between 19 and 49): "))

magic_square = generate_magic_square(n1, n2, magic_sum)

# Print the generated magic square
for row in magic_square:
    print(row)
 
