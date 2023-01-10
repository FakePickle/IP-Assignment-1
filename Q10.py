def poly(x): #returning the polynomial which is given in the question
    return x*x*x-10.5*x*x+34.5*x-35

def derivative_poly(x): #returning the derivative of the polynomial given
    return 3*x*x-21*x+34.5

def root(x): #finding the roots of the polynomial given in the question
    h = poly(x)/derivative_poly(x)
    while abs(h)>0.00000001: #Going through the formula of Newton Raphson method until the absolute value of h becomes smaller than 0.0001
        h = poly(x)/derivative_poly(x)
        x = x-h
    return x

#Drivers code
if __name__ == '__main__':
    x0 = int(input("Input the initial value : "))
    print(f"The root of the polynomial will be :",root(x0))