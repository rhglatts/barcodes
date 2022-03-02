#Rebecca Glatts
#Project 2
#Problem 2

import turtle
#Prints the starting and ending lines to the barcode
def print_start_stop():
    tall_line()

#Draws a short line
def short_line():
    turtle.left(90)
    turtle.forward(30)
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.pendown()

#Draws a tall line
def tall_line():
    turtle.left(90)
    turtle.forward(50)
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.pendown()

#Prints barcode corresponding to 0
def print_zero():
    tall_line()
    tall_line()
    short_line()
    short_line()
    short_line()

#Prints barcode corresponding to 1
def print_one():
    short_line()
    short_line()
    short_line()
    tall_line()
    tall_line()

#Prints barcode corresponding to 2
def print_two():
    short_line()
    short_line()
    tall_line()
    short_line()
    tall_line()

#Prints barcode corresponding to 3
def print_three():
    short_line()
    short_line()
    tall_line()
    tall_line()
    short_line()

#Prints barcode corresponding to 4
def print_four():
    short_line()
    tall_line()
    short_line()
    short_line()
    tall_line()

#Prints barcode corresponding to 5
def print_five():
    short_line()
    tall_line()
    short_line()
    tall_line()
    short_line()

#Prints barcode corresponding to 6
def print_six():
    short_line()
    tall_line()
    tall_line()
    short_line()
    short_line()

#Prints barcode corresponding to 7
def print_seven():
    tall_line()
    short_line()
    short_line()
    short_line()
    tall_line()

#Prints barcode corresponding to 8
def print_eight():
    tall_line()
    short_line()
    short_line()
    tall_line()
    short_line()

#Prints barcode corresponding to 9
def print_nine():
    tall_line()
    short_line()
    tall_line()
    short_line()
    short_line()