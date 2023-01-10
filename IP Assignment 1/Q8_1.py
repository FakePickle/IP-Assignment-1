'''Taking number of years as input
so we can find the population at
different years like the population after 15 years etc.
Since we already the number of years taken 
to reach peak population if we input 13
(the number of years taken to reach peak
population) we get the peak population.
This answer is done without updating into the list.'''

def year_calc(list,Y): #To calculate the peak population
    a = 0 #To calculate the number of years
    x = 0.025 #The percentage of population that will increase by every year
    sum = 0 #to calculate the sum of the peak population
    for i in list:
        population = 0
        for j in range(Y):
            i += (population+x)*i
            a = j+1
            population -= 0.001
        sum += i
        x -= 0.004
    return int(sum*1000000),a #Multiplying sum by 1 million because population is supposed to be in millions and type casting it into integer value

#drivers code
if __name__ == "__main__":
    l = list(map(int,input("Enter populations : ").split()))
    Y = int(input("Input the number of years to reach peak population : "))
    print("The current population is :",sum(l))
    x,y = year_calc(l,Y)
    print("The peak population will be :",x)
    print("Number of years to reach peak population will be :",y)