def distance(td): #Function to calculate distance
    x = x0 #since we need the value of x0 we assign other variable to x0
    y = y0 #since we need the value of y0 we assign other variable to y0
    while True:
        d = float(input("Enter the distance : "))
        if d <= 0: #To stop the loop from going further
            break
        elif d<=25:
            y+=d
            td+=d #keep on adding distance
        elif d<=50:
            y -= d
            td+=d #keep on adding distance
        elif d<=75:
            x += d
            td+=d #keep on adding distance
        else:
            x -= d
            td+=d #keep on adding distance
    print("The co-ordinates of the new points are : ",x,y)
    print("The distance between point "+str(x0)+','+str(y0)+" and points ",str(x)+','+str(y)+" is : ",td)
    print("The displacement between the two points is : ",((x - x0)**2+(y - y0)**2)**0.5)

if __name__=="__main__":
    x0 = float(input("Enter the starting x coordinate : "))
    y0 = float(input("Enter the starting y coordinate : "))
    total_distance = 0
    distance(total_distance)