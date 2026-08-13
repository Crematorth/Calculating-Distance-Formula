import math

#calculates the distance between the points provided.
def calculateDistanceFormula(x1, y1, x2, y2):
    #Calculates the distance of the previous 2 points using distance formula.
    x_distance = float(math.pow((x2-x1),2))
    y_distance = float(math.pow((y2-y1),2))
    distance = float(math.sqrt(x_distance+y_distance))
    distance = round(distance, 2)
    
    return distance

#Collects coordinates of the 2 points.
def runProgram():
    #Asks the users to input the coordinates of 2 points.
    print("Enter coordinates of Point A:")
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    print("Enter coordinates of Point B:")
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    
    #Calls function to solve for distance formula.
    finaldistance = calculateDistanceFormula(x1, y1, x2, y2)
    
    #Outputs the distance between the 2 points.
    print("The distance between the 2 points is: ",finaldistance," units")

#Constantly checks if the program is run.
while True:
    user_input = input("Enter run to start program: ").strip().lower()
    
    if user_input == "run":
        runProgram()


"""
 Reflection:
It made it so much simpler to get the answer and my code became much more optimized.
"""