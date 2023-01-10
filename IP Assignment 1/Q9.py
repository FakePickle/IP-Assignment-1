from math import e #importing math to calculate the log with base e of Demand and supply

def Demand(a,b,p): #returning the demand formula given in the question
    return e**(a-b*p)

def Supply(c,d,p): #returning the supply formula given in the question
    return e**(c+d*p)

def equilibrium(a,b,c,d,pi): #function to find the equilibrium
    while Demand(a,b,pi)>=Supply(c,d,pi):
        pi += pi*0.05
    print("The equilibrium found is at Demand "+str(int(Demand(a,b,pi)))+" and at supply "+str(int(Supply(c,d,pi)))+" at price "+str(pi))

if __name__ == "__main__":
    pi = 1.0 #Given in question to assume initial price as 1.0
    a = 10 #the values of a given in question
    b = 1.05 #the values of b given in question
    c = 1 #the values of c given in question 
    d = 1.06 #the values of d given in question
    equilibrium(a,b,c,d,pi)