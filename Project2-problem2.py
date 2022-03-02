#Rebecca Glatts
#Project 2
#Problem 2

import turtle
import digiprint

#Reads the code from input, gets rid of -, and calls check_sum() 
#to attack the check digit to the zip code
def read_code():
    code = input("Enter in a zip-code: ")
    global code2 
    code2 = code.replace("-","")
    check = str(check_sum())
    code2 = code2 + check
    global window
    #Starts the turtle on the left side of the screen, instead of the middle
    window = turtle.Screen()
    turtle.penup()
    turtle.backward(300)
    turtle.pendown()
    #Calls print_start_stop() to create the start line

    digitprint.print_start_stop()
    #If the digit in the string matches a specific number, it calls
    #the function to print the corresponding barcode for that number
    for i in range (10):
        number = int(code2[i])
        if number == 0:
            digitprint.print_zero()
        elif number == 1:
            digitprint.print_one()
        elif number == 2:
            digitprint.print_two()
        elif number == 3:
            digitprint.print_three()
        elif number == 4:
            digitprint.print_four()
        elif number == 5:
            digitprint.print_five()
        elif number == 6:
            digitprint.print_six()
        elif number == 7:
            digitprint.print_seven()
        elif number == 8:
            digitprint.print_eight()
        else: 
            digitprint.print_nine()

    digitprint.print_start_stop()

#Calculates the check sum by adding up the digits, mod 10, and then 
#subtracting that number from 10 to get the check digit
#Returns a string so it can be concat to the zipcode
def check_sum():
    total = 0
    for i in range (9):
        total += int(code2[i])
    temp = total % 10
    check = 10 - temp
    check = str(check)
    return check



#Main fuction that calls read_code() and exits the turtle window 
#when the user clicks on it
def main() :
    read_code()
    window.exitonclick()

#Calls main
main()

"""
Tests: (Screenshots are attached in pdf)
Enter in a zip-code: 55555-1237

Enter in a zip-code: 38719-3193

Enter in a zip-code: 13223-1345
"""