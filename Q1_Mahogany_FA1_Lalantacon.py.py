import math

#Distance formula Loop
while True:
    #Asks the users to input the coordinates of 2 points.
    print("Enter coordinates of Point A:")
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    print("Enter coordinates of Point B:")
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    #Calculates the distance of the previous 2 points using distance formula.
    x_distance = float(math.pow((x2-x1),2))
    y_distance = float(math.pow((y2-y1),2))
    distance = float(math.sqrt(x_distance+y_distance))
    distance = round(distance, 2)

    print("The distance between the 2 points is: ",distance," units")
    
    #Loops the function when user types "Yes"
    if input("Do you need to redo the equation? (Keyword: ""Yes"") ") == "Yes":
        continue
    else:
        break
    
    
    


"""
 Reflection:
It made it so much simpler to get the answer and my code became much more optimized.
"""