# Family name: Nicholas Broadbent
# Course: IT1 1120 
# Assignment Number 4

def ap4(m):
    ''' (2d_list)-> 2d_list

    This function takes in a 2d list as input and searches
    for an arithmetic progression containing at least 4 numbers,
    and returns 4 locations in the matrix of one such sequence.

    If sequence found, returns 2d list.
    If sequence not found, returns empty 1d list.

    Precondition: m is a matrix (m will not have rows with different number of elements)
    '''

    vert = False
    hor = False

    # If the matrix has 4 or more columns then check horizontal
    if len(m[0]) >= 4:
        hor = True
    # If the matrix has 4 or more rows then check vertical
    if len(m) >= 4:
        vert = True

    # Check all directions
    if (vert and hor):
        for i in range(len(m)):
            for j in range(len(m[i])-3):
                # Check horizontal
                if m[i][j]-m[i][j+1] == m[i][j+1] - m[i][j+2] == m[i][j+2]-m[i][j+3]:
                    # Arithmetic progression found
                    return print_indices(i, j)
                # Check diagonal
                if i < len(m)-3:
                    # Top-left to bottom-right
                    if m[i][j]-m[i+1][j+1] == m[i+1][j+1]-m[i+2][j+2] == m[i+2][j+2]-m[i+3][j+3]:
                        # Arithmetic progression found
                        return print_indices(i, j, 3)
                    # Top-right to bottom-left
                    if m[i][j+3]-m[i+1][j+2] == m[i+1][j+2]-m[i+2][j+1] == m[i+2][j+1]-m[i+3][j]:
                        return print_indices(i, j+3, 2)
            # Check vertical
            if i < len(m)-3:
                for j in range(len(m[i])):
                    if m[i][j]-m[i+1][j] == m[i+1][j] - m[i+2][j] == m[i+2][j]-m[i+3][j]:
                        # Arithmetic progression found
                        return print_indices(i, j, 1)
    # Check horizontal only
    elif hor:
        for i in range(len(m)):
            for j in range(len(m[i])-3):
                if m[i][j]-m[i][j+1] == m[i][j+1] - m[i][j+2] == m[i][j+2]-m[i][j+3]:
                    # Arithmetic progression found
                    return print_indices(i, j)
    # Check vertical only
    elif vert:
        for i in range(len(m)-3):
            for j in range(len(m[i])):
                if m[i][j]-m[i+1][j] == m[i+1][j] - m[i+2][j] == m[i+2][j]-m[i+3][j]:
                    # Arithmetic progression found
                    return print_indices(i, j, 1)
    # No arithmetic progression patterns found. Return empty list
    return []
        

def print_indices(i, j, direction = 0):
    ''' (int, int, [int])-> 2d_list

    Takes in the starting index of a 2d list and prints 4 indices
    from starting index, vertically, horizontally or diagonally.

    If no 3rd argument passed, the function assumes horizontally.

    Otherwise:
    direction is 1 for vertical and 2 for diagonal (bottom-left to top-right)
    and any integer for diagonal (top-left to bottom-right).
    '''
    
    if direction == 0:
        return [[i, j+k] for k in range(4)]
    elif direction == 1:
        return [[i+k, j] for k in range(4)]
    elif direction == 2:
        return [[i+k, j-k] for k in range(4)]
    else:
        return [[i+k, j+k] for k in range(4)]

    
        
