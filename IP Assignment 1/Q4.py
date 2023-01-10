from math import log as l

def distance_rocket(a): #To calculate the distance rocket will fly
    t = a
    n = 0
    x = 0
    while t<b:
        x = 2000*l(140000/(140000-2100*t))-9.8*t #formula given in the question
        c = t + 0.25
        y = 2000*l(140000/(140000-2100*c))-9.8*c #formula to find the integration of the next time stop
        avg = (x+y)/2
        n += avg*0.25
        t += 0.25
    return n

#drivers code
if __name__ == '__main__':
    a = int(input("Enter the starting time : "))
    b = int(input("Enter the ending time : "))
    d = distance_rocket(a)
    print("The distance the rocket will fly for :",d)