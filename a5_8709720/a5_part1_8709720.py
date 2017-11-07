# Family name: Nicholas Broadbent
# Student number:  8709720
# Course: IT1 1120 
# Assignment Number 5

### 1a ###
def largest_34(a):
    '''(list)->int

    Returns the sum of the 3rd and 4th largest values in a list, a.
    '''
    
    l = [0]*4
    
    for i in range(len(a)):
        # Check if current item is larger than the current 4 largest
        # Insert item and move others if necessary
        if a[i] > l[0]:
            l[3] = l[2]
            l[2] = l[1]
            l[1] = l[0]
            l[0] = a[i]
        elif a[i] > l[1]:
            l[3] = l[2]
            l[2] = l[1]
            l[1] = a[i]
        elif a[i] > l[2]:
            l[3] = l[2]
            l[2] = a[i]
        elif a[i] > l[3]:
            l[3] = a[i]

    # Return the sum of the 3rd and 4th largest values
    return l[2]+l[3] 

### 1b ###
def largest_third(a):
    '''(list)->int

    Returns the sum of the largest len(a)//3 number of elements in list a
    '''

    # Sort this list
    # n log n
    a.sort(reverse = True)

    # Return the sum
    return sum(a[:(len(a)//3)])

### 1c ###
def third_at_least(a):
    '''(list)->bool

    Return  true of false if a value is in the list at least
    len(a)//3 + 1 times.
    '''

    # Initialise variables
    x = len(a)//3 + 1
    l = []
    flag = False

    for i in a:
        flag = True
        for j in l:
            # Check if value is in the list
            if i == j[0]:
                j[1] += 1
                # Check if frequency is great enough
                if j[1] >= x:
                    return j[0]
                flag = False
        if flag:
            # Add value to the list
            l.append([i, 1])
            flag = False
    # None found
    return None   
            
### 1d ###
def sum_tri(a, x):
    '''(list, int)->bool

    Returns true if 3 numbers add up to equal c
    '''

    # Move from left to right
    for i in range(len(a)):
        # Move j
        for j in range(len(a)):
            # Move k
            for k in range(len(a)):
                # Check if found
                if a[i] + a[j] + a[k] == x:
                    return True
    return False
