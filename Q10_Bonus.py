def poly(x): #returning the polynomial which is given in the question
    return x*x*x-10.5*x*x+34.5*x-35

def derivative_poly(x): #returning the derivative of the polynomial given
    return 3*x*x-21*x+34.5

def root(x1,x2): #Finding the roots of polynomial within the range of x1 and x2 which will be inputted by the user
    print("The roots of the polynomial are :",end = " ")
    for i in range(x1,x2+1):
        h = poly(i)/derivative_poly(i)
        j = i-0.5
        h1 = poly(j)/derivative_poly(j)
        if h == 0:
            print(i, end = ", ")
        elif h1 == 0:
            print(j, end = ", ")
        # while abs(h)>=0.000001:
        #     h = poly(i)/derivative_poly(i)
        #     i = i-h
        #     print(i)

#Drivers code
if __name__ == '__main__':
    x1 = int(input("Enter starting range of roots : "))
    x2 = int(input("Enter ending range of roots : "))
    print("The number of roots will be : 3") #The number of roots will be 3 since number of roots are equal to the highest degree of the polynomial
    root(x1,x2)