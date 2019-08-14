def square(side):
    square = side * side
    return square
def rect(width, height):
    rect = width * height
    return rect
def circumference(radius):
    circumference = 2 * 3.1415 * radius
    return circumference
def question(prompt):
    return input(prompt).lower()

def userinput(prompt = "Do you want to continue? (y/n) "):
    uinpt = None
 
    while uinpt != 'n':
 
        choice = int(input("Area of what you would like to calculate? \n 1-circle \n 2-square \n 3-rectangle \n>>"))
        if choice == 1:
            radius = int(input("Enter radius of a circle "))
            circ = circumference(radius)
            print ("Circumference: ", round(circ, 2))
        elif choice == 2:
            side = int(input("Enter lenght of a side of a square "))
            sqr = square(side)
            print("Square of the square is ", sqr)
        elif choice == 3:
            width = int(input("Enter the width of a rectangle "))
            height = int(input("Enter the height of a rectangle "))
            rectangle = rect(width, height)
            print("Square of the rectangle is ", rectangle)
        uinpt = question(prompt)
 
    else:
        print("Have a good day!")
 
userinput()