def saving_fractions(allowance,t,cost,r):
    c = cost 
    sf = 0.1 
    for i in range(t):
        s = 0 #SAVINGS
        month = 0
        while True:
            s += s*(r/100)
            s += sf*allowance
            month += 1 #Adding 1 to months until the months inputted is equal to the months getting added
            if s>c: #When savings cross the cost of laptop the loop breaks
                break
        if month == t: #When month is equal to the number of months taken as input we come out of the loop
            break
        sf += 0.1 #adding 0.1 to saving fraction until month is equal to the number of months taken as input
    print(f'The saving fraction should be {sf}')

#driver code
if __name__ == '__main__':
    allowance = float(input("The allowance per month is : ")) #allowance per month
    time =int(input("The amount of months you want to buy laptop in : ")) # Number of months to buy laptop
    rate = float(input("Rate of interest per month is : ")) # rate of interest per month
    cost = int(input("Cost of the laptop : ")) # Laptop cost
    saving_fractions(allowance,time,cost,rate)