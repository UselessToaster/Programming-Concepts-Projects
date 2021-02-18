### calculates the perimeter of a triangle ###

# DRIVER: Tianna Davis (U69901851)
# NAVIGATOR: Peyton Krimmel (U85951028)

# gets user input
print("Enter the 3 side lengths like so: \nx \ny \nz \n")
x = float(input())
y = float(input())
z = float(input())

# repeats prompt until input is valid
while x + y < z or y + z < x or z + x < y:
    print ("Input is not valid, please enter valid triangle side lengths as shown: \nx \ny \nz \n")
    x = float(input())
    y = float(input())
    z = float(input())

#calculates and prints perimeter
else:
    perimeter = x + y + z 
    print(f"The perimeter of your triangle is: {perimeter}")
