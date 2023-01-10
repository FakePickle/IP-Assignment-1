def time(sf,cost,r,allowance): #function to calculate the number of months taken to buy the laptop
    t = 0
    s = 0
    c = cost
    while s<=c: #until the savings crosses the cost of the laptop the loop goes on
        s += s*(r/100)
        s += sf*allowance
        t += 1
    print("The number of months taken to save money and buy laptop is : ",t)
    print("Amount of money remaining after buying laptop is : ",s-c)

#drivers code
if __name__ == '__main__':
    allowance = float(input("The allowance per month is : ")) #allowance per month
    saving_fraction =float(input("The fraction saved every month from allowance : ")) # Saving fraction
    rate = float(input("Rate of interest per month is : ")) # rate of interest per month
    cost = int(input("Cost of the laptop : ")) # Laptop cost
    time(saving_fraction,cost,rate,allowance) #To find the number of months