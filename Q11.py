from math import log #Except for finding log the module was not used anywhere else

def factorial(n): #Function to calculate the factorial for finding the value of sin and cos
    if n==0: return 1
    elif n==1: return 1 
    else:    
        a=1
        for i in range(1,n+1):
            a *= i
    return a

def sin(x): #Calculating the sin of the angle
    sum = 0
    for n in range(10):
        sum += ((-1)**n)*(x**((2*n)+1))/factorial((2*n)+1)
    return sum

def cos(x): #Calculating the cos of the angle
    sum = 0
    for n in range(10):
        sum += ((-1)**n)*(x**(2*n))/factorial(2*n)
    return sum

def tan(x): #Calculating the tan of the angle
    return sin(x)/cos(x)

def cosec(x): #Calculating the cosec of the angle
    return 1/sin(x)

def sec(x): #Calculating the sec of the angle
    return 1/cos(x)

def cot(x): #Calculating the cot of the angle
    return cos(x)/sin(x)

def radians(x): #Calculating the radians of the angle
    return x*3.14/180

def calculate(a,b): #Main function where all the operations are going to take place
    if operand == '+': return a + b
    elif operand == '-': return a - b
    elif operand == '*': return a * b
    elif operand == '%': return a % b
    elif operand == '/': return a / b
    elif operand == '//': return a // b
    elif operand == 'sin': return sin(a)
    elif operand == 'cos': return cos(a)
    elif operand == 'tan': return tan(a)
    elif operand == 'cosec': return cosec(a)
    elif operand == 'sec': return sec(a)
    elif operand == 'cot': return cot(a)
    elif operand == 'radians': return radians(a)
    elif operand == 'log': return log(a)

#Drivers Code
if __name__ == '__main__':
    print("The operations available are : ")
    print("1. sum(+)")
    print("2. difference(-)")
    print("3. Product(*)")
    print("4. Modulus(%)")
    print("5. Divide(/)")
    print("6. Floor division(//)")
    print("7. sin")
    print("8. cos")
    print("9. tan")
    print("10. cosec")
    print("11. sec")
    print("12. cot")
    print("13. Radians")
    print("14. Log")
    operand = input("Enter operation : ")
    
    if operand == 'sin' or operand == 'cos' or operand == 'tan' or operand == 'cosec' or operand == 'sec' or operand == 'cot' or operand == 'radians' or operand == 'log':
        a = int(input("Enter the number : ")) #taking input of one number since the operation will be taken place only on one number
        print(f'The value of {operand}({a}) is : ',calculate(a,0)) 
    elif operand == '+' or operand == '-' or operand == '*' or operand == '/' or operand == '%' or operand == '//':
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        print(f'The value of {a} {operand} {b} will be :',calculate(a,b))
    else:
        print("Invalid operation")