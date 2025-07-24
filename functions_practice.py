#Exercise 1 - Greeting message
def the_name(name):
    print("Hello", f"{name}")


the_name("Joel")


#Exercise 2 - Calculate area of a rectangle
def rectangle_area(length, width):
    print(length * width)


rectangle_area(10, 5)


#Exercise 3 - Check if a number is even or odd
def check_number(number):
    if number % 2 == 0:
        print("number is even")
    elif number % 2 != 0:
        print("number is odd")

check_number(9)