# Create a program that calculates the sqft of a room
# make a function that calculates two parameters that are passed in
# take an input for width and height as variables
# call the function and pass in teh width and height
# multiply w * h
# print the final sqft

print("Please enter the dimensions of the room in feet")

def calculate_area(w, h):
    area_sqft = w * h
    print(f"The square footage of this room is: {area_sqft}")


width = int(input("What is the width of the room? "))
height = int(input("What is the height of the room? "))

calculate_area(width, height)
