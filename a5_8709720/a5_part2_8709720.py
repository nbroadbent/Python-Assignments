# Family name: Nicholas Broadbent
# Student number:  8709720
# Course: IT1 1120 
# Assignment Number 5

class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle(Point):
    'class that represents a rectangle in a plane'

    def __init__(self, p1, p2, colour):
        '''(Rectangle, number, number, str)->None
    
        Initialise rectangle.
        '''
        
        self.p1 = p1
        self.p2 = p2
        self.colour = colour

    def __eq__(self, y):
        '''(Rectangle, Rectangle)->bool

        Returns true if both rectangles are equal
        '''
    
        if self.p1 == y.p1 and self.p2 == y.p2 and self.colour == y.colour:
            return True
        return False

    def __str__(self):
        '''(Rectangle)->str

        Returns a nice string of rectangle
        '''
        
        return 'I am a '+self.colour+' rectangle with bottom left corner at ('+str(self.p1.x)+', '+str(self.p1.y)+') and top right corner at ('+str(self.p2.x)+', '+str(self.p2.y)+').'

    def __repr__(self):
        '''(Rectangle)->str

        Returns string of object
        '''
        
        return "Rectangle("+str(self.p1)+","+str(self.p2)+",'"+self.colour+"')"
    
    def get_bottom_left(self):
        '''(Rectangle)->Point

        Returns bottom-left point.
        '''

        # Return the point
        return self.p1

    def get_top_right(self):
        '''(Rectangle)->Point

        Returns top-right point.
        '''

        # Return the point
        return self.p2

    def get_color(self):
        '''(Rectangle)->str

        Returns colour or rectangle.
        '''

        # Return the colour
        return self.colour

    def reset_color(self, colour):
        '''(Rectangle, str)->None

        Sets colour of rectangle
        '''

        # Set the colour
        self.colour = colour

    def get_perimeter(self):
        '''(Rectangle)->number

        Returns perimeter of rectangle
        '''

        # Return perimeter
        return (self.p2.x - self.p1.x)*2 + (self.p2.y - self.p1.y)*2
        
    def get_area(self):
        '''(Rectangle)->number

        Returns area of rectangle.
        '''

        # Return Area
        return (self.p2.x - self.p1.x) * (self.p2.y - self.p1.y)
    
    def move(self, x, y):
        '''(Rectangle, number, number)->None

        Moves Rectangle.
        '''
        
        # Point 1
        self.p1.move(x, y)
        
        # Point 2
        self.p2.move(x, y)

    def intersects(self, r):
        '''(Rectangle, Rectangle)

        This function returns true if the two rectangles intersect
        and false otherwise.
        '''

        # Check if rectangle intersects other rectangle
        if self.p1.x <= r.p2.x and r.p1.x <= self.p2.x:
            if self.p1.y <= r.p2.y and r.p1.y <= self.p2.y:
                # The rectangles intersect
                return True
        # The rectangles do not intersect
        return False

    ''' Over thought version
    def intersects2(self, r, n = False):
        '(Rectangle, Rectangle, [bool])->bool'
        if self.p1.x <= r.p1.x <= self.p2.x or self.p1.x <= r.p2.x <= self.p2.x:
            # Check for corners inside
            if self.p1.y <= r.p1.y <= self.p2.y or self.p1.y <= r.p2.y <= self.p2.y:
                return True
            # Check for vertical intersect
            elif r.p1.y <= self.p1.y and self.p2.y <= r.p2.y:
                return True
        if self.p1.y <= r.p1.y <= self.p2.y or self.p1.y <= r.p2.y <= self.p2.y:
            # Check for horizontal intersect
            if r.p1.x <= self.p1.x and self.p2.x <= r.p2.x:
                return True
            
        # Check other corners and return
        if not(n):
            r = Rectangle(Point(r.p1.x, r.p1.y), Point(r.p2.x, r.p2.y), "red")
            return self.intersects(r, True)
        return False
    '''
        
    def contains(self, x, y):
        '''(Rectangle, number, number)->bool

        Returns true if rectangle contains the point with coordinates
        at x and y.
        '''

        if self.p1.x <= x <= self.p2.x and self.p1.y <= y <= self.p2.y:
            # Rectangle contains point
            return True
        # Rectangle does not contain point
        return False
     
class Canvas(Rectangle):
    'class that represents the plane'

    def __init__(self):
        '(Canvas)-None'
        self.rects = []

    def __len__(self):
        '''(Canvas)-int

        Returns the number of rectangles on canvas
        '''
        
        return len(self.rects)

    def __repr__(self):
        '''(Canvas)->str

        Returns a string of object
        '''

        return 'Canvas('+str(self.rects)+')'
    
    def add_one_rectangle(self, r):
        '''(Canvas, Rectangle)->None

        Adds a rectangle to the canvas
        '''
        
        self.rects.append(r)
 
    def count_same_color(self, colour):
        '''(Canvas, str)->int

        Returns the number of rectangles with colour, colour
        '''
        
        num = 0

        # loop through list checking for same colour
        for i in self.rects:
            if i.colour == colour:
                num += 1
        return num
        
    def total_perimeter(self):
        '''(Canvas)->int

        Returns the total perimeter of each rectangle
        '''

        total = 0

        # add the perimeters of each rectangle on canvas
        for i in self.rects:
            total += i.get_perimeter()
        return total

    def min_enclosing_rectangle(self):
        '''(Canvas)->Rectangle

        Returns the smallest rectangle that can enclose all rectangles on the canvas.
        '''

        # Starting values
        min_point = [self.rects[0].p1.x, self.rects[0].p1.y]
        max_point = [self.rects[0].p2.x, self.rects[0].p2.y]
        
        for i in self.rects:
            # Check bottom-left point
            if i.p1.x < min_point[0]:
                min_point[0] = i.p1.x
            if i.p1.y < min_point[1]:
                min_point[1] = i.p1.y   
            # Check top-right point
            if i.p2.x > max_point[0]:
                max_point[0] = i.p2.x
            if i.p2.y > max_point[1]:
                max_point[1] = i.p2.y
        return Rectangle(Point(min_point[0], min_point[1]), Point(max_point[0], max_point[1]), 'red')   
        
    def common_point(self):
        '''(Canvas)->bool

        Returns true if there's a common point between all rectangles on canvas
        '''

        # Look for common point
        for i in range(len(self.rects)):
            for j in range(i, len(self.rects)):
                if not(self.rects[i].intersects(self.rects[j])):
                    return False
        return True























    
