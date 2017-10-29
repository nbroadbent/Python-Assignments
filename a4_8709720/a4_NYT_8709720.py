# Family name: Nicholas Broadbent
# Course: IT1 1120 
# Assignment Number 4

def valid_input(x):
    ''' (str)->str

    This function takes in a string as input and checks if it is valid input
    (a number or it is Q or q) and returns it if it's valid. Otherwise it will
    keep asking for input.
    '''
    if str(x).isdigit():
        if 0 < int(x) < 7:
            return x
        print("\nInvalid input, try again\n")
    elif x == 'Q' or x == 'q':
        return x
    else:
        print("\nIf you answer is not Q or q, then it must be an integer.\nInvalid input, try again\n")
    
    return valid_input(input("Answer (1, 2, 3, 4, 5, 6, Q or q): "))

def menu():
    ''' (None)->None

    Prints a menu to the user, and calls the right functions to do what the user wants.
    '''
    
    books = []
    f = []
    
    while True:
        # Print menu
        print("===================================================")
        print("What would you like to do? Enter 1, 2, 3, 4, 5, 6 or Q for answer.")
        print("1: Look up year range")
        print("2: Look up month/year")
        print("3: Search for author")
        print("4: Search for title")
        print("5: Number of authors with at least x bestsellers")
        print("6: List y authors with the most bestsellers")
        print("Q: Quit")
        print("===================================================")

        # Get and validate input
        choice = valid_input(input("Answer (1, 2, 3, 4, 5, 6, Q or q): "))

        # Check if user wants to quit
        if choice == 'Q' or choice == 'q':
            break
        
        # Check if choice is a number
        if choice.isdigit():
            choice = int(choice)

        # Read file once
        if books == []:
            books = read__parse_file('bestsellers.txt')
            
            # Change dates
            for i in range(len(books)):
                j = books[i][3].strip().split('/')

                # Make months 2 digits
                try:
                    if int(j[0]) < 10:
                        j[0] = '0'+j[0]
                    if int(j[1]) < 10:
                        j[1] = '0'+j[1]
                except ValueError:
                    pass
                
                # Make date (year-month-day)
                books[i][3] = j[2]+'-'+j[0]+'-'+j[1]
                
            # Sort the list by date
            books.sort(key=lambda x: x[3])

        #[print(books[i][3]) for i in range(len(books)-1) if books[i][3][:4] == books[i+1][3][:4] and books[i][3][5:7] == books[i+1][3][5:7]]

        # Do choice
        if choice == 1:
            find_year_range(books)
        elif choice == 2:
            find_month_year(books)
        elif choice == 3:
            search_author(books)
        elif choice == 4:
            search_title(books)
        elif choice == 5:
            f = min_num_bestsellers(books, f)
        elif choice == 6:
            f = y_most_bestsellers(books, f)

        # Wait for user
        input("\nPress Enter to continue...\n\n\n")


def read__parse_file(path):
    ''' (str)-> 2D_list

    This function takes in a string, path,
    and reads from the file that the path leads to.
    
    Returns a 2D list of the file where each list is
    one line from the file and each element of a list is
    parsed by tab in the file.

    Preconditions: path must include the file extension.
    '''
    return [line.strip().split('\t') for line in open(path, 'r')]
        
# Choice 1
def find_year_range(books):
    ''' (2D_list)-> None

    Prompts the user for two years (a starting year and an ending year),
    then display all books which reached the #1 spot between those two years (inclusive).

    Preconditions: books is a sorted list.
    '''
    start_year = ''
    end_year = ''

    #Search algorithm for choice 1
    def two_year_search():
        ''' (None)->None

        This function does a binary search to find the index of the starting year,
        then does an O(k) loop to find and print the books until it reaches
        the end year (inclusively).
        '''

        # Check years
        if start_year > end_year:
            print("No books found in that range of years.")
            return None

        # Variables
        t = 0
        b = len(books)
        x = b//2
        found = False

        # Binary search to find starting index
        while True:
            if books[x][3][:4] > start_year:
                # Ignore the part of the list below books[x-1]
                b = x-1
            elif books[x][3][:4] < start_year:
                #Ignore the part of the list above books[x+1]
                t = x+1
            elif books[x][3][:4] == start_year:
                # Ensure this index is the beginning
                if books[x-1][3][:4] == start_year:
                    b = x-1
                else:
                    # Starting position found!
                    break
            x = (t+b)//2

            # Check for end of search
            if t == b:
                break
        
        # Linear search to display books from starting year to end year
        while x < len(books):
            # Check if we've gone out of year range
            if end_year < books[x][3][:4]:
                break
            print('\n'+books[x][0] + ', ' + books[x][1] + ' (' + books[x][3] + ')\n')
            x += 1
            found  = True

        # Check if we found any books
        if not(found):
            print("No books found in that range of years.")

    # Get years
    while True:
        start_year = input("Enter beginning year: ")
        if start_year.isdigit() and len(start_year) == 4:
            break
        print("\nPlease give a four digit integer for the year.\n")
    while True:
        end_year = input("Enter ending year: ")
        if end_year.isdigit() and len(end_year) == 4:
            break
        print("\nPlease give a four digit integer for the year.\n")

    # Search
    two_year_search()
    
# Choice 2
def find_month_year(books):
    ''' (2d_list)- None

    Prompts the user for a month and a year, then prints all of the books
    in the 2d list that are found in that month of the year.
    '''
    
    month = ''
    year = ''

    # Search algorith for choice 2
    def month_year_search():
        ''' (None)->None

        This function does a binary search to find the index starting year,
        the uses linear search to find and print the books until it reaches
        the end year (inclusively).
        '''
        
        t = 0
        b = len(books)
        x = b//2
        found = False

        # Binary search to find starting index
        while True:
            if books[x][3][:4] > year:
                # Ignore the part of the list below books[x-1]
                b = x-1
            elif books[x][3][:4] < year:
                #Ignore the part of the list above books[x+1]
                t = x+1
            elif books[x][3][:4] == year:
                # Ensure this index is the beginning
                if books[x][3][5:7] > month:
                    b = x-1
                elif books[x][3][5:7] < month:
                    #Ignore the part of the list above books[x+1]
                    t = x+1
                elif books[x][3][5:7] == month:
                    # Check before it for same month
                    if books[x-1][3][5:7] == month:
                        b = x-1
                    else:
                        # Starting position found!
                        break
            x = (t+b)//2

            # Check for end of search
            if t == b:
                break
        
        # Linear search to display books from entire month of year
        while x < len(books):
            # Check if we've gone out of month range
            if month < books[x][3][5:7] or year < books[x][3][:4]:
                break
            print('\n'+books[x][0] + ', ' + books[x][1] + ' (' + books[x][3] + ')\n')
            x += 1
            found = True

        # Check if we found any books
        if not(found):
            print("No books found in that month of year.") 
        
    # Get valid month
    while True:
        month = input('Enter month (as an integer, 1-12): ')
        try:
            if 12 < int(month) or int(month) < 1:
                print('\nInvalid month. Must be interger, 1-12. Try again\n')
            else:
                break
        except ValueError:
            print('\nMonth must be an integer.\nInvalid month. Must be interger, 1-12. Try again\n')
    # Get valid year
    while True:
        year = input('Enter year: ')
        try:
            x = int(year)
            if len(year) != 4 or int(year) < 0:
                print('\nPlease give a four digit integer for the year.\n')
            else:
                break
        except ValueError:
            print('\nYear must be an integer.\nPlease give a four digit integer for the year.\n')
            
    if int(month) < 10:
        month = '0'+month
        
    month_year_search()            
    
#Choice 3
def search_author(books):
    ''' (2D_list)->None

    Prompts the user for a string, then display all books whose
    author’s namecontains that string (regardless of case). 
    '''
    found = False
    
    # Get name to be searched
    name = input("Enter an author's name (or part of a name): ").lower()

    # Search for name
    for i in range(len(books)):
        if name in books[i][1].lower():
            print('\n'+books[i][0]+', by ' + books[i][1] + ' (' + books[i][3]+')\n')
            found = True
    if not(found):
        print('\nNo books found by an author whose name contains: '+name)

# Choice 4
def search_title(books):
    ''' (2D_list)->None

    Prompts the user for a string, then display all books whose
    title contains that string (regardless of case). 
    '''
    found = False
    
    # Get title to be searched
    title = input("Enter a title (or part of a title): ").lower()
    
    # Search for title
    for i in range(len(books)):
        if title in books[i][0].lower():
            print('\n'+books[i][0]+', by ' + books[i][1] + ' (' + books[i][3]+')\n')
            found = True
    if not(found):
        print('\nNo books found with title that contains: '+title)
        
# Choice 5
def min_num_bestsellers(books, f=[]):
    ''' (2D_list, [2D_list])->2D_list

    Prompts the user for a string, then displays all of the books
    whose title contains that string (regardless of case).

    Takes up to 2 arguments.

    If only 1 argument is passed, then the function will find the
    frequency of authors in the 2d list books. Otherwise, if another
    2d list for f is passed, then the function will use that list as
    the frequency list instead of finding it.

    Preconditions:

    f is a 2d list where element 1 and 2 of each list in f
    is a string and int, repsectively.
    '''
    x = 0

    # Get valid input
    while True:
        x = input("Enter an integer bigger than zero: ")
        if x.isdigit():
            x = int(x)
            if x > 0:
                break
        try:
            int(x)
            print("\nNumber must be at least one. Try again\n")
        except ValueError:
            print("\nNumber must be an integer.\nNumber must be at least one. Try again\n")

    # Don't find frequency of of authors if we already did it
    if f == []:
        f = frequency(books)

    # Print authors
    print("\nThe list of authors with at least "+ str(x) +" NYT bestsellers is:")
    [print(str(i+1)+'.', f[i][0] + ' with ' + str(f[i][1]) + ' bestsellers') for i in range(len(f)) if f[i][1] >= x]

    # Keep the frequency list
    return f

# Choice 6
def y_most_bestsellers(books, f=[]):
    ''' (2D_list)->2D_list

    Takes in a 2d list of books and prompts the user for an integer y
    and prints y authors with the most best sellers.

    Optional: second argument, 2d list,  frequency: where f = [[authors, frequency]]

    returns a 2d list of authors and their frequency.
    '''
    y = 0

    # Get valid input
    while True:
        y = input("Enter an integer bigger than zero: ")
        if y.isdigit():
            y = int(y)
            if y > 0:
                break
        try:
            int(y)
            print("\nNumber must be at least one. Try again\n")
        except ValueError:
            print("\nNumber must be an integer.\nNumber must be at least one. Try again\n")

    # Don't find frequency of of authors if we already did it
    if f == []:
        f = frequency(books)

    # Print authors
    print('Top ', y,' authors by the number of NYT bestsellers is: \n')
    
    for i in range(y):
        if i >= len(f):
            break
        print(str(i+1)+'.', f[i][0])

    # Keep the frequency list
    return f

def frequency(books):
    '''(2D_list)->2D_list

    Counts the frequency of every author in a 2d list
    and returns a sorted 2d list of authors and their frequency.

    Sorted from highest to lowest.

    [author, frequency]
    '''
    
    f=[]

    # Find the frequency of authors
    for i in range(len(books)):
        flag=False
        for j in range(len(f)):
            if books[i][1].strip() == f[j][0]:
                f[j][1] = f[j][1]+1
                flag = True
        if not(flag):
            f.append([books[i][1], 1])
    # Let's sort this list by descending order of frequency
    f.sort(key=lambda x: x[1], reverse=True)
    return f

# MAIN
menu()
