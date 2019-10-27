#Albert
'''
This code implements a program that prints out a double half-pyramid
of a specified height.
'''

height = input("Height: ")

#check for if the input is valid
while not height.isdigit() or int(height) < 0 or int(height) > 23:
    height = input("Retry: ")
    
height = int(height)
number = ""
space = height -1

#builds the pyramid
for n in range(height):
    number = space * " " + (n + 2)* "#" + "  " + (n + 2)* "#"
    space = space - 1
    print(number)

    
