'''This is the answer done with updating within the list'''

def total_pop(list):  #To print the total population of the list
    sum = 0
    for i in list:
        sum += i
    return sum

def length(list): #To find the length of the list since we can't use any list functions
    count = 0
    for i in list:
        count += 1
    return count

def year_calc(list):  #To calculate the number of years taken to reach peak population
    Y = 0 #Counting the number of years starting from 0
    cp = total_pop(list) # The sum of current population
    x = 0.025 #The percentage of population that will increase by every year
    sum = 0 #Assigning sum to 0 outside loop for incrementing the sum every year
    while True: #Basically the loop ends when the new sum is lesser than the previous sum
        for i in range(length(list)):
            list[i] += list[i]*(x-(0.004*i))
        sum = total_pop(list) #total sum of the population
        x -= 0.001
        a = cp
        cp = sum #Current population becomes sum of new population
        sum = a #sum becomes the sum of previous populations
        if sum>cp:
            break
        Y += 1 #Incrementing year by one after every loop gets over
    return int(sum*1000000),Y  #multiplying sum by 1 million and type casting
#Drivers Code
if __name__ == "__main__":
    l = list(map(int,input("Enter your list with space between each element : ").split()))
    x,y = year_calc(l)
    print("The peak population will be :",x)
    print("Number of years to reach peak population will be :",y)