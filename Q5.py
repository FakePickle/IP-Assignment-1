'''Since there is no end point 
I took extra input for end point of iterations
so we will get proper answer'''

def factorial(n): #Function to find the factorial to calculate sin and cos
    if n==0: return 1
    elif n==1: return 1 
    else:    
        a=1
        for i in range(1,n+1):
            a *= i
        return a

def sin(x, N): #Function to find the sin of angle
    sum = 0
    for n in range(N):
        sum += ((-1)**n)*(x**((2*n)+1))/factorial((2*n)+1) #sin expansion formula
    return sum

def cos(x, N): #Function to find the cos of angle
    sum = 0
    for n in range(N):
        sum += ((-1)**n)*(x**(2*n))/factorial(2*n) #cos expansion formula
    return sum

def tan(x, N): #To find the tan of angle
    return sin(x, N)/cos(x, N) 

def height(a, d, N): #To find the height from bottom to top
    pi = 3.14
    radians = pi/180
    b = a*radians #Converting angle to radians
    return d * tan(b, N)

def line_of_sight(a, d, N): #To find the distance from person's eyes to the top
    pi = 3.14
    radians = pi/180
    b = a*radians #Converting angle to radians
    return d / cos(b, N)

#Drivers code
if __name__ == '__main__':
    angle = float(input("Enter the angle (in degrees): "))
    distance = float(input("Enter the distance: "))
    N = int(input("Enter the number of iterations (N): "))
    if angle == 90:
        print("Since the angle is 90 degrees the line of sight and height will be parallel and the values cannot be calculated")
    elif angle == 0:
        print("Since the angle is 0 degrees the line of sight and distance will be parallel and the values cannot be calculated")
    else:
        print("The height of the object is: ", height(angle,distance,N))
        print("Line of Sight is: ", line_of_sight(angle,distance,N))