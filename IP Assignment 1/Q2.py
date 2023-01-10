def Profit(x1): #To find the total profit of chairs plus tables
    while True:
        x2_x = 120 - 2*x1
        x2_y = 200 - 4*x1
        if x2_x == x2_y:
            break
        else:
            x1+=1 #keep on incrementing 1 until x2_x and x2_y are equal
    return x2_x,x2_y #returning only one value as both x2_x and x2_y will be equal

#drivers code
if __name__ == '__main__':
    x1 = 0 #Initializing the value of x1 as 0 to start with
    M = int(input("Enter the input of the number of iterations : "))
    a,b = Profit(x1)
    print("The number of chairs will be :",a)
    print("The number of tables will be :",b)
    if M>a: #This condition is so that when M is greater than or equal to x1, the value of profit will not come negative
        print("The total profit will be :",(M*90+M*25))
    else:
        print("The total profit will be :",(M*90+M*25)+((a-M)*100+(a-M)*30))